import matplotlib
matplotlib.use('GTK3Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self, weather_list, city):
        super().__init__(title=f"Godzinna prognoza pogody dla {city}")
        self.weather_list = weather_list
        self.city = city

    def create_plot(self):
        # Temperature
        fig, ax = plt.subplots()
        ax.bar(self.get_hours(), self.get_temps())
        plt.xticks(rotation=45)

        plt.xlabel("Godziny")
        plt.ylabel("Temperatura [\u00b0C]")

        for i in range(len(self.get_hours())):
            plt.text(i, self.get_temps()[i]+0.05, self.get_temps()[i], ha = 'center')

        canvas = FigureCanvas(fig) 
        canvas.set_size_request(600, 400)
        self.add(canvas)

    def get_hours(self):
        return [obj.hour for obj in self.weather_list]
    
    def get_times(self):
        return [obj.time for obj in self.weather_list]
    
    def get_temps(self):
        return [float(obj.temp) for obj in self.weather_list]


def start_gtk_app(hourly_weather_list, city):
    win = MyWindow(hourly_weather_list, city)
    win.create_plot()
    win.connect("delete-event", Gtk.main_quit)
    win.set_default_size(600, 450)
    win.show_all()
    Gtk.main()
