#!/usr/bin/python3

'''
This demo provides a processing script to calculate the energy
for each phase based on the record time stamp.
'''
import numpy as np
import os
import time
from ina219_pi_seelab import ina219_pi_seelab

PWR_FILE = "./ina219_power.txt"
LOG_FILE = "./ina219_log.txt"
MEASURE_TIME = 10
SAMPLE_INTERVAL = 100 # ms
MSG = "Collecting power measurements for {} seconds...\r\n".format(
        MEASURE_TIME)
MSG += "Check {} for detailed traces afterwards.".format(PWR_FILE)

def process():
    '''
    Calculate total and average power based on
    power file and time stamp log file
    '''
    all_pwr = np.loadtxt(PWR_FILE, delimiter=',')
    phase = np.loadtxt(LOG_FILE, delimiter=',')
    i, start_idx, end_idx = 0, 0, 0
    for start, end in phase:
        phase_pwr = []
        while i < len(all_pwr):
            if all_pwr[i][0] == start:
                start_idx = i
                while all_pwr[i][0] != end:
                    phase_pwr.append(all_pwr[i][1])
                    i += 1
                phase_pwr.append(all_pwr[i][1])
                end_idx = i
                print("total energy in phase {}-{} is {}".format(
                    all_pwr[start_idx][0], all_pwr[end_idx][0],
                    sum(phase_pwr)))
                print("average energy in phase {}-{} is {}".format(
                    all_pwr[start_idx][0], all_pwr[end_idx][0],
                    sum(phase_pwr)/len(phase_pwr)))
                print("\n")
                break
            else:
                i += 1

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
    ina_sensor = ina219_pi_seelab(filename=PWR_FILE)
    ina_sensor.run(SAMPLE_INTERVAL, pwr_callback)

    print(MSG)
    time.sleep(MEASURE_TIME)

    ina_sensor.stop()
    
    # select several time intervals and write into log file
    log_file = open(LOG_FILE, "w+")
    i = 0
    while i < len(pwr_callback.pwr_data) - 5:
        phase = "{},{}\n".format(pwr_callback.pwr_data[i][0], 
                pwr_callback.pwr_data[i+5][0])
        log_file.write(phase)
        i = i + 10
    log_file.close()
    
    process()


if __name__ == '__main__':
    main()
