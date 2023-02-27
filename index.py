from plyer import notification
import psutil
import time

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent


    notification.notify (
        title = "Pourcentage de la batterie",
        message = str(percent) + "% de batterie restant",
        app_icon = "Power.ico",
        timeout = 20,
        app_name="Pourcentage"
    )
    #répéter l'action toutes les heures
    time.sleep(10*60)
    continue