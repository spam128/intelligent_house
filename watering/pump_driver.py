import RPi.GPIO as GPIO
from django.conf import settings

# numbering to use board pin numbering, check pin numbering
# run in terminal pinout
# TODO move to manage.py or apps.py
# if not GPIO.getmode() == BPIO.BOARD:
#    GPIO.setmode(GPIO.BOARD)
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
# GPIO.output(channel, 1)


class PumpDriver:
    channel = settings.WATER_PUMP1_RPI_PIN
    output = GPIO.LOW

    def __init__(self):
        if not GPIO.getmode() == GPIO.BOARD:
            GPIO.setmode(GPIO.BOARD)
        self._pin_off(self.channel)

    def switch(self):
        new_state = GPIO.LOW if self.output == GPIO.HIGH else GPIO.HIGH
        if new_state == GPIO.LOW:
            self._pin_off(self.channel)
        elif new_state == GPIO.HIGH:
            self._pin_on(self.channel)
        else:
            raise AttributeError(
                f"During switching pin, incorrect new state: {new_state}"
            )
        self.output = new_state
        return new_state

    @property
    def state(self):
        return "ON" if self.output == GPIO.HIGH else "OFF"

    def _pin_on(self, pin_number):
        GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.HIGH)

    def _pin_off(self, pin_number):
        GPIO.setup(pin_number, GPIO.IN)
