# 🌤️ Weather App

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt5](https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white)

A modern, user-friendly desktop weather application built with Python and PyQt5. Get real-time weather information for any city worldwide with an intuitive graphical interface.

## ✨ Features

- 🌍 **Global Weather Data** - Search weather for any city worldwide
- 🌡️ **Real-time Information** - Current temperature, weather conditions, and descriptions
- 😊 **Weather Emojis** - Visual weather representation with emojis
- 🎨 **Clean UI** - Modern, easy-to-use graphical interface
- ⚡ **Fast & Responsive** - Quick weather lookups with comprehensive error handling
- 🔒 **Secure API Key Management** - Prompt-based API key input

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **GUI Framework:** PyQt5
- **HTTP Client:** requests
- **Weather API:** OpenWeatherMap API

## 📋 Prerequisites

Before running the application, ensure you have:

1. **Python 3.8 or higher** installed
   - Download from [python.org](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **OpenWeatherMap API Key**
   - Sign up for free at [OpenWeatherMap](https://openweathermap.org/api)
   - Navigate to API Keys section
   - Generate a new API key (free tier allows 1,000 calls/day)

## 🔑 How to Get a Free API Key

1. **Sign Up**: Create a free account at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
2. **Verify Email**: Check your inbox and verify your email address
3. **Get Key**:
   - Go to your account dashboard
   - Click on the **"API keys"** tab
   - You'll see a default key generated for you (or create a new one)
4. **Copy & Use**: Copy the API key string and paste it into the Weather App when prompted

> **Note**: A new API key may take 10-15 minutes to become active. If you get an error initially, please wait a few minutes.

## 🚀 Installation

### Step 1: Clone or Download

```bash
# If using Git
git clone <repository-url>
cd "Python projects"

# Or simply navigate to the directory
cd "d:\Projects\Python projects"
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Running the Application

```bash
python weather.py
```

### First-Time Setup

1. **Launch the app** - Run `python weather.py`
2. **Enter API Key** - A dialog will prompt you to enter your OpenWeatherMap API key
3. **Search Weather** - Enter any city name and click "Get Weather"

### Using the App

1. Type a city name in the input field (e.g., "London", "New York", "Tokyo")
2. Click the **"Get Weather"** button
3. View the results:
   - Temperature in Fahrenheit
   - Weather emoji representation
   - Weather description

## 🎨 Weather Emoji Guide

| Emoji | Weather Condition |
|-------|------------------|
| ⛈ | Thunderstorm |
| 🌦 | Drizzle |
| 🌧 | Rain |
| ❄ | Snow |
| 🌫 | Fog/Mist |
| 🌋 | Volcanic Ash |
| 💨 | Squalls |
| 🌪 | Tornado |
| ☀ | Clear Sky |
| ☁ | Clouds |

## 🔧 Troubleshooting

### Common Issues

**Issue: "Unauthorized: Invalid API key"**
- Solution: Verify your API key is correct and active
- Check if you've activated the API key in your OpenWeatherMap account

**Issue: "Not found: City not found"**
- Solution: Check the spelling of the city name
- Try using the city name in English
- For cities with common names, try adding the country code (e.g., "Paris, FR")

**Issue: "Connection Error: Check your internet connection"**
- Solution: Verify you have an active internet connection
- Check if your firewall is blocking the application

**Issue: Module not found errors**
- Solution: Ensure you've activated the virtual environment and installed dependencies
```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

## 📦 Dependencies

- **PyQt5** (5.15.11) - GUI framework for the application interface
- **requests** (2.32.3) - HTTP library for API calls

## 🔐 API Key Security

> [!WARNING]
> Never commit your API key to version control or share it publicly.

The application prompts for the API key at startup. For future enhancements, consider:
- Storing the API key in a local config file (add to `.gitignore`)
- Using environment variables
- Implementing encrypted storage

## 🚧 Future Enhancements

- [ ] Temperature unit toggle (Celsius/Fahrenheit/Kelvin)
- [ ] 5-day weather forecast
- [ ] Save favorite cities
- [ ] Weather history
- [ ] Dark/Light theme toggle
- [ ] System tray integration
- [ ] Persistent API key storage

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

<p align="center">
  Made with ❤️ using Python & PyQt5 By Aman Kanojiya
</p>
