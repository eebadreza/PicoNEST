from machine import Pin,UART
uart = UART(0,9600)

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)

while True:
    
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        data=str(data) #Converting bytes to str type
        print(data)
    
        if ('red on' in data):
            led1.value(1)
        elif ('red off' in data):
            led1.value(0)
        elif ('yellow on' in data):
            led2.value(1)
        elif ('yellow off' in data):
            led2.value(0)
        elif ('green on' in data):
            led3.value(1)
        elif ('green off' in data):
            led3.value(0)
