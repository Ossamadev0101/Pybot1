from selenium import webdriver
import time

def run_whatsapp_bot():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)

    while True:
        user_input = input("Enter your message (type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        # إذا كان المستخدم يرسل "hi"، قم بالرد بـ "hello"
        if user_input.lower() == 'hi':
            response = "hello"
        else:
            # إذا لم يتطابق أي شرط، يمكنك إضافة قواعد أخرى هنا
            response = "I'm not sure how to respond to that."

        # يمكنك استخدام response في الرد على واجهة الواتساب هنا
        print("Bot's response:", response)

    driver.quit()

if __name__ == "__main__":
    run_whatsapp_bot()
