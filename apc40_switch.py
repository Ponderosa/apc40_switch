"""
The apc40_switch uses the Mido midi library to switch the
user defined firmware mode on the APC40.

Requirements: mido, python-rtmidi
"""

import mido


def apc40_set_fw_mode(mode):
    """Set the firmware mode to the mode supplied by the user"""
    if mode > 2:
        print("Please enter a valid mode\n\
               0: Generic Mode\n\
               1: Ableton Live Mode\n\
               2: Alternate Ableton Live Mode")
    else:
        mido.set_backend('mido.backends.rtmidi')
        try:
            output = mido.open_output('Akai APC40')
        except ImportError:
            print("RT Midi Library not found")
        except OSError:
            print("Please connect APC via USB and power up APC.")

        msg = mido.parse([0xF0,
                          0x47,
                          0x00,
                          0x73,
                          0x60,
                          0x00,
                          0x04,
                          (0x40 + mode),
                          0x08,
                          0x04,
                          0x01,
                          0xF7])

        output.send(msg)
