from Home import PowerState
from Home import LightIntensity
from Home import LightColor
from Home import LightDirection
from Home import DoorState

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
        elif color == 'BLUE':
            device.setColor(LightColor.BLUE)
        elif color == 'GREEN':
            device.setColor(LightColor.GREEN)
    except Exception as e:
        print(e)

def get_direction(device, args):
    try:
        print(device.getDirection())
    except Exception as e:
        print(e)

def set_direction(device, args):
    direction = args[1]
    try:
        if direction == 'WEST':
            device.setDirection(LightDirection.WEST)
        elif direction == 'EAST':
            device.setDirection(LightDirection.EAST)
        elif direction == 'SOUTH':
            device.setDirection(LightDirection.SOUTH)
        elif direction == 'NORTH':
            device.setDirection(LightDirection.NORTH)
    except Exception as e:
        print(e)

def get_door_state(device, args):
    try:
        print(device.getState())
    except Exception as e:
        print(e)

def set_door_state(device, args):
    state = args[1]
    try:
        if state == 'OPEN':
            device.setState(DoorState.OPEN)
        elif state == 'CLOSED':
            device.setState(DoorState.CLOSED)
    except Exception as e:
        print(e)

def get_temp(device, args):
    try:
        print(device.getTemperature())
    except Exception as e:
        print(e)

def set_temp(device, args):
    temp = args[1]
    try:
        device.setTemperature(temp)
    except Exception as e:
        print(e)
