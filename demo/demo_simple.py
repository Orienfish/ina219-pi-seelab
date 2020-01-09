#!/usr/bin/python

'''
A simple power reading demo for ina219-pi-seelab
'''
import os
import time

from ina219-pi-seelab import ina219_pi_seelab

PWR_FILE = "./ina219-power.txt"
MEASURE_TIME = 10
MSG = "Collecting power measurements for {} seconds...\r\n".format(
        MEASURE_TIME)
MSG += "Check {} for detailed traces afterwards.".format(PWR_FILE)

def pwr_callback(pwr_data):
    '''
    Callback function that reads power from module.
    This function is responsible for recording time stamps
    that receive the power measurements.
    Args:
        pwr_data : [time stamp (s), power (W)]
    Attributes:
        pwr_callback.start_time (float): the time that first data comes in, seconds
        pwr_callback.pwr_data: A list of [time stamp (s), power (W)]
    '''
    if pwr_callback.start_time is None:
        pwr_callback.start_time = time.time() * 1000 # in ms

    pwr_callback.pwr_data.append(pwr_data)

pwr_callback.pwr_data = []
pwr_callback.start_time = None

def main():
    '''
    main function
    Start measurement for 10s, save traces to PWR_FILE,
    and return all power values in pwr_callback.pwr_data.
    '''
    ina_sensor = ina219_pi_seelab(PWR_FILE)
    ina_sensor.run(pwr_callback)

    print(MSG)
    time.sleep(MEASURE_TIME)

    ina_sensor.stop()

    for p in pwr_callback.pwr_data:
        print(p)

if __name__ == '__main__':
    main()
