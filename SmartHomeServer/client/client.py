import logging
import os
import sys
import Ice

from Home import DevicePrx
from Home import LightPrx

from commands import *

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
    def __init__(self):
        self.is_running = True
        self.devices_params = []

    def init_device_params(self, communicator):
        base_commands = [Command('pstate', get_power_state, 'check power state', 0),
                         Command('set-pstate', set_power_state, 'set power state to ON or OFF: set-pstate OFF', 1)]

        commands = base_commands
        base = communicator.stringToProxy('device1:tcp -h localhost -p 10000: udp -h localhost -p 10000')
        self.devices_params.append(DeviceParams('Device1', DevicePrx.uncheckedCast(base), commands))
        print(self.devices_params)

        light_commands = [Command('getBrightness', get_brightness, 'get brightness', 0)]
        commands = light_commands
        base = communicator.stringToProxy('light1:tcp -h localhost -p 10000: udp -h localhost -p 10000')
        self.devices_params.append(DeviceParams('Light1', LightPrx.uncheckedCast(base), commands))


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
                        print('device_id - enter device control mode')
                        print('devices - show available devices')
                        print('help - show help')
                        print('exit - shut down client')
                    elif args[0] == 'devices':
                        print(self.get_devices_string())
                    else:
                        for dp in self.devices_params:
                            if dp.name == args[0]:
                                prefix = args[0]
                                device_params = dp
                                print(dp.__dict__)
                else:
                    if args[0] == 'exit':
                        prefix = ''
                    elif args[0] == 'help':
                        for command in device_params.commands:
                            print(command.command, ' - ', command.desc)
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
                                    print(command.command, ' - ', command.desc)
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
    try:
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
        alert_client = SmartHomeClient()
        alert_client.run()
        print('Smart home client shut down')
    except KeyboardInterrupt:
        print('Smart home client shut down')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)