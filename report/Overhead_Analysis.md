# Overhead Analysis

Report on the overhead analysis when reading power consumption from Raspberry Pi with INA219 sensor.

## Motivation

When we use a Raspberry Pi to run a thread, and, at the same time, use INA219 sensor to measure the power consumption, the thread that runs the measurement may interfere the accuracy of the power reading. So we design an experiment to measure the overhead of power consumption.

## Experiment Design

- Set up Python environment on two Raspberry Pi's.
- Install ina219-pi-seelab module on one of the Pi's (measuring Pi) and connect the pins of a Adafruit INA219 sensor to the corresponding pins on the measureing Pi. Connect to power of the INA219 sensor to the power supply of the other Pi (target Pi).
- Install RPi.GPIO on both Pi's.
- Connect two Pi's with a wire on GPIO pins.
- Connect the ground pins of two Pi's.
- Set the connected pin on the measuring Pi as INPUT and set the pin on the target Pi as OUTPUT.
- Run a simple python program on the target Pi.
- Use the measuring Pi to read the power data with demo_animation.py and demo_process.py, store the image of power reading and calculate the average power consumption on a certain time interval.
- Now disconnect two Pi's and connect the INA219 sensor on the measuring Pi.
- Run the same python program on measuring Pi and use demo_animation.py and demo_process.py to store the image of power reading and calculate the average power consumption on the same time interval.

## Results and Analysis

Here is the power reading when running the demo code on a target Pi and measuring the power from another Pi:

```
!(/Images/target_pi_figure.png)
```

the average power consumption from 1500ms to 3500ms is around: 887

And here is the power reading when running the demo code and measuring the power on the same Pi:

```
!(/Images/same_pi_figure.png)
```

the average power consumption from 1500ms to 3500ms is around: 863

So average power consumption is not significantly different whethor or not we run the code and measure on the same Pi. But from the figure we can see that when we use the same Pi to both run a thread and do the power measurement, the fluctuation is larger (800W - 1000W) than the fluctuation of power when we run a thread and do the measurement on different Pi. 