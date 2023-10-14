# Factorial Bot

Automate your daily work routine in Factorial HR with this Python script! The Factorial Bot logs you in, clocks you in and out, takes breaks, and sends updates via Telegram. This README provides a guide on using and configuring the script.

![Factorial Bot](https://www.example.com/path/to/your/image.png)

## Prerequisites

Before using the Factorial Bot, ensure you have the following prerequisites:

- **Python 3.x**: Download and install Python from the [official website](https://www.python.org/downloads/).

- **Required Python Libraries**: Install these libraries using pip:

  - `selenium`
  - `schedule`
  - `requests`

- **Google Chrome**: Make sure you have Google Chrome installed on your system.

## Configuration

Customize the script to your needs by following these steps:

- **Factorial Login Credentials**: Replace the placeholder values in the script with your actual Factorial login credentials:

  ```python
  your_email = "your.email@example.com"
  your_password = "YourPassword123"
  ```

- **Telegram Integration (Optional)**: To receive notifications via Telegram, insert your Telegram Bot API token and chat ID in the script:

  ```python
  api_token = 'YOUR_TELEGRAM_BOT_API_TOKEN'
  chat_id = 'YOUR_TELEGRAM_CHAT_ID'
  ```

- **Chrome Profile Path**: Set the path to your Chrome profile for automatic login. You can find your "profilepath" under "chrome://version/":

  ```python
  options.add_argument("user-data-dir=/path/to/your/chrome/profile")
  ```

## Usage

Running the Factorial Bot is simple. Open your terminal or command prompt, navigate to the script's directory, and execute the script with this command:

```bash
python factorial_bot.py
```

## Automated Tasks

The script takes care of various work-related tasks automatically based on the schedule:

1. **Is_Awake_Function (07:50 AM):** Sends a notification to let you know that the server is active and the script is running.

2. **Login (08:00 AM):** Logs you into the Factorial system.

3. **Breaks:** Manages your breaks, including taking the break and returning from it. The timing can be adjusted as per your schedule.

4. **Lunch:** Manages your lunch break, taking the break and returning from it. The timing is customizable based on your lunch schedule.

5. **Logout (05:00 PM):** Logs you out from the Factorial system.

## Important Considerations

- Use the script responsibly and only for legitimate purposes.

- Ensure you have the necessary rights and permissions to use the Factorial system and automate your work schedule.

- Keep in mind that websites may have measures to prevent automated actions, which this script attempts to bypass.

- If you choose to integrate Telegram notifications, keep your API token and chat ID confidential.

Please respect the terms of service and policies of the website you are interacting with. Unauthorized or improper use of this script may result in legal consequences.