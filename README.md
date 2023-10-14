# Automatic Work Scheduler README

## Introduction
The Automatic Work Scheduler is a user-friendly Python script designed to automate your daily work routine in the Factorial HR management system. With this script, you can effortlessly log in, clock in, take breaks, log out, and receive notifications via Telegram. This README will guide you through using and customizing the script to meet your specific needs.

## Prerequisites
Before getting started, ensure you have the following prerequisites in place:

- **Python 3.x**: If you don't have it, you can download it from the [official Python website](https://www.python.org/downloads/).

- **Required Python Libraries**: You'll need to install these libraries using `pip`:

    - `selenium`
    - `schedule`
    - `requests`

- **Google Chrome**: The script uses the Chrome web browser, so please make sure you have Chrome installed on your system.

## Configuration
Before running the script, you need to configure some settings to match your specific requirements:

- **Factorial Login Credentials**: Replace the placeholder values with your actual Factorial login credentials in the script:

    ```python
    your_email = "your.email@example.com"
    your_password = "YourPassword123"
    ```

- **Telegram Integration (Optional)**: If you want to receive notifications via Telegram, replace the following placeholders with your own Telegram Bot API token and chat ID:

    ```python
    api_token = 'YOUR_TELEGRAM_BOT_API_TOKEN'
    chat_id = 'YOUR_TELEGRAM_CHAT_ID'
    ```

- **Chrome Profile Path**: Set the path to your Chrome profile to keep yourself logged in. You can find your "profilepath" under "chrome://version/". Replace the placeholder with your path:

    ```python
    options.add_argument("user-data-dir=YOUR_CHROME_PROFILE_PATH")
    ```

## Usage
Running the Automatic Work Scheduler is straightforward. Open your terminal or command prompt, navigate to the script's directory, and execute the script with the following command:

```
python auto_work_scheduler.py
```

## Automated Tasks
The script takes care of various work-related tasks automatically based on the schedule:

1. **Is_Awake_Function (07:50 AM):** This task sends a notification to let you know that the server is active and the script is running.

2. **Login (08:00 AM):** The script logs you into the Factorial system.

3. **First Break:** The script handles your first break, including taking the break and returning from it. The timing can be adjusted as per your schedule.

4. **Lunch:** The script manages your lunch break, taking the break and returning from it. The timing is customizable based on your lunch schedule.

5. **Second Break:** The script manages your second break, including taking the break and returning from it. The timing can be adjusted as per your schedule.

6. **Logout (05:00 PM):** The script logs you out from the Factorial system.

## Important Considerations
- Use this script responsibly and solely for legitimate purposes.

- Ensure that you have the necessary rights and permissions to use the Factorial system and automate your work schedule.

- Keep in mind that websites may have measures to prevent automated actions, which this script attempts to bypass.

- If you choose to integrate Telegram notifications, ensure that you keep your API token and chat ID confidential.

Please respect the terms of service and policies of the website you are interacting with. Unauthorized or improper use of this script may result in legal consequences.