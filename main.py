# Import necessary libraries for hardware control and timing
import time  # For adding delays
import board  # For accessing board pins
import digitalio  # For controlling digital input/output pins
import busio  # For I2C communication
from adafruit_ssd1306 import SSD1306_I2C
import adafruit_hcsr04  # Library for the ultrasonic sensor
from adafruit_motor import servo  # Library for controlling servo motor
import pwmio

# Setup for the ultrasonic sensor:
# The ultrasonic sensor is used to detect objects by measuring distance.
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP21, echo_pin=board.GP20)

# Setup for the OLED display:
# The I2C communication protocol is used to communicate with the OLED.
i2c = busio.I2C(board.GP1, board.GP0)  # SCL and SDA pins
oled = SSD1306_I2C(128, 32, i2c)       # 128x32 OLED display

# Setup for the servo motor:
# The PWM (Pulse Width Modulation) signal controls the servo motor's position.
pwm_servo = pwmio.PWMOut(board.GP4, frequency=50)  # PWM frequency set to 50Hz
door_servo = servo.Servo(pwm_servo)  # Create servo object

# Setup for the buzzer:
# The buzzer provides audio alerts and is controlled as a digital output.
buzzer = digitalio.DigitalInOut(board.GP3)  # Buzzer connected to GP3
buzzer.direction = digitalio.Direction.OUTPUT

# Setup for the push button:
# The button triggers door opening from the inside.
button = digitalio.DigitalInOut(board.GP2)  # Button connected to GP2
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Sets the button to be "pulled up" (default state is HIGH)

# Door operation thresholds:
# These constants define the distances for opening and closing the door.
OPEN_DISTANCE = 10.0  # Distance in cm to trigger the door to open
CLOSE_DISTANCE = 30.0  # Distance in cm to trigger the door to close

# Function to display messages on the OLED:
# This function takes a text message as input, clears the OLED screen, 
# displays the message, and then shows it on the OLED display.
def display_message(message):
    oled.fill(0)  # Clear the display
    oled.text(message, 0, 10, 1)  # Display message at coordinates (x=0, y=10)
    oled.show()  # Show the message on the OLED screen

# Main loop to monitor the ultrasonic sensor and control the door
while True:
    try:
        # Measure the distance from the ultrasonic sensor
        distance = sonar.distance  # Returns distance in cm
        print("Distance: {:.2f} cm".format(distance))  # Print distance to the terminal for monitoring
        
        # Detect if someone is outside the room based on distance
        if distance < OPEN_DISTANCE:
            display_message("Person Outside!")  # Display warning on OLED
            print("Person Outside!")  # Print message in terminal
            
            # Beep the buzzer continuously as long as someone is detected outside
            buzzer.value = True  # Turn on the buzzer
            time.sleep(0.5)      # Keep buzzer on for 0.5 seconds
            buzzer.value = False  # Turn off the buzzer
            time.sleep(0.5)      # Buzzer remains off for 0.5 seconds (creates a beeping effect)
        else:
            # Turn off the buzzer if no one is outside the monitored range
            buzzer.value = False

        # Check if the button is pressed to open the door
        if not button.value:  # When the button is pressed, value will be LOW (0)
            display_message("Button Pressed")  # Show "Button Pressed" on OLED
            time.sleep(0.1)  # Short delay for button debounce
            
            # Open the door
            door_servo.angle = 90  # Set servo angle to 90 degrees (door open position)
            display_message("Door Open")  # Display "Door Open" message on OLED
            print("Door Open")  # Print "Door Open" in terminal
            time.sleep(2)  # Door remains open for 2 seconds
            
            # Close the door
            door_servo.angle = 0  # Set servo angle to 0 degrees (door closed position)
            display_message("Door Closed")  # Show "Door Closed" on OLED
            print("Door Closed")  # Print "Door Closed" in terminal

        time.sleep(0.1)  # Delay to avoid excessive sensor reads and button presses

    except RuntimeError as e:
        # Handle any sensor reading errors and show an error message
        print("Error in reading sensor: {}".format(e))  # Print error to terminal
        display_message("Sensor Error")  # Display "Sensor Error" on OLED
        time.sleep(1)  # Delay before retrying the main loop

