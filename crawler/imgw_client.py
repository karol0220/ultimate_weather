import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ultimate_weather.settings")
import django
django.setup()
import logging
from datetime import datetime
from ultimate_weather_site.models import Temperatures, Service
import requests
import json

def get_temperature():
    url = 'https://danepubliczne.imgw.pl/api/data/synop/station/warszawa'

    warsaw_data = json.loads(requests.get(url).text)

    #warsaw_data = next((x for x in data if x['stacja'] == 'Warszawa'), None)
    if warsaw_data:

        service = Service.objects.get(name='actual')
        date = datetime.strptime(warsaw_data['data_pomiaru'], '%Y-%m-%d')
        hour = warsaw_data['godzina_pomiaru']
        if len(hour) == 1:
            hour = '0' + hour
        temp = int(float(warsaw_data['temperatura']))
        logging.info('GOT ' + str(temp) + ' AT HOUR: ' + str(hour))

        temps = Temperatures.objects.filter(date=date, service_id=service.pk).first()
        if temps:
            value_for_current_hour = getattr(temps, 'h_'+hour)
            if not value_for_current_hour:
                setattr(temps, 'h_'+hour, temp)
                temps.save()
                logging.info('SAVED TEMP')

        else:
            temps = Temperatures()
            temps.service_id = service
            temps.date = date
            setattr(temps, 'h_'+hour, temp)
            temps.save()
            logging.info('SAVED TEMP')
