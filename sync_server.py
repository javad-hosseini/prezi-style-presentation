"""
سرور ساده برای سینک کردن اسلاید بین چند مانیتور روی شبکه محلی.

نصب:
    pip install fastapi "uvicorn[standard]" --break-system-packages

اجرا (از همون پوشه‌ای که presentation.html توشه):
    uvicorn sync_server:app --host 0.0.0.0 --port 8000

بعدش:
- روی سیستم خودت (Leader) باز کن:
    http://<IP-خودت>:8000/?leader=1
- روی بقیه مانیتورها (Follower) باز کن:
    http://<IP-خودت>:8000/

آی‌پی خودت رو با دستور زیر پیدا کن (لینوکس/مک: ifconfig یا ip addr، ویندوز: ipconfig)
هر بار که روی سیستم Leader اسلاید عوض بشه (کلیک، فلش، Space و ...)
پیام از طریق WebSocket به همه‌ی Followerها فرستاده می‌شه و اونا هم goTo(idx) می‌زنن.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).parent
PRESENTATION_FILE = BASE_DIR / "presentation.html"

connected_clients: list[WebSocket] = []


@app.get("/")
async def serve_presentation():
    return FileResponse(PRESENTATION_FILE)


@app.websocket("/ws")
async def sync_ws(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # هر پیامی که میاد (فقط از Leader فرستاده میشه) رو برای همه پخش کن
            stale = []
            for client in connected_clients:
                try:
                    await client.send_text(data)
                except Exception:
                    stale.append(client)
            for s in stale:
                if s in connected_clients:
                    connected_clients.remove(s)
    except WebSocketDisconnect:
        if websocket in connected_clients:
            connected_clients.remove(websocket)
