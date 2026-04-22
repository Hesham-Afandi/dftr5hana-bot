import os
import random
import requests
import sys
from datetime import datetime
from io import BytesIO

# 🔐 الإعدادات
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@BlackWidowHouse"
WEBSITE_URL = "https://hesham-afandi.github.io/DafterKhana/"
LOGO_URL = "https://hesham-afandi.github.io/DafterKhana/logo.png"

# 📚 الاقتباسات (احتفظ بقائمتك الكاملة هنا)
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
    ("المعرفة قوة", "فرانسيس بيكون")
    # ... أضف باقي الاقتباسات هنا ...
]

def send_quote():
    quote, author = random.choice(QUOTES)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    
    caption = (
        f"📚 *اقتباس اليوم | دفتر خانة*\n\n"
        f"✨ \"{quote}\"\n"
        f"🖋️ — {author}\n\n"
        f"🌐 {WEBSITE_URL}\n\n"
        f"#اقتباسات #دفتر_خانة #قراءة #أدب"
    )
    
    # محاولة تحميل اللوجو
    try:
        logo_res = requests.get(LOGO_URL, timeout=10)
        files = {"photo": ("logo.png", BytesIO(logo_res.content), "image/png")} if logo_res.status_code == 200 else None
    except Exception:
        files = None

    payload = {"chat_id": CHANNEL_ID, "caption": caption, "parse_mode": "Markdown"}
    
    try:
        res = requests.post(url, data=payload, files=files, timeout=30)
        print(f"📡 رد تليجرام الخام: [{res.status_code}] {res.text}")
        
        if res.status_code == 200:
            print("✅ تم النشر بنجاح في القناة!")
            sys.exit(0)  # نجاح حقيقي
        else:
            print("❌ رفض تليجرام الرسالة! انظر لرد الـ API بالأعلى.")
            sys.exit(1)  # يفشل الـ Workflow فوراً
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🤖 بدء البوت...")
    print(f"📡 القناة: {CHANNEL_ID}")
    print(f"🌐 الرابط المستخدم: {WEBSITE_URL}")
    send_quote()
