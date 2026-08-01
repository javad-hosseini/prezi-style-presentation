تو یک توسعه‌دهنده فرانت‌اند حرفه‌ای، متخصص Creative Coding و ساخت پرزنتیشن‌های تعاملی سبک Prezi هستی.

محتوای پیوست شده را به یک Presentation تعاملی بسیار حرفه‌ای در قالب یک فایل HTML واحد تبدیل کن.

خروجی باید:

- فقط یک فایل HTML کامل و اجرایی باشد.
- تمام CSS و JavaScript داخل همان فایل HTML قرار داشته باشند.
- بدون هیچ کتابخانه خارجی، CDN یا dependency باشد.
- بدون نیاز به build شدن یا نصب چیزی اجرا شود.
- خروجی نباید یک صفحه اسکرولی باشد؛ باید یک اسلایدشو تعاملی واقعی شبیه Prezi باشد.
- تمام جزئیات بصری، انیمیشن‌ها، کنترل‌ها و تعاملات ذکرشده را دقیق پیاده‌سازی کن.
- هیچ بخشی را خلاصه یا حذف نکن.

==================================================
ARCHITECTURE CORE — ساختار حیاتی پرزنتیشن
==================================================

این پرزنتیشن یک Slide Show است، نه یک صفحه Scroll.

1) Canvas و Frames:

یک بوم بزرگ ثابت ایجاد کن:

Canvas:
5100 × 6200 px

Stage:

- تمام صفحه
- overflow:hidden
- viewport ثابت

تمام Frame ها به صورت:

<section>

با:

position:absolute

روی Canvas قرار بگیرند.

هر Frame دارای:

data-x
data-y
data-width
data-height
data-rotation

باشد.

هر Frame باید:

- موقعیت مستقل داشته باشد.
- اندازه متفاوت داشته باشد.
- چرخش جزئی داشته باشد.

Rotation:
بین ±2 درجه

تا حس یک نقشه بصری Prezi ایجاد شود.

==================================================
CAMERA SYSTEM — سیستم دوربین Prezi
==================================================

Viewport نقش دوربین را دارد.

برای فوکوس روی هر Frame دقیقاً از این منطق استفاده کن:

canvas.style.transform =

translate(${vw/2}px, ${vh/2}px)
rotate(${rot}deg)
scale(${s})
translate(${-cx}px, ${-cy}px)

با:

transform-origin: 0 0

که:

s = min(
vw * 0.94 / frameWidth,
vh * 0.86 / frameHeight
)

هدف:

Frame حدود 90 درصد صفحه را پر کند.

Transition دوربین:

transform:

1.3s cubic-bezier(.66,.02,.24,1)

حرکت دوربین باید حس پرواز واقعی بین بخش‌ها داشته باشد.

==================================================
RAD MAP / مسیر حرکت
==================================================

روی Canvas یک مسیر بصری ایجاد کن:

- استفاده از SVG
- مسیر نرم Catmull-Rom بین مرکز تمام Frame ها
- نمایش مسیر حرکت بین بخش‌ها

ویژگی‌ها:

- خط مسیر اصلی
- Progress line با:

stroke-dasharray
stroke-dashoffset

- Marker های دایره‌ای شماره‌دار روی هر Frame

==================================================
OVERVIEW MODE
==================================================

یک حالت Overview بساز:

- کل نقشه Presentation را در viewport نمایش دهد.
- Camera تمام Frame ها را fit کند.
- تمام مسیر و Frame ها دیده شوند.

با کلیک روی هر Frame:

Camera به همان Frame Navigate کند.

==================================================
VISUAL SYSTEM — سیستم بصری
==================================================

CSS Theme System:

از CSS Variables استفاده کن:

--bg
--fg
--acc
--acc2
--line

هر Frame باید Theme مستقل داشته باشد.

Theme هنگام ورود به Frame تغییر کند:

body[data-theme]

ترکیبی از:

- Dark theme
- Light theme

متناسب با موضوع هر بخش.

Transition تغییر Theme:

0.9 seconds

==================================================
BACKGROUND EFFECTS
==================================================

پس زمینه چندلایه بساز:

