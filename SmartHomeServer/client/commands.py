from Home import PowerState
from Home import LightIntensity
from Home import LightColor
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

def get_intensity(device, args):
    try:
        print(device.getIntensity())
    except Exception as e:
        print(e)

def set_intensity(device, args):
    intensity_str = args[1]
    try:
        if intensity_str == 'LOW':
            device.setIntensity(LightIntensity.LOW)
        elif intensity_str == 'MEDIUM':
            device.setIntensity(LightIntensity.MEDIUM)
        elif intensity_str == 'HIGH':
            device.setIntensity(LightIntensity.HIGH)
    except Exception as e:
        print(e)

def get_color(device, args):
    try:
        print(device.getColor())
    except Exception as e:
        print(e)

def set_color(device, args):
    color = args[1]
    try:
        if color == 'RED':
            device.setColor(LightColor.RED)
        if color == 'BLUE':
            device.setColor(LightColor.BLUE)
        if color == 'GREEN':
            device.setColor(LightColor.GREEN)
    except Exception as e:
        print(e)
