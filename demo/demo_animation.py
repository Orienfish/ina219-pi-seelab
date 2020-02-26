#!/usr/bin/python2

'''
An animation demo that will display the readings in real time
'''
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import os
import time
from ina219_pi_seelab import ina219_pi_seelab

SAMPLE_INTERVAL = 0 # continuous sampling
MEASURE_TIME = 1
PWR_FILE = "./ina219_power.txt"
def pwr_callback(pwr_data):
    '''
    Callback function that reads power data from module with continuous sampling
    Args:
        pwr_data : [time stamps(s), power(W)]
    Attributes:
        pwr_callback.start_time (float): the time that first data comes in, seconds
        pwr_callback.pwr_data: A list of [time stamp (s), power (W)]
    '''
    if pwr_callback.start_time is None:
        pwr_callback.start_time = time.time() * 1000
    pwr_callback.pwr_data.append(pwr_data)


def update_pwr(num, x, y, line):
    '''
    update function that updates the power to draw on the plot
    '''
    line.set_data(x[:num], y[:num])
    return line,

def pwr_animation(pwr_data):
    '''
    Function that creates an animation to display the readings
    Args:
        pwr_data : [time stamps(s), power(W)]
    '''
    pwr_data = np.array(pwr_data)
    fig = plt.figure()
    plt.xlim(0, MEASURE_TIME * 1000)
    plt.xlabel('time (ms)')
    plt.ylabel('power (W)')
    plt.title('power reading with sampling interval {}ms'.format(SAMPLE_INTERVAL))
    x = pwr_data[:,0]
    y = pwr_data[:,1]
    line, = plt.plot(x, y, color='r')
    DATA_LENGTH = pwr_data
    pwr_ani = animation.FuncAnimation(fig, update_pwr, len(pwr_data),fargs=[x,y,line],
         interval = 20, repeat=False)
    plt.show()

pwr_callback.pwr_data = []
pwr_callback.start_time = None
def main():
    '''
    main function
    Generate an animation that displays readings in real time.
    '''
    ina_sensor = ina219_pi_seelab()
    ina_sensor.run(SAMPLE_INTERVAL, pwr_callback)
    time.sleep(MEASURE_TIME)
    ina_sensor.stop()
    pwr_animation(pwr_callback.pwr_data)
if __name__ == '__main__':
    main()


