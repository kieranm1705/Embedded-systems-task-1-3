# Embedded-systems-task-1-3
Coursework repository containing code and simulations for SmartSolver, Wokwi lock, and IoT sensor tasks.
This repository contains code and documentation for the Embedded Systems reassessment (Tasks 1–3), completed using Python, MicroPython, and the Wokwi simulation environment. Each task focuses on applying embedded systems concepts through practical implementation.

Task 1 – Smart Word Solver
A Python-based solver designed to guess a hidden 6-letter word using feedback logic similar to Wordle. The solver maintains an average of fewer than 3.5 guesses across a dictionary of 4000+ words. Frequency-based scoring and feedback filtering were used to reduce guesses and improve efficiency.

Files:

solver.py, smart_solver.py, test_solver.py

wordList.txt

Task 2 – Combination Lock Simulation
A digital combination lock simulated using MicroPython on an ESP32, tested via the Wokwi online platform. The system uses button inputs and LED feedback to verify a hardcoded unlock sequence.

Files:

lock.py

Wokwi link and circuit screenshot included in submission

Task 3 – IoT Sensor and GUI
An IoT system that sends sensor data from an ESP32 to a ThingSpeak channel and visualises it using a Python GUI. Sensor values are simulated on Wokwi and updated every 15 seconds, with live data retrieved via API.

Files:

iot_sender.py, thingspeak_gui.py

Wokwi project and ThingSpeak channel link included

