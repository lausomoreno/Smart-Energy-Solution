import time
from pynput import mouse, keyboard
import psutil
import serial
timeout_s = 600 #in seconds
monitoring = True
last_activity_time = time.time()
application_name_ = 'StartTest.exe'



# Set up the serial connection
ser = serial.Serial('COM31', 9600)  #change port number as you see fit 
str0 = "0\n"
str1 = "1\n"


#Action to be triggered every time a mouse or keyboard activity is detected
def mouse_move(x,y):
    globals()["last_activity_time"] = time.time()
    #Action to be triggered every time a mouse or keyboard activity is detected
def mouse_click(x,y,button,pressed):
    globals()["last_activity_time"] = time.time()

#Action to be triggered every time a mouse or keyboard activity is detected
def keyboard_press(key):
    globals()["last_activity_time"] = time.time()

#Action to be triggered every time a mouse or keyboard activity is detected
def keyboard_release(key):
    globals()["last_activity_time"] = time.time()
# Simulate turning equipment on or off
def turn_equipment_on():
    print("Equipment turned ON")
    ser.write(str0.encode('utf-8'))
    #print(type(str0))
    #print(type(encoded_str0))

def turn_equipment_off():
    print("Equipment turned OFF")
    ser.write(str1.encode('utf-8'))


#Check if application is running
def is_application_running(application_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == application_name:
            return True
    return False


def start_monitoring(monitoring, timeout):
       mouse_listener = mouse.Listener(on_move=mouse_move,on_click=mouse_click)
       keyboard_listener = keyboard.Listener(on_press = keyboard_press, on_release = keyboard_release) 
       with mouse_listener as m_listener, keyboard_listener as k_listener:
            while monitoring:
                current_time = time.time()
                if (current_time - globals()["last_activity_time"] > timeout) and (is_application_running(application_name_) == False):
                    turn_equipment_off()
                else:
                    turn_equipment_on()
                time.sleep(1)



if __name__ == "__main__":
   
    start_monitoring(monitoring, timeout_s)










 