- Floating bokeh particles
- Animated film grain noise
- Vignette effect

==================================================
FRAME CONTENT ANIMATION
==================================================

محتوای هر Frame هنگام فعال شدن:

Staggered Reveal

داشته باشد.

المان‌ها به صورت مرحله‌ای ظاهر شوند.

Animation ها:

فقط وقتی Frame فعال است اجرا شوند.

وقتی Frame غیرفعال شد:

animation باید pause شود.

منطق:

.frame.active

و:

.rv reveal elements

==================================================
INTERACTIVE DEMOS
==================================================

حداقل 3 Frame باید دارای Demo تعاملی یا Animation مرتبط با موضوع خود باشند.

این Demo ها باید:

- شناور باشند.
- جذاب باشند.
- با موضوع همان بخش هماهنگ باشند.

==================================================
HUD SYSTEM
==================================================

یک HUD ثابت و مینیمال ایجاد کن.

شامل:

بالا:

- نام بخش فعلی
- شماره Frame

پایین:

- Navigation
- Progress indicator

HUD نباید باعث حواس‌پرتی مخاطب شود.

==================================================
LANGUAGE & TYPOGRAPHY
==================================================

کل Presentation:

RTL باشد.

زبان:
فارسی

فونت‌ها:

Google Fonts:

Lalezar برای تیترها

Vazirmatn برای متن‌ها

==================================================
PRESENTER REMOTE SUPPORT
(PowerPoint Compatible)
==================================================

این Presentation باید با Remote Presenter های استاندارد کار کند.

تمام Mapping های زیر را دقیقاً مثل PowerPoint پیاده کن:

NEXT:

PageDown
ArrowDown
ArrowRight
Space
Enter
N

PREVIOUS:

PageUp
ArrowUp
ArrowLeft
Backspace
P

BLACKOUT:

کلید:

B

یا:

.

یک overlay کاملاً سیاه روی همه چیز ایجاد کند.

با:

B
.
یا Esc

بازگردد.

شامل HUD نیز باشد.

WHITEOUT:

کلید:

W

یا:

F5

صفحه کاملاً سفید شود.

FIRST / LAST:

Home:

اولین Frame

End:

آخرین Frame

F5:

Restart از Frame اول

NUMBER + ENTER:

پرش مستقیم به Frame شماره n

رفتار:

- اعداد تایپ شده جمع شوند.
- یک indicator کوچک روی صفحه شماره تایپ شده را نشان دهد.
- indicator به صورت fade حذف شود.

OVERVIEW:

M

HELP:

H

Esc:

خروج از هر Mode

==================================================
ADDITIONAL INPUT METHODS
==================================================

پشتیبانی شود:

- Mouse wheel throttled
- Touch swipe
- Previous/Next buttons
- Clickable progress dots روی صفحه

==================================================
KEYBOARD TECHNICAL DETAILS
==================================================

بعد از کلیک روی هر button:

اجرا کن:

document.activeElement.blur()

تا Space یا Enter دوباره همان دکمه را trigger نکند.

برای:

Space
Arrow keys

حتماً:

e.preventDefault()

قرار بده.

Keyboard handling هنگام focus بودن روی:

<input>

<textarea>

غیرفعال باشد.

Navigation:

در ابتدا و انتهای Presentation:

Loop نداشته باشد.

یعنی:

Frame اول + Previous:
هیچ کاری نکند.

Frame آخر + Next:
هیچ کاری نکند.

==================================================
TECHNICAL REQUIREMENTS
==================================================

Implement exactly:

Stage:

full viewport
overflow hidden

Canvas:

fixed 5100x6200px

Canvas:

transform-origin:0 0

Frames:

data-x/y/w/h/rot attributes

Camera:

translate + rotate + scale

Transition:

1.3s cubic-bezier(.66,.02,.24,1)

SVG:

Catmull-Rom path

Progress:

stroke-dasharray/dashoffset

Themes:

body[data-theme]

Reveal:

.frame.active

Animation:

paused when inactive

No libraries.

Single self-contained HTML.

RTL Persian Presentation.

Generate the complete final HTML code only.
