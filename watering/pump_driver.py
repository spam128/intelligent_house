import RPi.GPIO as GPIO

# numbering to use board pin numbering, check pin numbering 
# run in terminal pinout
# TODO move to manage.py or apps.py
#if not GPIO.getmode() == BPIO.BOARD:
#    GPIO.setmode(GPIO.BOARD)
#GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)
# GPIO.output(channel, 1)

class PumpDriver:
    channel=26
    output=GPIO.LOW

    def __init__(self):
        if not GPIO.getmode() == GPIO.BOARD:
            GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.channel, GPIO.OUT, initial=self.output)
    
    def switch(self):
        new_state = GPIO.LOW if self.output == GPIO.HIGH else GPIO.HIGH
        GPIO.output(self.channel, new_state)
        self.output = new_state
        return new_state

    @property
    def state(self):
        return 'ON' if self.output == GPIO.HIGH else 'OFF' 
