# Import necessary libraries
import time  # For adding delays
import adafruit_dht  # For DHT11 temperature and humidity sensor
import board  # For accessing board pins
import digitalio  # For controlling digital input/output pins
import busio  # For I2C communication
from adafruit_ssd1306 import SSD1306_I2C  # OLED display library

# Initialize DHT11 sensor
# The DHT11 sensor measures temperature and humidity and is connected to pin GP2.
dht = adafruit_dht.DHT11(board.GP2)

# Initialize the buzzer
# The buzzer provides an alert sound if temperature or humidity exceeds thresholds.
buzzer = digitalio.DigitalInOut(board.GP3)
buzzer.direction = digitalio.Direction.OUTPUT  # Set buzzer as an output

# Initialize the OLED display
# The display uses I2C communication to show temperature, humidity, and other messages.
i2c = busio.I2C(board.GP1, board.GP0)  # Set SCL and SDA pins for I2C
display = SSD1306_I2C(128, 32, i2c)    # Set up 128x32 pixel OLED display

# Temperature and humidity thresholds
# These values set the point at which the buzzer should be activated.
TEMP_THRESHOLD = 27.0  # Temperature threshold in Celsius
HUMIDITY_THRESHOLD = 48  # Humidity threshold in percent

# Your name or room label for display
name = "Aiman's Bedroom"  # Displayed at the top of the OLED

# Main loop to continuously monitor temperature and humidity
while True:
    try:
        # Read temperature and humidity from DHT11 sensor
        temperature = dht.temperature  # Get temperature in Celsius
        humidity = dht.humidity  # Get humidity in percent

        display.fill(0)  # Clear display for fresh updates
        
        # Display the name or room label at the top of the OLED
        display.text(name, 0, 0, 1)

        if temperature is not None and humidity is not None:
            # Display temperature and humidity values
            print("Temperature: {:.1f} C \t Humidity: {}%".format(temperature, humidity))  # Log values

            display.text("Temperature: {:.1f} C".format(temperature), 0, 10, 1)  # Temperature on OLED
            display.text("Humidity: {}%".format(humidity), 0, 20, 1)       # Humidity on OLED
            display.show()  # Update OLED display with the latest values

            # Activate buzzer if thresholds are exceeded
            if temperature > TEMP_THRESHOLD or humidity > HUMIDITY_THRESHOLD:
                buzzer.value = True  # Turn on the buzzer
                time.sleep(0.5)      # Short delay for buzzer alert
                buzzer.value = False # Turn off the buzzer

        else:
            # If sensor data fails, display error message on OLED
            print("Failed to read sensor data.")  # Log the issue
            display.text("Error: No data", 0, 10, 1)  # Error message on OLED
            display.show()  # Update OLED display with error message

    # Error handling for sensor read issues
    except RuntimeError as e:
        print("Error reading DHT sensor: {}".format(e.args))  # Log error
        display.fill(0)  # Clear display for error message
        display.text("Error: {}".format(e.args[0]), 0, 0, 1)  # Display error message on OLED
        display.show()  # Update display with error message

    # Small delay before the next loop iteration
    time.sleep(1)

