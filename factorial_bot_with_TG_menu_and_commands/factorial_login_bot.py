from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import logging
import warnings
warnings.filterwarnings("ignore", message="Starting with ImageIO v3 the behavior of this function will switch to that of iio.v3.imread.")
import schedule
import requests

# Log errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

instructions = "Instructions:\n\n" \
        "Login: Login you into Factorial\n" \
        "Clockin: Start your Shift\n" \
        "Break On: Start your Break\n" \
        "Break Off: End your Break\n" \
        "Clockout: End your Shift\n" \
        "Status: Check if Program is still awake\n"

# Telegram Bot Token
api_token = 'XXXXXXXXXX'
chat_id = 'XXXXXXXX'

# Giving some credits hehe
print("Factorial Bot coded by TheMysteryPanda")

api_url = f'https://api.telegram.org/bot{api_token}/getUpdates'


# Send Send_Message_Telegram
def Send_Message_Telegram(text):
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': text + "\n" + "https://app.factorialhr.com/dashboard"}
    response = requests.post(api_url, data=params)

def Send_Picture_Telegram(text, screenshot):
    api_url = f'https://api.telegram.org/bot{api_token}/sendPhoto'
    params = {'chat_id': chat_id, 'caption': text + "\n" + "https://app.factorialhr.com/dashboard"}
    files = {'photo': ('screenshot.png', screenshot)}
    response = requests.post(api_url, params=params, files=files)

last_update_id = 0

