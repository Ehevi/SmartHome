import logging
import os
import sys
import Ice

from Home import DevicePrx
from Home import LightPrx
from Home import ColoredLightPrx
from Home import DirectedLightPrx
from Home import DoorPrx
from Home import ThermostatPrx

from commands import *

#port = 10001
#port = 10000

class Command:
    def __init__(self, command, callback, desc, args_num):
        self.command = command
        self.callback = callback
        self.desc = desc
        self.args_num = args_num


class DeviceParams:
    def __init__(self, name, device_prx, commands):
        self.name = name
        self.device_prx = device_prx
        self.commands = commands


class SmartHomeClient:
    def __init__(self, port):
        self.is_running = True
        self.devices_params = []
        self.port = port

    def init_device_params(self, communicator):
        base_commands = [Command('get-state', get_power_state, 'Check power state', 0),
                         Command('set-state', set_power_state, 'Set power state to ON or OFF. Example: set-state OFF', 1)]

        commands = base_commands
        base = communicator.stringToProxy('device1:tcp -h localhost -p ' + port + ': udp -h localhost -p ' + port)
        self.devices_params.append(DeviceParams('Device1', DevicePrx.uncheckedCast(base), commands))
        print(self.devices_params)

        light_commands = [Command('get-intensity', get_intensity, 'Get light intensity', 0),
                            Command('set-intensity', set_intensity, 'Set light intensity to one of the following: LOW, MEDIUM, HIGH. Example: set-intensity LOW', 1)]
        commands = base_commands + light_commands
        base = communicator.stringToProxy('light1:tcp -h localhost -p ' + port + ': udp -h localhost -p ' + port)
        self.devices_params.append(DeviceParams('Light1', LightPrx.uncheckedCast(base), commands))

        color_light_commands = [Command('get-color', get_color, 'get color', 0),
                                Command('set-color', set_color, 'set light color to one of the following: RED, BLUE, GREEN. Example: set-color GREEN', 1)]
        commands = base_commands + light_commands + color_light_commands
        base = communicator.stringToProxy('coloredLight1:tcp -h localhost -p ' + port + ':udp -h localhost -p ' + port)
        self.devices_params.append(DeviceParams('ColoredLight1', ColoredLightPrx.uncheckedCast(base), commands))

        directed_light_commands = [Command('get-direction', get_direction, 'Get light direction', 0),
                                    Command('set-direction', set_direction, 'Set light direction to one of the following: NORTH, SOUTH, EAST, WEST. Example: set-direction WEST', 1)]
        commands = base_commands + light_commands + directed_light_commands
        base = communicator.stringToProxy('directedLight1:tcp -h localhost -p ' + port + ':udp -h localhost -p ' + port)
        self.devices_params.append(DeviceParams('DirectedLight1', DirectedLightPrx.uncheckedCast(base), commands))

        door_commands = [Command('get-door-state', get_door_state, 'Get door state', 0),
                        Command('set-door-state', set_door_state, 'Open or close the door. Example: set-door-state OPEN', 1)]
        commands = base_commands + door_commands
        base = communicator.stringToProxy('door1:tcp -h localhost -p ' + port + ':udp -h localhost -p ' + port )
        self.devices_params.append(DeviceParams('Door1', DoorPrx.uncheckedCast(base), commands))

        thermostat_commands = [Command('get-temp', get_temp, 'Get temperature', 0),
                                Command('set-temp', set_temp, 'Set temperature. Example: set-temp 25', 1)]
        commands = base_commands + thermostat_commands
        base = communicator.stringToProxy('thermostat1:tcp -h localhost -p ' + port + ':udp -h localhost -p ' + port)
        self.devices_params.append(DeviceParams('Thermostat1', ThermostatPrx.uncheckedCast(base), commands))


    def get_devices_string(self):
        av_devices = 'Available devices: '
        for device_params in self.devices_params:
            av_devices += device_params.name + ' '
        return av_devices

    def print_devices(self):
        logging.info(self.get_devices_string())

    def run_console(self):
        self.print_devices()
        prefix = ''
        device_params = None
        prompt_msg = '> '
        while self.is_running:
            text = input(prefix + prompt_msg)
            if text:
                args = text.split()
                if not prefix:
                    if args[0] == 'exit':
                        self.is_running = False
                    elif args[0] == 'help':
                        print('***')
                        print('*** <device_id> : enter device control mode')
                        print('*** devices     : list available devices')
                        print('*** help        : here you are')
                        print('*** exit        : shut down')
                        print('***')
                    elif args[0] == 'devices':
                        print(self.get_devices_string())
                    else:
                        for dp in self.devices_params:
                            if dp.name == args[0]:
                                prefix = args[0]
                                device_params = dp
                else:
                    if args[0] == 'exit':
                        prefix = ''
                    elif args[0] == 'help':
                        print('***')
                        for command in device_params.commands:
                            print('***', command.command.ljust(14), ':', command.desc)
                        print('*** exit           : Go back')
                        print('***')
                    elif args[0] == 'devices':
                        print(self.get_devices_string())
                    else:
                        command_found = False
                        for command in device_params.commands:
                            if command.command == args[0]:
                                if command.args_num == len(args) - 1:
                                    command.callback(device_params.device_prx, args)
                                else:
                                    print('Wrong number of parameters')
                                    print(command.command, ':', command.desc)
                                command_found = True
                                break
                        if not command_found:
                            print('Command not found')

    def run(self):
        logging.info('Starting smart home client...')
        with Ice.initialize(sys.argv) as communicator:
            self.init_device_params(communicator)
            self.run_console()


if __name__ == '__main__':
    server = sys.argv[1]
    print(sys.argv)
    if (server == 'server1'):
        port = '10001'
    elif (server == 'server2'):
        port = '10000'
    else:
        print('Please specify the server connection.')
        sys.exit(0)
    try:
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
        alert_client = SmartHomeClient(port)
        alert_client.run()
        print('Smart home client shut down')
    except KeyboardInterrupt:
        print('Smart home client shut down')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)