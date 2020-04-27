# ina219-pi-seelab
A Python module for current sensor INA219 on Raspberry Pi.

Work with Python 2.7 and 3.7.

## Installation

Download the desired version from the corresponding branch (`master` for Python >= 3.7, `py2.7` for Python >= 2.7) and decompress it. `cd` into it, then:

```shell
# for Python 2.7
pip2 install .
# or for Python 3.7
pip3 install .
```

The required modules will be installed automatically. Basically, this module adds some wrap-up on top of [pi-ina219](https://pypi.org/project/pi-ina219/) module in PyPI.

By default, the module will be installed to your packages library for Python. However, if you do want to install the module in "editable" mode, which will be based on the code in the current directory:

```shell
# for Python 2.7
pip2 install -e .
# or for Python 3.7
pip3 install -e .
```

## Demos

There are several handy demos included in the `demo` folder:

* [simple demo](./demo/demo_simple.py)

This demo shows how to create a separate thread for power monitoring and how to receive data with a `callback` function. The measured traces ([time(ms), power(mW)] pairs) will be logged into a text file.

* [animation demo](./demo/demo_animate.py)

This demo shows how to create a simple animation to view the power traces in real-time.

* [energy processing demo](./demo/demo_energy/)

This demo provides a processing script to calculate the energy for each phase based on the record time stamp.

## Notes

* Please check the settings of parameters in `ina219_pi_seelab/ina219_pi_seelab.py` before using.

  ```
  SHUNT_OHMS = 0.025          # shunt resistor in ohms
  MAX_EXPECTED_AMPS = 1.0     # max permitted current in amps
  ADDRESS = 0x40              # I2C address
  ```

  For specific settings, check [tutorial by Adafruit](https://learn.adafruit.com/adafruit-ina219-current-sensor-breakout/overview).

* The current version with animation and processing demos have not been thoroughly tested, thus the release is not ready. The prior release only includes the simple demo.

  