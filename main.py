#Code to be loaded onto Raspberry Pi Pico
import machine
import time
import sys
from machine import Pin, Timer
import select



# Initialize GPIO pin
gpio_pin = Pin(15, Pin.OUT)


#Troubleshooting purposes
led = Pin("LED", Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)


# Setup poll object to read USB port
poll_object = select.poll()
poll_object.register(sys.stdin,select.POLLIN)

try:       
    while True:
    

        events = poll_object.poll(1000)# This will block for 1 second

        if events:  # If there is any event
            data = sys.stdin.readline().strip()
            if len(data) > 0:
                data_value = data.split()
                #print(len(data_value))
                #print(type(data_value))
                if data_value[0] == '1':
                    print('ON')
                    gpio_pin.value(1)
            
                elif data_value[0] == '0':
                    print('OFF')
                    gpio_pin.value(0)
                
        #print('llego aca') 
finally:
    print("Exited out of main loop!")            

