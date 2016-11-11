from setuptools import setup
with open('readme.txt') as f:
    readme = f.read()

requires = ['mido', 'python-rtmidi']

setup(
    name='apc40_switch',
    install_requires=requires,
    version='0.1',
    author='Josh Erickson',
    author_email='ponderosa@imaginaryphotons.com',
    license='MIT',
    description='Switch the firmware mode of an Akai APC-40.',
    long_description=readme,
    py_modules=['apc40_switch'])