def function(text):
    # This is only for options
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
    
    if text == "Status":
        time.sleep(10)
        Send_Picture_Telegram("SERVER IS STILL ACTIVE, DON'T WORRY", driver.get_screenshot_as_png())

    # Login
    if text == "Login":
        # Check if we have to login, otherwise let bot do whatever bot has to do
        try:
            time.sleep(10)
            Email_Field = driver.find_element(By.CSS_SELECTOR, "#user_email")
            Password_Field = driver.find_element(By.CSS_SELECTOR, "#user_password")
            Remember_Me_Field = driver.find_element(By.CSS_SELECTOR, "#user_remember_me")
            submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        
            if Email_Field:
                action = ActionChains(driver)
                Email_Field.click()
                action.send_keys("tobias.rubenbauer@clusterosl.com").perform()
                Password_Field.click()
                action.send_keys("Redbull1975!!").perform()
                Remember_Me_Field.click()
                submit_button.click()
                time.sleep(3)
                Send_Picture_Telegram("SUCCESSFULLY LOGGED IN", driver.get_screenshot_as_png())
            else:
                Send_Message_Telegram("COULDNT FIND LOGIN FIELDS")
        except:
            Send_Picture_Telegram("COULDNT LOGIN", driver.get_screenshot_as_png())

    # CLOCKIN / BREAK / BREAK OFF / CLOCKOUT AUTOMATICALLY    
    if text == "Clockin":
        try:
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')))
            clock_in_button = driver.find_element(By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')
            if clock_in_button:
                clock_in_button.click()
                time.sleep(3)
                Send_Picture_Telegram("SUCCESSFULLY CLOCKED-IN", driver.get_screenshot_as_png())
            else:
                Send_Message_Telegram("COULDNT FIND CLOCK-IN BUTTON")
        except:
            Send_Picture_Telegram("COULDNT CLICK CLOCK-IN BUTTON", driver.get_screenshot_as_png())


    if text == "Break On":
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')))
            go_to_break_button = driver.find_element(By.CSS_SELECTOR, 'button.pszv5n1 div.kn616m0 div._1e5wml26 span._1ddb6550')
            if go_to_break_button:
                    go_to_break_button.click()
                    time.sleep(3)
                    Send_Picture_Telegram("SUCCESSFULLY TURNED ON BREAK", driver.get_screenshot_as_png())
            else:
                Send_Message_Telegram("COULDNT FIND BREAK BUTTON")
        except:
            Send_Picture_Telegram("COULDNT CLICK BREAK BUTTON", driver.get_screenshot_as_png())

    if text == "Break Off":
        try:
            wait = WebDriverWait(driver, 40)
            back_from_break_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Back to work')]")))
            if back_from_break_button:
                back_from_break_button.click()
                time.sleep(3)
                Send_Picture_Telegram("SUCCESSFULLY TURNED OFF BREAK", driver.get_screenshot_as_png())
                # try:
                #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._10fn5990._10fn5991 div._10fn5994 div._8w5xc40._8w5xc43s._8w5xc4bv._8w5xc4e0._8w5xc4hj._4arc4f0._1e5wml26 form.ZiyXo div._8w5xc40._8w5xc472._8w5xc47t._8w5xc4bt._8w5xc4by._8w5xc4c1._8w5xc4ck._8w5xc4dz._8w5xc4cu._4arc4f26._4arc4f48._4arc4f3p._1e5wml2u._1e5wml212.ld8cds0 button.pszv5n1:nth-child(1) div.kn616m0 div._8w5xc40._8w5xc46y._8w5xc47q._8w5xc4v._8w5xc437._8w5xc4bv._8w5xc4e0._4arc4fi._4arc4f2._4arc4f23._1e5wml26 div._8w5xc40._8w5xc46v._8w5xc4bt._8w5xc4c1._4arc4f0 div._8w5xc40._8w5xc4bt._8w5xc4cr._4arc4f0 div._8w5xc40._8w5xc46w._8w5xc4bv._8w5xc4hr._4arc4f0 span._1eq2a570._1eq2a57k._1eq2a57r._1eq2a5713._1eq2a576._1eq2a578._1eq2a572t._1eq2a572w > span._1ddb6550")))
                #     break_button_confirm = driver.find_element(By.CSS_SELECTOR, "div._10fn5990._10fn5991 div._10fn5994 div._8w5xc40._8w5xc43s._8w5xc4bv._8w5xc4e0._8w5xc4hj._4arc4f0._1e5wml26 form.ZiyXo div._8w5xc40._8w5xc472._8w5xc47t._8w5xc4bt._8w5xc4by._8w5xc4c1._8w5xc4ck._8w5xc4dz._8w5xc4cu._4arc4f26._4arc4f48._4arc4f3p._1e5wml2u._1e5wml212.ld8cds0 button.pszv5n1:nth-child(1) div.kn616m0 div._8w5xc40._8w5xc46y._8w5xc47q._8w5xc4v._8w5xc437._8w5xc4bv._8w5xc4e0._4arc4fi._4arc4f2._4arc4f23._1e5wml26 div._8w5xc40._8w5xc46v._8w5xc4bt._8w5xc4c1._4arc4f0 div._8w5xc40._8w5xc4bt._8w5xc4cr._4arc4f0 div._8w5xc40._8w5xc46w._8w5xc4bv._8w5xc4hr._4arc4f0 span._1eq2a570._1eq2a57k._1eq2a57r._1eq2a5713._1eq2a576._1eq2a578._1eq2a572t._1eq2a572w > span._1ddb6550")
                #     if break_button_confirm:
                #         break_button_confirm.click()
                #         Send_Message_Telegram("CONFIRMED BREAK")
                #     else:
                #         print("COULDNT CONFIRM BREAK")
                # except:
                # 
                #     print("NO NEED TO CONFIRM BREAK")

            else:
                Send_Message_Telegram("COULDNT FIND BACK FROM BREAK BUTTON ")

        except:
                Send_Picture_Telegram("COULDNT CLICK BACK FROM BREAK BUTTON", driver.get_screenshot_as_png())

    if text == "Clockout":
        try:
            wait = WebDriverWait(driver, 40)
            clock_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Clock out')]")))
            if clock_out_button:
                clock_out_button.click()
                time.sleep(3)
                Send_Picture_Telegram("SUCCESSFULLY CLOCKED-OUT", driver.get_screenshot_as_png())
            else:
                Send_Message_Telegram("COULDNT FIND CLOCK-OUT BUTTON")
        except:
                Send_Picture_Telegram("COULDNT CLICK CLOCK-OUT BUTTON", driver.get_screenshot_as_png())


def check_for_updates():
    global last_update_id
    api_url1 = f'https://api.telegram.org/bot{api_token}/getUpdates?offset={last_update_id}'
    response = requests.get(api_url1)
    if response.status_code == 200:
        data = response.json()
        if len(data['result']) > 0:
            for update in data['result']:
                if 'message' in update and 'text' in update['message']:
                    message_text = update['message']['text']
                    if message_text == "Login":
                        function("Login")
                    if message_text == "Status":
                        function("Status")
                    if message_text == "Clockin":
                        function("Clockin")
                    if message_text == "Clockout":   
                        function("Clockout")
                    if message_text == "Break On":
                        function("Break On")
                    if message_text == "Break Off":
                        function("Break Off")
                    if message_text == "Help":
                        Send_Message_Telegram(instructions)
                    else:
                        print(message_text)
                    last_update_id = update['update_id'] + 1
       


# Login

schedule.every().friday.at("07:57").do(function, "Clockin")
schedule.every().friday.at("09:45").do(function, "Break On")
schedule.every().friday.at("10:01").do(function, "Break Off")
schedule.every().friday.at("12:00").do(function, "Break On")
schedule.every().friday.at("13:00").do(function, "Break Off")
schedule.every().friday.at("14:45").do(function, "Break On")
schedule.every().friday.at("15:01").do(function, "Break Off")
schedule.every().friday.at("17:00").do(function, "Clockout")

schedule.every().thursday.at("07:57").do(function, "Clockin")
schedule.every().thursday.at("09:45").do(function, "Break On")
schedule.every().thursday.at("10:01").do(function, "Break Off")
schedule.every().thursday.at("12:00").do(function, "Break On")
schedule.every().thursday.at("13:00").do(function, "Break Off")
schedule.every().thursday.at("14:45").do(function, "Break On")
schedule.every().thursday.at("15:01").do(function, "Break Off")
schedule.every().thursday.at("17:00").do(function, "Clockout")

schedule.every().wednesday.at("07:57").do(function, "Clockin")
schedule.every().wednesday.at("09:55").do(function, "Break On")
schedule.every().wednesday.at("10:11").do(function, "Break Off")
schedule.every().wednesday.at("12:00").do(function, "Break On")
schedule.every().wednesday.at("13:00").do(function, "Break Off")
schedule.every().wednesday.at("14:45").do(function, "Break On")
schedule.every().wednesday.at("15:01").do(function, "Break Off")
schedule.every().wednesday.at("17:00").do(function, "Clockout")

schedule.every().tuesday.at("07:57").do(function, "Clockin")
schedule.every().tuesday.at("09:45").do(function, "Break On")
schedule.every().tuesday.at("10:01").do(function, "Break Off")
schedule.every().tuesday.at("12:00").do(function, "Break On")
schedule.every().tuesday.at("13:00").do(function, "Break Off")
schedule.every().tuesday.at("14:45").do(function, "Break On")
schedule.every().tuesday.at("15:01").do(function, "Break Off")
schedule.every().tuesday.at("17:00").do(function, "Clockout")

schedule.every().monday.at("07:57").do(function, "Clockin")
schedule.every().monday.at("09:45").do(function, "Break On")
schedule.every().monday.at("10:01").do(function, "Break Off")
schedule.every().monday.at("12:00").do(function, "Break On")
schedule.every().monday.at("13:00").do(function, "Break Off")
schedule.every().monday.at("14:45").do(function, "Break On")
schedule.every().monday.at("15:01").do(function, "Break Off")
schedule.every().monday.at("17:00").do(function, "Clockout")

# Check for Updates every 3 seconds
schedule.every(3).seconds.do(check_for_updates)

# Keep Program running
while True:
    schedule.run_pending()
    time.sleep(1)
