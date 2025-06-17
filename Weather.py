#created by prince jha
#message on telegrram @prince_jha_04

import os
import sys
import requests
from dotenv import load_dotenv
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt


load_dotenv()
api_key = os.getenv("API_KEY")

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(400,400,700,500)

        self.city_label=QLabel("Weather App 😍",self) #setting up the labels
        self.city_input=QLineEdit('',self)
        self.city_input.setPlaceholderText("Enter The City Name")
        self.get_weather_button=QPushButton("Get Weather",self)
        self.result_label=QLabel('',self)

        self.AppUI()

    def AppUI(self):
        self.layout=QVBoxLayout()  #designing the layout

        self.layout.addWidget(self.city_label, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.get_weather_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
        self.SetStyle()
        
        #get weather function will be called when the button is clicked
        self.get_weather_button.clicked.connect(self.get_weather) 

    def SetStyle(self):  #designing using the CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLineEdit {
                padding: 6px;
                border: 2px solid #0078D7;
                border-radius: 9px;
                font-weight: bold;
                font-size: 20px;
            }

            QPushButton {
                background-color: #0078D7;
                color: white;
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #005bb5;
            }

            QLabel {
                color: #333;
                font-size: 50px;
                font-weight: bold;
            }
        """)

    def get_weather(self):

        city=self.city_input.text()

        if not city:
            self.result_label.setText("Please enter a city name.")
            return
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


        response=requests.get(url) #fetching data through api call
        data=response.json()
            
        if response.status_code==200:
            Weather=data['weather'][0]['main']
            temperature=data['main']['temp']
            description=data['weather'][0]['description']
            windspeed=data['wind']['speed']

            self.result_label.setText(f"""weather: {Weather}
Temperature: {temperature}°C
Description: {description}
Wind Speed: {windspeed}""")
            
        else:
            self.result_label.setText("City not Found")
                
                
if __name__=="__main__":
    app=QApplication(sys.argv)
    Weather=WeatherApp()
    Weather.show()
    sys.exit(app.exec_())