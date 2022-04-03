import sys
from PyQt5.QtWidgets import *
from py_gtk_app.app import start_gtk_app
from py_qt_app.functions import *


class Screen(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.create_menu()
        
    def show_current_weather(self, temp, min_temp, max_temp, feels_like, main_weather, 
        weather_description, clouds, wind_speed, pressure, humidity):
        main_info = QLabel()
        main_info.setText(f"Aktualna pogoda dla miasta {get_city_from_file().upper()}:\n\n"
            f"Ogólne warunki: {main_weather} ({weather_description})\n\n"
            f"Zachmurzenie wynosi {clouds}%\n"
            f"Aktualna temperatura wynosi {temp}\u00b0C (odczuwalne {feels_like}\u00b0C)\n"
            f"Temperatura waha się od {min_temp}\u00b0C do {max_temp}\u00b0C\n"
            f"Wiatr osiąga prędkość {wind_speed}m/s ({convert_wind_speed(wind_speed)}km/h)\n"
            f"Ciśnienie jest równe {pressure} hPa\n"
            f"Wilgotność powietrza wynosi {humidity}%\n")
        self.layout.addWidget(main_info)

    def weather_trigger(self, q):
        temp, min_temp, max_temp, feels_like, main_weather, \
            weather_description, clouds, wind_speed, pressure, \
            humidity = get_weather_trigger(q)
        self.show_current_weather(temp, min_temp, max_temp,
            feels_like, main_weather, weather_description, 
            clouds, wind_speed, pressure, humidity)
    
    def create_menu(self):
        menu_bar = QMenuBar()
        self.layout.addWidget(menu_bar, 0, 0)
        
        # First button in menu
        weather = menu_bar.addMenu("Pogoda")
        action_current_weather = QAction("Aktualna pogoda", self)
        weather.addAction(action_current_weather)
        action_future_weather = QAction("Pogoda na 3 dni", self)
        weather.addAction(action_future_weather)
        weather.triggered[QAction].connect(self.weather_trigger)

        # Second button in menu
        change_city = menu_bar.addMenu("Zmień miasto")
        action_change_city = QAction("Podaj nazwę miasta", self)
        change_city.addAction(action_change_city)
        change_city.triggered[QAction].connect(start_gtk_app)

        # Third button in menu
        about_app = menu_bar.addMenu("O aplikacji")
        action_about_app = QAction("O twórcy", self)
        about_app.addAction(action_about_app)
        action_about_api = QAction("Więcej o OpenWeatherMap", self)
        about_app.addAction(action_about_api)
        about_app.triggered[QAction].connect(about_app_trigger)

        
def start_app():     
    app = QApplication(sys.argv)
    screen = Screen()
    screen.resize(450, 300)
    screen.show()
    sys.exit(app.exec_())
