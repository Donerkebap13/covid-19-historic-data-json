import requests
import json
from datetime import datetime, timedelta
import os
path = (os.path.dirname(os.path.realpath(__file__)))

def add_date():
    with open("{}/dates.json".format(path), "r") as file:
        data = json.load(file)

    data.append(datetime.strftime(datetime.now(), '%m-%d-%Y %H:%M:%S'))

    with open("{}/dates.json".format(path), "w") as file:
        json.dump(data, file)

if __name__ == '__main__':
    add_date()
