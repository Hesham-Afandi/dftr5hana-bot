from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# 🎨 إعدادات التصميم (متناسقة مع ألوان موقعك)
WIDTH, HEIGHT = 1080, 1080
BG_COLOR = (11, 15, 20)           # خلفية داكنة
ACCENT_COLOR = (201, 162, 39)     # ذهبي
TEXT_COLOR = (230, 237, 243)      # أبيض مائل للرمادي
AUTHOR_COLOR = (139, 139, 158)    # رمادي للمؤلف

def get_font(size, bold=False):
    """تحميل خطوط نظام آمنة ومتوفرة دائماً على خوادم GitHub"""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:/Windows/Fonts/arial.ttf"
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

def create_quote_image(quote, author, output_path="daily_quote.jpg"):
    """إنشاء صورة الاقتباس بتصميم إنجليزي/لاتيني آمن"""
    
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # رسم إطار ذهبي أنيق
    margin = 40
    draw.rectangle(
        [(margin, margin), (WIDTH-margin, HEIGHT-margin)],
        outline=ACCENT_COLOR,
        width=3
    )
    
    # تحميل الخطوط
    font_title = get_font(48, bold=True)
    font_quote = get_font(42)
    font_author = get_font(36, bold=True)
    font_footer = get_font(28)
    
    # 1. العنوان الإنجليزي
    draw.text((WIDTH//2, 140), "QUOTE OF THE DAY", fill=ACCENT_COLOR, font=font_title, anchor="mm")
    
    # 2. نص الاقتباس (يدعم التفاف الأسطر تلقائياً)
    max_chars = 32
    lines = textwrap.wrap(quote, width=max_chars)
    y_pos = 260
    for line in lines:
        draw.text((WIDTH//2, y_pos), line, fill=TEXT_COLOR, font=font_quote, anchor="mm")
        y_pos += 65
        
    # 3. اسم المؤلف
    author_text = f"— {author}"
    draw.text((WIDTH//2, y_pos + 40), author_text, fill=AUTHOR_COLOR, font=font_author, anchor="mm")
    
    # 4. شعار الموقع بالأسفل
    draw.text(
        (WIDTH//2, HEIGHT - 90), 
        "Daftar Khana | Every Word Has Its Place", 
        fill=(60, 60, 70), 
        font=font_footer, 
        anchor="mm"
    )
    
    # حفظ الصورة بجودة عالية
    img.save(output_path, "JPEG", quality=95, optimize=True)
    print(f"💾 تم حفظ الصورة بنجاح: {output_path}")
