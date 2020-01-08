#!/usr/bin/python2
from ina219 import INA219
from ina219 import DeviceRangeError
import os
import time
import threading

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 1.0
ADDRESS = 0x40

class ina219_pi(object):
    def __init__(self, address=ADDRESS, shunt_ohms=SHUNT_OHMS,
                       max_expected_amps=MAX_EXPECTED_AMPS, filename=None):
        self.ina = INA219(shunt_ohms, max_expected_amps, address=address)
        self.ina.configure(self.ina.RANGE_16V)
        self.filename = filename
        self.f = None
        self.loop_thread = None
        self.callback = None

    def log(self, str):
        if self.f is not None:
            self.f.write(str)
            self.f.write('\n')
        else:
            print(str)

    def read_power(self):
        return self.ina.power()

    def read_voltage(self):
        return self.ina.voltage()

    def read_current(self):
        return self.ina.current()

    def test_read(self):
        while True:
            print("Bus Voltage: %.3f V" % self.ina.voltage())
            try:
                print("Bus Current: %.3f mA" % self.ina.current())
                print("Power: %.3f mW" % self.ina.power())
                print("Shunt voltage: %.3f mV" % self.ina.shunt_voltage())
            except DeviceRangeError as e:
                # Current out of device range with specified shunt resister
                print(e)

    def run_in_loop(self):
        self.is_loop_running = True
        self.start_time = time.time() * 1000
        while self.is_loop_running:
            t = float(time.time() * 1000 - self.start_time) # ms
            pwr = self.read_power() # mW
            output_str = str(t) + ',' + str(pwr)
            if self.callback is not None:
                self.callback([t, pwr]) # Pack into list and call functioin

            self.log(output_str)
        # End of the loop

    def run(self, callback=None):
        # Create file
        if self.filename is not None:
            # Delete existing file if any
            if os.path.exists(self.filename):
                os.remove(self.filename)
            self.f = open(self.filename, "w+"):
        self.callback = callback

        # Start thread
        self.loop_thread = threading.Thread(target=self.run_in_loop)
        self.loop_thread.start()

    def stop(self):
        # Stop running thread
        assert(self.loop_thread is not None)
        self.is_loop_running = False
        self.loop_thread.join()

        # Flush file
        if self.f is not None:
            self.f.close()
