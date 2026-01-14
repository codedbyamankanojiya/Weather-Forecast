import sys
import os
import json
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                                                       QLineEdit, QPushButton, QVBoxLayout, QInputDialog, QMessageBox)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = None
        self.temp_unit = 'F'  # Default to Fahrenheit
        self.current_temp_k = None  # Store temperature in Kelvin
        self.current_feels_like_k = None  # Store feels like temperature
        self.current_city = ""  # Store current city name
        
        # UI Components
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText("e.g., London, Tokyo, Mumbai")
        self.get_weather_button = QPushButton("Get Weather", self)
        self.unit_toggle_button = QPushButton("Switch to °C", self)
        
        # Weather display labels
        self.city_name_label = QLabel(self)
        self.temperature_label = QLabel(self)
        self.feels_like_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.humidity_label = QLabel(self)
        self.wind_label = QLabel(self)
        
        self.initUI()
        self.load_config()

    def load_config(self):
        """Load API key from config.json or prompt user if not found."""
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        
        # Try to load from config file
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    self.api_key = config.get('api_key', '')
                    if self.api_key and self.api_key != 'your_openweathermap_api_key_here':
                        return  # Successfully loaded API key
            except (json.JSONDecodeError, IOError):
                pass  # Fall through to prompt
        
        # Prompt for API key if not found in config
        self.prompt_api_key()
    
    def prompt_api_key(self):
        """Prompt user for API key and optionally save it."""
        api_key, ok = QInputDialog.getText(self, "API Key Required", 
                                           "Enter your OpenWeatherMap API Key:")
        if ok and api_key:
            self.api_key = api_key
            
            # Ask if user wants to save the API key
            reply = QMessageBox.question(self, 'Save API Key',
                                        'Would you like to save this API key for future use?',
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self.save_config()
        else:
            QMessageBox.critical(self, "API Key Missing", 
                               "You must enter a valid API key to use this app.")
            sys.exit(1)
    
    def save_config(self):
        """Save API key to config.json file."""
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        config = {
            'api_key': self.api_key,
            'default_unit': 'fahrenheit'
        }
        
        try:
            with open(config_path, 'w') as f:
                json.dump(config, f, indent=2)
            QMessageBox.information(self, "Success", 
                                  "API key saved successfully!")
        except IOError as e:
            QMessageBox.warning(self, "Save Failed", 
                              f"Could not save API key: {e}")

    def initUI(self):
        self.setWindowTitle("🌤️ Weather App")
        self.setMinimumSize(550, 750)

        vbox = QVBoxLayout()
        vbox.setSpacing(12)
        vbox.setContentsMargins(30, 30, 30, 30)

        # Input section
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.unit_toggle_button)
        
        # Weather display section
        vbox.addSpacing(10)
        vbox.addWidget(self.city_name_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.feels_like_label)
        vbox.addWidget(self.description_label)
        vbox.addSpacing(10)
        vbox.addWidget(self.humidity_label)
        vbox.addWidget(self.wind_label)
        vbox.addStretch()

        self.setLayout(vbox)

        # Set alignments
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_name_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.feels_like_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.wind_label.setAlignment(Qt.AlignCenter)

        # Set object names for styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.city_name_label.setObjectName("city_name_label")
        self.temperature_label.setObjectName("temperature_label")
        self.feels_like_label.setObjectName("feels_like_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.humidity_label.setObjectName("humidity_label")
        self.wind_label.setObjectName("wind_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI', calibri, sans-serif;
            }
            QLabel#city_label{
                font-size: 32px;
                font-weight: 600;
                color: #2d3748;
                margin-bottom: 10px;
            }
            QLineEdit#city_input{
                font-size: 28px;
                padding: 12px;
                border: 2px solid #cbd5e0;
                border-radius: 8px;
                background-color: white;
                color: #2d3748;
            }
            QLineEdit#city_input:focus{
                border: 2px solid #4299e1;
            }
            QPushButton#get_weather_button{
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
                background-color: #4299e1;
                color: white;
                border: none;
                border-radius: 8px;
                margin-top: 10px;
            }
            QPushButton#get_weather_button:hover{
                background-color: #3182ce;
            }
            QPushButton#get_weather_button:pressed{
                background-color: #2c5282;
            }
            QPushButton#unit_toggle_button{
                font-size: 18px;
                padding: 10px;
                background-color: #48bb78;
                color: white;
                border: none;
                border-radius: 6px;
                margin-top: 5px;
            }
            QPushButton#unit_toggle_button:hover{
                background-color: #38a169;
            }
            QLabel#temperature_label{
                font-size: 72px;
                font-weight: bold;
                color: #2d3748;
                margin-top: 20px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: 'Segoe UI Emoji', 'Apple Color Emoji', sans-serif;
            }
            QLabel#city_name_label{
                font-size: 28px;
                font-weight: 600;
                color: #2b6cb0;
                margin-top: 15px;
                margin-bottom: 5px;
            }
            QLabel#description_label{
                font-size: 28px;
                color: #4a5568;
                text-transform: capitalize;
                margin-bottom: 10px;
            }
            QLabel#feels_like_label{
                font-size: 20px;
                color: #718096;
                margin-top: 5px;
            }
            QLabel#humidity_label, QLabel#wind_label{
                font-size: 22px;
                color: #4a5568;
                padding: 8px;
                background-color: rgba(255, 255, 255, 0.6);
                border-radius: 6px;
                margin: 3px;
            }
        """)

        # Connect signals
        self.get_weather_button.clicked.connect(self.get_weather)
        self.unit_toggle_button.clicked.connect(self.toggle_temperature_unit)
        self.city_input.returnPressed.connect(self.get_weather)  # Enter key to search
        
        # Hide elements until weather is fetched
        self.unit_toggle_button.hide()
        self.city_name_label.hide()
        self.feels_like_label.hide()
        self.humidity_label.hide()
        self.wind_label.hide()

    def get_weather(self):
        if not self.api_key:
            self.display_error("API key is missing.")
            return
        city = self.city_input.text().strip()
        if not city:
            self.display_error("Please enter a city name.")
            return
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px; color: #e53e3e;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.unit_toggle_button.hide()
        self.city_name_label.hide()
        self.feels_like_label.hide()
        self.humidity_label.hide()
        self.wind_label.hide()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 72px; font-weight: bold; color: #2d3748; margin-top: 20px;")
        
        # Extract weather data
        self.current_temp_k = data["main"]["temp"]
        self.current_feels_like_k = data["main"]["feels_like"]
        self.current_city = data["name"]
        country = data["sys"]["country"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]  # in m/s
        
        # Display city name
        self.city_name_label.setText(f"{self.current_city}, {country}")
        self.city_name_label.show()
        
        # Display main weather info
        self.update_temperature_display()
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)
        
        # Display additional info
        self.humidity_label.setText(f"💧 Humidity: {humidity}%")
        self.humidity_label.show()
        
        # Convert wind speed from m/s to km/h
        wind_kmh = wind_speed * 3.6
        self.wind_label.setText(f"💨 Wind: {wind_kmh:.1f} km/h")
        self.wind_label.show()
        
        # Show toggle button
        self.unit_toggle_button.show()
    
    def update_temperature_display(self):
        """Update temperature display based on current unit."""
        if self.current_temp_k is None:
            return
        
        if self.temp_unit == 'F':
            temp = (self.current_temp_k * 9/5) - 459.67
            feels_like = (self.current_feels_like_k * 9/5) - 459.67
            self.temperature_label.setText(f"{temp:.0f}°F")
            self.feels_like_label.setText(f"Feels like {feels_like:.0f}°F")
        else:  # Celsius
            temp = self.current_temp_k - 273.15
            feels_like = self.current_feels_like_k - 273.15
            self.temperature_label.setText(f"{temp:.0f}°C")
            self.feels_like_label.setText(f"Feels like {feels_like:.0f}°C")
        
        self.feels_like_label.show()
    
    def toggle_temperature_unit(self):
        """Toggle between Fahrenheit and Celsius."""
        if self.temp_unit == 'F':
            self.temp_unit = 'C'
            self.unit_toggle_button.setText("Switch to °F")
        else:
            self.temp_unit = 'F'
            self.unit_toggle_button.setText("Switch to °C")
        
        self.update_temperature_display()

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
