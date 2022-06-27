package devices;

import Home.*;
import com.zeroc.Ice.Current;

public class ThermostatImplementation extends DeviceImplementation implements Thermostat {

    private int temperature = 25;
    @Override
    public int getTemperature(Current current) {
        return temperature;
    }

    @Override
    public void setTemperature(int temperature, Current current) throws UnknownException {
        this.temperature = temperature;
    }
}
