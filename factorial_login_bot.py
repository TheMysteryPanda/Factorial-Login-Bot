from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import schedule
import requests


# Replace this with your real login data
your_email = "stinkysocks@socks.socks"
your_password = "TEST123"

# Replace this with your real Telegram tokens
# * To lazy to google? Got you... https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token
api_token = 'yourtoken'
chat_id = 'yourchatid'


# I use Telegram Message, so I get notified on my phone if everything worked well
def Telegram_Message(message):

    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    response = requests.post(api_url, data=params)
    print(response.json())

def Is_Awake_Function():
    Telegram_Message("Factorial - SERVER IS STILL ACTIVE, DON'T WORRY")

def function(text):
# Get current Time
    current_time = time.ctime()
    options = webdriver.ChromeOptions()
    # Omline define path of chromedriver on windows
    # driver = webdriver.Chrome(executable_path="/home/tobi/Programs/chromedriver.exe", options=options)

    # For Linux and Mac use this line:
    driver = webdriver.Chrome()

    # ! Change this to your chrome profile path. This will keep you logged in (most of the time)
    # You can find your "profilepath" under "chrome://version/"
    options.add_argument("user-data-dir=/home/tobi/.config/google-chrome")

    # Open Factorial
    driver.get("https://app.factorialhr.com/dashboard")

    # Check if we have to login, otherwise let bot do whatever bot has to do
    try:
        wait = WebDriverWait(driver, 40)
        Email_Field = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#user_email"))
        Password_Field = driver.find_element(By.CSS_SELECTOR, "#user_password")
        Remember_Me_Field = driver.find_element(By.CSS_SELECTOR, "#user_remember_me")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    
        if Email_Field:
            action = ActionChains(driver)
            Email_Field.click()
            action.send_keys(your_email).perform()
            Password_Field.click()
            action.send_keys(your_password).perform()
            Remember_Me_Field.click()
            submit_button.click()
        else:
            print("COULDNT LOGIN")
    except:
        print("NO LOGIN NEEDED")

    # LOGIN / BREAK / BREAK OFF / LOGOUT AUTOMATICALLY
    if text == "clockin":
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')))
            clock_in_button = driver.find_element(By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')
            if clock_in_button:
                clock_in_button.click()
                Telegram_Message("Factorial - SUCCESSFULLY CLOCKED-IN")
            else:
                Telegram_Message("Factorial - COULDNT FIND CLOCK-IN BUTTON")
        except:
            Telegram_Message("Factorial - COULDNT CLICK CLOCK-IN BUTTON")

    if text == "turn on break":
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')))
            go_to_break_button = driver.find_element(By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')
            if go_to_break_button:
                    go_to_break_button.click()
                    Telegram_Message("Factorial - WENT TO BREAK")
            else:
                Telegram_Message("Factorial - COULDNT CLICK BREAK")
        except:
            Telegram_Message("Factorial - COULDNT FIND BREAK")

    if text == "turn off break":
        try:
            wait = WebDriverWait(driver, 40)
            back_from_break_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Back to work')]")))

            if back_from_break_button:
                back_from_break_button.click()
                Telegram_Message("Factorial - CAME FROM BREAK")
                # try:
                #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._10fn5990._10fn5991 div._10fn5994 div._8w5xc40._8w5xc43s._8w5xc4bv._8w5xc4e0._8w5xc4hj._4arc4f0._1e5wml26 form.ZiyXo div._8w5xc40._8w5xc472._8w5xc47t._8w5xc4bt._8w5xc4by._8w5xc4c1._8w5xc4ck._8w5xc4dz._8w5xc4cu._4arc4f26._4arc4f48._4arc4f3p._1e5wml2u._1e5wml212.ld8cds0 button.pszv5n1:nth-child(1) div.kn616m0 div._8w5xc40._8w5xc46y._8w5xc47q._8w5xc4v._8w5xc437._8w5xc4bv._8w5xc4e0._4arc4fi._4arc4f2._4arc4f23._1e5wml26 div._8w5xc40._8w5xc46v._8w5xc4bt._8w5xc4c1._4arc4f0 div._8w5xc40._8w5xc4bt._8w5xc4cr._4arc4f0 div._8w5xc40._8w5xc46w._8w5xc4bv._8w5xc4hr._4arc4f0 span._1eq2a570._1eq2a57k._1eq2a57r._1eq2a5713._1eq2a576._1eq2a578._1eq2a572t._1eq2a572w > span._1ddb6550")))
                #     break_button_confirm = driver.find_element(By.CSS_SELECTOR, "div._10fn5990._10fn5991 div._10fn5994 div._8w5xc40._8w5xc43s._8w5xc4bv._8w5xc4e0._8w5xc4hj._4arc4f0._1e5wml26 form.ZiyXo div._8w5xc40._8w5xc472._8w5xc47t._8w5xc4bt._8w5xc4by._8w5xc4c1._8w5xc4ck._8w5xc4dz._8w5xc4cu._4arc4f26._4arc4f48._4arc4f3p._1e5wml2u._1e5wml212.ld8cds0 button.pszv5n1:nth-child(1) div.kn616m0 div._8w5xc40._8w5xc46y._8w5xc47q._8w5xc4v._8w5xc437._8w5xc4bv._8w5xc4e0._4arc4fi._4arc4f2._4arc4f23._1e5wml26 div._8w5xc40._8w5xc46v._8w5xc4bt._8w5xc4c1._4arc4f0 div._8w5xc40._8w5xc4bt._8w5xc4cr._4arc4f0 div._8w5xc40._8w5xc46w._8w5xc4bv._8w5xc4hr._4arc4f0 span._1eq2a570._1eq2a57k._1eq2a57r._1eq2a5713._1eq2a576._1eq2a578._1eq2a572t._1eq2a572w > span._1ddb6550")
                #     if break_button_confirm:
                #         break_button_confirm.click()
                #         Telegram_Message("CONFIRMED BREAK")
                #     else:
                #         print("COULDNT CONFIRM BREAK")
                # except:
                # 
                #     print("NO NEED TO CONFIRM BREAK")

        except:
                print("Factorial - COULDNT TURN OFF BREAK")

    if text == "clockout":
        try:
            wait = WebDriverWait(driver, 40)
            clock_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Clock out')]")))
            if clock_out_button:
                clock_out_button.click()
                Telegram_Message("Factorial - SUCCESSFULLY CLOCKED-OUT")
            else:
                Telegram_Message("Factorial - COULDNT FIND CLOCKED-OUT BUTTON")
        except:
            Telegram_Message("Factorial - COULDNT CLICK CLOCKED-OUT BUTTON")

# Check if is awake

schedule.every().day.at("07:50").do(Is_Awake_Function)

# Login
schedule.every().day.at("08:00").do(function, "clockin")

# First Break
schedule.every().day.at("09:45").do(function, "turn on break")
schedule.every().day.at("10:02").do(function, "turn off break")

# Lunch
schedule.every().day.at("12:00").do(function, "turn on break")
schedule.every().day.at("13:00").do(function, "turn off break")


# Second Break
schedule.every().day.at("14:45").do(function, "turn on break")
schedule.every().day.at("15:00").do(function, "turn off break")

# Logout
schedule.every().day.at("17:00").do(function, "clockout")


# Keep Program running
while True:
    schedule.run_pending()
    time.sleep(1)