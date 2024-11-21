# 3 mini project with Raspberry Pi Pico using CircuitPython

# Raspberry Pi Pico W
![Raspberry_pi_pico_w_pinout-1-1536x864](https://github.com/user-attachments/assets/ecf73dbf-0255-44af-b6a5-df3b1ac57800)

# Temperature and Humidity Monitoring
![WhatsApp Image 2024-11-19 at 14 53 16_8bb28bc8](https://github.com/user-attachments/assets/1bd40e2e-4f84-4e8c-8478-6f6daea0d11d)

## Diagram
![image](https://github.com/user-attachments/assets/f6d01ea4-e9c1-41b9-8faa-11be9143ea10)

## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
DHT 11 Temperature and Humidity Sensor <br />
## How it works
The reading of temperature and humidity will be display on oled and if the temperature reach 28 Celcius or humidity reach 58% the buzzer will trigger to alert the user.

# Safe Lock System
## Safe locked
![lock after](https://github.com/user-attachments/assets/c9a2965e-9945-4fcd-9a71-5edf5309c378)
## Safe violated
![lock before](https://github.com/user-attachments/assets/512e0dbd-7925-4636-992e-f79976b2ede9)

## Diagram
![image](https://github.com/user-attachments/assets/960f4449-8ac0-4d33-8de8-437ceb0b992e)

## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
Infrared sensor <br />
## How it works
Infrared sensor will be put facing the safe door, whenever the door is opened it will trigger the buzzer and show count how many time the safe had been opened

# Door Control System
![door control](https://github.com/user-attachments/assets/e442b466-8074-44e9-89f9-21f36a09531d)

## Diagram
![image](https://github.com/user-attachments/assets/9cf77b1f-dbc7-4380-ae88-7b5ad4020c2c)

## Components
Raspberry Pi Pico <br />
Oled 128x32 <br />
Buzzer <br />
Ultrasonic sensor <br />
Servo Motor 90 <br />
Push Button <br />
## How it works
Ultrasonic will be place in front of the door, if there is anyone standing within the range it will trigger the buzzer and display on oled someone outside and to open the door you will need to click the push button to trigger the servo motor to open the door and the display will show door opened and close back within 5 second.
