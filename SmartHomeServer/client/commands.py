from Home import PowerState
#from Home.AC import PollutionLevel
#from Home.Kitchen import BakingSide, BakingParams

def get_power_state(device, args):
    try:
        print(device.getPowerState())
    except Exception as e:
        print(e)


def set_power_state(device, args):
    pstate_str = args[1]
    try:
        if pstate_str == 'ON':
            device.setPowerState(PowerState.ON)
        elif pstate_str == 'OFF':
            device.setPowerState(PowerState.OFF)
        else:
            print('Unknown parameter {}'.format(pstate_str))
    except Exception as e:
        print(e)

def get_brightness(device, args):
    try:
        print(device.getBrightness())
    except Exception as e:
        print(e)
