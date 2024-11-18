# Import necessary libraries
import time  # For adding delays
import board  # For accessing board pins
import digitalio  # For controlling digital input/output pins
import busio  # For I2C communication
from adafruit_ssd1306 import SSD1306_I2C  # OLED display library

# Initialize PIR (Passive Infrared) motion sensor
# The PIR sensor detects motion and outputs a HIGH signal when triggered.
pir_sensor = digitalio.DigitalInOut(board.GP2)
pir_sensor.direction = digitalio.Direction.INPUT  # Set PIR sensor as an input

# Initialize the buzzer
# The buzzer provides an alert sound when motion is detected.
buzzer = digitalio.DigitalInOut(board.GP3)
buzzer.direction = digitalio.Direction.OUTPUT  # Set buzzer as an output

# Initialize the OLED display
# The display uses I2C communication to show messages about the system status.
i2c = busio.I2C(board.GP1, board.GP0)  # Set SCL and SDA pins for I2C
display = SSD1306_I2C(128, 32, i2c)    # Set up 128x32 pixel OLED display

# Your name or system label for display
name = "Aiman's Safe Lock"  # Displayed at the top of the OLED

# Initialize motion counter
# Counts the number of times motion has been detected, acting as a log of detections.
motion_counter = 0

# Variable to track ongoing motion detection bursts
# Ensures that multiple detections during a single burst are counted as one.
motion_detected = False

# Main loop to continuously monitor for motion and update the display and buzzer
while True:
    try:
        display.fill(0)  # Clear display for fresh updates
        
        # Display the system name or identifier at the top of the OLED
        display.text(name, 0, 0, 1)

        # Check if the PIR sensor detects motion
        if pir_sensor.value:  # Motion detected (PIR sensor output HIGH)
            if not motion_detected:  # Only trigger on the first detection in a burst
                print("Motion Detected!")  # Log the detection in terminal
                motion_detected = True   # Set flag to track motion burst
                motion_counter += 1      # Increment the motion counter

            # Display motion detection messages on the OLED
            display.text("Door Open!", 0, 10, 1)
            display.text("Don't touch my safe", 0, 20, 1)
            display.show()  # Update OLED display with new messages

            # Buzzer beeps continuously while motion is detected
            buzzer.value = True  # Turn on buzzer
            time.sleep(0.2)      # Short delay to create a beep effect
            buzzer.value = False # Turn off buzzer briefly
            time.sleep(0.2)      # Short delay before next beep

        else:
            if motion_detected:  # Reset if motion is no longer detected
                print("No Motion Detected")  # Log to terminal
                motion_detected = False  # Clear flag to allow new detections

            # Display messages for no motion detected, showing door closed and counter
            display.text("Door Closed", 0, 10, 1)
            display.text("Opened: {}".format(motion_counter), 0, 20, 1)  # Display counter
            display.show()  # Update OLED display with current status

    # Error handling in case of issues with the PIR sensor
    except RuntimeError as e:
        print("Error reading PIR sensor: {}".format(e.args))  # Log error to terminal
        display.fill(0)  # Clear display
        display.text("Error: {}".format(e.args[0]), 0, 0, 1)  # Show error message on OLED
        display.show()  # Update display with error message

    # Small delay to avoid overloading the loop and allow time for changes
    time.sleep(0.1)

