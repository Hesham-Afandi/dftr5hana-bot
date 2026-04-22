import os
import random
import requests
from datetime import datetime
from io import BytesIO

# 🔐 الإعدادات
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@BlackWidowHouse"
WEBSITE_URL = "https://hesham-afandi.github.io/DafterKhana/"
LOGO_URL = "https://hesham-afandi.github.io/DafterKhana/logo.png"
SLOGAN = "عقل المؤلف بين يديك"

# 📚 الاقتباسات (نفس اللي في الموقع)
QUOTES = [
    ("الكتب أصدقاء لا يخونون", "مارك توين"),
    ("من يفتح باب مدرسة يغلق باب سجن", "فيكتور هوجو"),
    ("في الكتب أعناق من الجمال لا تُرى إلا بالتدبر", "مصطفى صادق الرافعي"),
    ("غرفة بلا كتب كجسد بلا روح", "شيشرون"),
    ("لا صديق أوفي من كتاب", "إرنست همنغواي"),
    ("القراءة هي بوابة الحكمة", "فرانسيس بيكون"),
    ("الكلمة الحرة هي أساس الحضارة", "طه حسين"),
    ("الأدب مرآة الحياة", "جبران خليل جبران"),
    ("اطلبوا العلم من المهد إلى اللحد", "حديث نبوي"),
    ("المعرفة قوة", "فرانسيس بيكون"),
    ("من سلك طريقاً يلتمس فيه علماً سهل الله له طريقاً إلى الجنة", "حديث نبوي"),
    ("سافر تجد عوضاً عما تفارقه", "المتنبي"),
    ("العلم يرفع بيتاً لا عماد له", "المتنبي"),
    ("إن مع العسر يسراً", "القرآن الكريم"),
    ("خير الناس أنفعهم للناس", "حديث نبوي"),
    ("القلم أقوى من السيف", "مثل إنجليزي"),
    ("العلم في الصغر كالنقش على الحجر", "مثل عربي"),
    ("من سار على الدرب وصل", "مثل عربي"),
    ("من جد وجد ومن زرع حصد", "مثل عربي"),
    ("الصبر مفتاح الفرج", "مثل عربي"),
    ("إنما الأعمال بالنيات", "حديث نبوي"),
    ("الكلمة الطيبة صدقة", "حديث نبوي"),
    ("العلم بلا عمل كالشجر بلا ثمر", "مثل عربي"),
    ("أفضل طريقة للتنبؤ بالمستقبل هي صنعه", "أبراهام لينكولن"),
    ("التعليم هو السلاح الأقوى لتغيير العالم", "نيلسون مانديلا")
]

def download_logo():
    """تحميل اللوجو"""
    try:
        response = requests.get(LOGO_URL, timeout=10)
        if response.status_code == 200:
            return BytesIO(response.content)
    except:
        pass
    return None

def send_quote():
    """إرسال الاقتباس"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    quote, author = random.choice(QUOTES)
    
    caption = (
        f"📚 *اقتباس اليوم | دفتر خانة*\n\n"
        f"✨ \"{quote}\"\n"
        f"🖋️ — {author}\n\n"
        f"🔖 {SLOGAN}\n\n"
        f"🌐 {WEBSITE_URL}\n\n"
        f"#اقتباسات #دفتر_خانة #قراءة #أدب #هشام_أفندي"
    )
    
    logo = download_logo()
    payload = {
        "chat_id": CHANNEL_ID,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    files = {"photo": ("logo.png", logo, "image/png")} if logo else None
    
    try:
        res = requests.post(url, data=payload, files=files, timeout=30)
        if res.status_code == 200:
            print(f"✅ تم النشر | {datetime.now()}")
            print(f"🔗 الرابط: {WEBSITE_URL}")
            return True
        else:
            print(f"❌ خطأ: {res.text}")
            return False
    except Exception as e:
        print(f"❌ استثناء: {e}")
        return False

if __name__ == "__main__":
    print("🤖 بدء البوت...")
    print(f"📡 القناة: {CHANNEL_ID}")
    print(f"🌐 الموقع: {WEBSITE_URL}")
    send_quote()
