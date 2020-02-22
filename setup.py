from setuptools import setup

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

SHORT_DESCRIPTION = (
    'Python module for INA219.'
)

VERSION = '1.0'

DEPENDENCIES = [
    'pi-ina219',
    'numpy',
    'matplotlib'
]

setup(
    name='ina219_pi_seelab',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=['ina219_pi_seelab'],
    python_requires='>=3.7.3',
    install_requires=DEPENDENCIES
)
