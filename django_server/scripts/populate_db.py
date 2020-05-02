import requests
from datetime import datetime, timedelta
from random import randint, randrange

url = 'http://localhost:8000/api/visit/'

# simulates 1000 costumers a day for 90 days
for i in range(90):
    for j in range(1000):
        # unique id that does not represent a true UUID
        device_id = randrange(100000,150000)

        # time_in is a random start. Supposed to simulate opening hour
        # also has delta to simulate time between 8AM and 8PM
        time_in = datetime(year=2020,month=1,day=1,hour=8,minute=0) + \
            timedelta(
                days=i,
                hours=randint(0, 11),
                minutes=randint(0, 59)
            )

        # time_out simulates someone staying in a store for maximum of 90 minutes
        time_out = time_in + timedelta(minutes=randint(1,90))

        data = {
            'device_id': device_id,
            'time_in': time_in,
            'time_out': time_out
        }

        resp = requests.post(url=url, data=data)
        print(resp.text)
