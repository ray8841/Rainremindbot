
# Weather Monitoring with LINE Notify - README

This project is a Python-based weather monitoring service that checks for rain in multiple global cities every 30 minutes. If rain is detected, a notification is sent to a LINE Notify account. The project uses OpenWeatherMap for weather data and Ngrok to expose the local Flask server to the public for testing purposes.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Additional Notes](#additional-notes)

---

### Prerequisites

Before running this project, ensure you have:

1. **Python 3.x**: This project requires Python 3.
2. **Ngrok**: Used to expose your local server to the internet.
3. **LINE Notify Token**: Required for sending notifications to your LINE account.
4. **OpenWeatherMap API Key**: Used to fetch weather data for different cities.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-line-notify.git
   cd weather-line-notify
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The main dependencies are:
   - `Flask`: For the web server.
   - `requests`: For making API calls.
   - `pyngrok`: To create a public URL for the local server.

3. **Install Ngrok**:
   You can download Ngrok from [https://ngrok.com/](https://ngrok.com/) and follow the installation instructions.

### Configuration

1. **Configure LINE Notify Token**:
   - Go to [LINE Notify](https://notify-bot.line.me/en/), log in, and generate a new token.
   - Replace `YOUR_LINE_NOTIFY_TOKEN` in `main.py` with the token.

2. **Configure OpenWeatherMap API Key**:
   - Sign up on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get an API key.
   - Replace `YOUR_OPENWEATHERMAP_API_KEY` in `main.py` with the API key.

### Usage

1. **Start Ngrok**:
   ```bash
   ngrok http 5000
   ```
   This command creates a public URL that will forward requests to your local Flask server on port 5000.

2. **Run the Flask Application**:
   ```bash
   python main.py
   ```

3. **View Ngrok URL**:
   The Ngrok URL will be printed in the console. You can use this URL to interact with the server or configure it for external webhooks if necessary.

4. **Automatic Rain Check**:
   The application will automatically check the weather in each specified city every 30 minutes. If it detects rain, it sends a notification to the LINE Notify account.

### Project Structure

- **main.py**: Main script containing the application logic for checking weather, sending LINE notifications, and starting the server.
- **requirements.txt**: List of required Python packages.

### Additional Notes

- This project is designed for testing and educational purposes. For production use, consider hosting on a reliable server and securing API keys properly.
- If you encounter any issues with Ngrok timing out, remember that free Ngrok sessions can sometimes expire. Simply restart Ngrok and update the Webhook URL if needed.

---

Feel free to contribute to the project by creating pull requests for improvements or adding support for additional weather providers or features. Happy coding!
