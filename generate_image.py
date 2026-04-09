from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import textwrap
import os

# 🎨 إعدادات التصميم (متناسقة مع موقع دفتر خانة)
WIDTH, HEIGHT = 1080, 1080
BG_COLOR = (11, 15, 20)           # خلفية داكنة مثل الموقع
ACCENT_COLOR = (201, 162, 39)     # ذهبي
TEXT_COLOR = (230, 237, 243)      # أبيض مائل للرمادي
AUTHOR_COLOR = (139, 139, 158)    # رمادي للمؤلف
BORDER_COLOR = (201, 162, 39)     # إطار ذهبي

def render_arabic(text):
    """معالجة النص العربي للعرض الصحيح"""
    try:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except:
        return text

def get_font(font_name, size):
    """تحميل الخط مع fallback"""
    font_path = f"fonts/{font_name}"
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        # خطوط بديلة في حال عدم وجود الخطوط المخصصة
        fallbacks = [
            "/usr/share/fonts/truetype/amiri/Amiri-Regular.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "C:/Windows/Fonts/arial.ttf"
        ]
        for fb in fallbacks:
            try:
                return ImageFont.truetype(fb, size)
            except:
                continue
        return ImageFont.load_default()

def create_quote_image(quote, author, output_path="daily_quote.jpg"):
    """إنشاء صورة الاقتباس الاحترافية"""
    
    # إنشاء الصورة
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # رسم إطار ذهبي أنيق
    margin = 40
    draw.rectangle(
        [(margin, margin), (WIDTH-margin, HEIGHT-margin)],
        outline=BORDER_COLOR,
        width=3
    )
    
    # تحميل الخطوط
    font_quote = get_font("Amiri-Regular.ttf", 56)
    font_author = get_font("ArefRuqaa-Regular.ttf", 42)
    font_footer = get_font("ArefRuqaa-Regular.ttf", 32)
    
    # معالجة واقتباس النص
    quote_ar = render_arabic(quote)
    author_ar = render_arabic(f"— {author}")
    footer_ar = render_arabic("دَفْتَرُ خَانَة | لكل كلمة مكان")
    
    # تغليف الاقتباس لعدة أسطر
    max_chars = 28
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= max_chars:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # حساب موضع النص في المنتصف
    line_height = 80
    total_quote_height = len(lines) * line_height
    start_y = (HEIGHT - total_quote_height) // 2 - 20
    
    # رسم الاقتباس سطر سطر
    for i, line in enumerate(lines):
        line_ar = render_arabic(line)
        bbox = draw.textbbox((0, 0), line_ar, font=font_quote)
        text_width = bbox[2] - bbox[0]
        x_pos = (WIDTH - text_width) // 2
        y_pos = start_y + i * line_height
        draw.text((x_pos, y_pos), line_ar, fill=ACCENT_COLOR, font=font_quote)
    
    # رسم اسم المؤلف
    author_bbox = draw.textbbox((0, 0), author_ar, font=font_author)
    author_width = author_bbox[2] - author_bbox[0]
    author_x = (WIDTH - author_width) // 2
    author_y = start_y + total_quote_height + 50
    draw.text((author_x, author_y), author_ar, fill=AUTHOR_COLOR, font=font_author)
    
    # رسم شعار الموقع في الأسفل
    footer_bbox = draw.textbbox((0, 0), footer_ar, font=font_footer)
    footer_width = footer_bbox[2] - footer_bbox[0]
    footer_x = (WIDTH - footer_width) // 2
    footer_y = HEIGHT - 80
    draw.text((footer_x, footer_y), footer_ar, fill=(60, 60, 70), font=font_footer)
    
    # إضافة زخرفة بسيطة
    draw.ellipse([(WIDTH//2 - 5, 30), (WIDTH//2 + 5, 40)], fill=ACCENT_COLOR)
    draw.ellipse([(WIDTH//2 - 5, HEIGHT-40), (WIDTH//2 + 5, HEIGHT-30)], fill=ACCENT_COLOR)
    
    # حفظ الصورة
    img.save(output_path, "JPEG", quality=95, optimize=True)
    print(f"💾 تم حفظ الصورة: {output_path}")
