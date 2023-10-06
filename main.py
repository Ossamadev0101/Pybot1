from selenium import webdriver
import time

def run_whatsapp_bot():
    # إعداد متصفح الويب
    driver = webdriver.Chrome()  # يمكنك استخدام متصفح آخر
    driver.get("https://web.whatsapp.com/")

    # انتظار حتى يتم تحميل صفحة واتساب
    time.sleep(15)

    # القيام بإجراءات إضافية بعد تحميل الصفحة، مثل إرسال رسالة أو استجابة للرسائل

    # إغلاق متصفح الويب بعد الانتهاء
    driver.quit()

if __name__ == "__main__":
    run_whatsapp_bot()
