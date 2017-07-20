# to jest moja proba odczytania danych z gpio

import time
import RPi.GPIO as GPIO

pin = 15

# ustawienie trybu w jaki sposob maja byc interpretowane oznaczenia pinow
GPIO.setmode(GPIO.BCM)

# ustawienie pinu jako OUT
GPIO.setup(pin, GPIO.OUT)

# tzw pull off?
# wyslanie sygnalu inicjalizujacego jako high (1)
# i wstrzymanie na pol sekundy
# send initial high
GPIO.output(pin, GPIO.HIGH)
time.sleep(0.05)

# pull down to low
GPIO.output(pin, GPIO.LOW)
time.sleep(0.02)

# ustawienie pinu jako wejscie
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)


def collect_input(pin):
    # collect the data while unchanged found
    unchanged_count = 0

    # this is used to determine where is the end of the data
    max_unchanged_count = 100

    last = -1
    data = []
    while True:
        current = GPIO.input(pin)
        data.append(current)
        if last != current:
            unchanged_count = 0
            last = current
        else:
            unchanged_count += 1
            if unchanged_count > max_unchanged_count:
                break
    print data
    return data

collect_input(pin)
