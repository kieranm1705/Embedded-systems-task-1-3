import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")
from machine import Pin, PWM
from time import sleep

# Lock configuration
PASSWORD = "22591208"  
input_code = ""

# Servo setup
servo = PWM(Pin(15))
servo.freq(50)

def set_locked():
    servo.duty_u16(2000)  # Horizontal (locked)
    print("🔒 LOCKED")

def set_unlocked():
    servo.duty_u16(8000)  # Vertical (unlocked)
    print("🔓 UNLOCKED")

# Keypad matrix
keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

rows = [Pin(pin, Pin.OUT) for pin in [2, 3, 4, 5]]
cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in [6, 7, 8, 9]]

def read_keypad():
    for i, row in enumerate(rows):
        row.high()
        for j, col in enumerate(cols):
            if col.value() == 1:
                row.low()
                return keys[i][j]
        row.low()
    return None

# Initial lock state
set_locked()

while True:
    key = read_keypad()
    if key:
        print(f"Pressed: {key}")
        if key == "*":
            set_locked()
            input_code = ""
        elif key == "#":
            if input_code == PASSWORD:
                set_unlocked()
            else:
                print("❌ WRONG CODE")
            input_code = ""
        else:
            input_code += key
        sleep(0.3)
