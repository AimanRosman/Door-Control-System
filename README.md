# 3 mini project with Raspberry Pi Pico using CircuitPython

# Temperature and Humidity Monitoring
![WhatsApp Image 2024-11-19 at 14 53 16_8bb28bc8](https://github.com/user-attachments/assets/1bd40e2e-4f84-4e8c-8478-6f6daea0d11d)
## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
DHT 11 Temperature and Humidity Sensor <br />
## How it works
The reading of temperature and humidity will be display on oled and if the temperature reach 28 Celcius or humidity reach 58% the buzzer will trigger to alert the user.

# Safe Lock System
## Safe locked
![lock before](https://github.com/user-attachments/assets/512e0dbd-7925-4636-992e-f79976b2ede9)
## Safe violated
![lock after](https://github.com/user-attachments/assets/c9a2965e-9945-4fcd-9a71-5edf5309c378)
## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
Infrared sensor <br />
## How it works
Infrared sensor will be put facing the safe door, whenever the door is opened it will trigger the buzzer and show count how many time the safe had been opened

# Door Control System
![door control](https://github.com/user-attachments/assets/e442b466-8074-44e9-89f9-21f36a09531d)
## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
Ultrasonic sensor <br />
Servo Motor 90 <br />
Push Button <br />
## How it works
Ultrasonic will be place in front of the door, if there is anyone standing within the range it will trigger the buzzer and display on oled someone outside and to open the door you will need to click the push button to trigger the servo motor to open the door and the display will show door opened and close back within 5 second.
