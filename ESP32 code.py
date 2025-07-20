import network
import urequests
from machine import ADC, Pin, PWM
from time import sleep

# Wi-Fi credentials (Wokwi auto-connects with these)
SSID = "Wokwi-GUEST"
PASSWORD = ""

# ThingSpeak API config
API_KEY = "W5PIAF7JEPOHXK1L"  # Your write key
CHANNEL_ID = "3000578"

# Sensor setup (Potentiometer on GP26 = ADC0)
sensor = ADC(Pin(26))

# LED setup (Connected to GP14)
led = Pin(14, Pin.OUT)

# Wi-Fi connection function
def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        sleep(1)
    print("✅ Connected to WiFi:", wlan.ifconfig())

# Connect to Wi-Fi
connect()

# Upload loop
while True:
    value = sensor.read_u16() // 256  # Scale from 0–65535 to 0–255
    print("Sensor Reading:", value)

    # LED turns on if value > 150
    if value > 150:
        led.on()
        print("💡 LED ON")
    else:
        led.off()
        print("💡 LED OFF")

    # Send data to ThingSpeak
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={value}"
    response = urequests.get(url)
    print("📡 ThingSpeak Response:", response.text)
    response.close()

    sleep(20)  # Respect ThingSpeak's rate limit (15s min)
