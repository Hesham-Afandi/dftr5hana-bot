import os
import random
import requests
from datetime import datetime

# 🔐 إعدادات البوت (تُقرأ تلقائياً من GitHub Secrets)
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@BlackWidowHouse"
WEBSITE_URL = "https://dftr5ana.netlify.app/?utm_source=telegram&utm_medium=bot&utm_campaign=daily_quote"
QUOTES_FILE = "quotes.txt"

def load_quotes():
    """تحميل الاقتباسات من ملف النص"""
    if not os.path.exists(QUOTES_FILE):
        print(f"⚠️ ملف {QUOTES_FILE} غير موجود!")
        return []
    with open(QUOTES_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and "|" in line]
    return [line.split("|", 1) for line in lines]

def send_text_message(quote, author):
    """إرسال اقتباس نصي منسق للقناة"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    message = (
        f"📖 *اقتباس اليوم من دفتر خانة*\n\n"
        f"🔹 \"{quote}\"\n"
        f"— {author}\n\n"
        f"🌐 اكتشف آلاف الكتب والاقتباسات:\n{WEBSITE_URL}\n\n"
        f"#اقتباسات #دفتر_خانة #قراءة #أدب #هشام_أفندي"
    )
    
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    res = requests.post(url, json=payload)
    if res.status_code == 200:
        print(f"✅ تم النشر بنجاح | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        return True
    else:
        print(f"❌ فشل النشر: {res.text}")
        return False

def main():
    print("🤖 بدء بوت دفتر خانة (نسخة نصية)...")
    
    quotes = load_quotes()
    if not quotes:
        print("⚠️ لا توجد اقتباسات صالحة في الملف!")
        return
        
    quote, author = random.choice(quotes)
    print(f"📡 جاري إرسال: {quote[:30]}...")
    send_text_message(quote, author)

if __name__ == "__main__":
    main()
