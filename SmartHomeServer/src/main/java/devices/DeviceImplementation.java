package devices;

import Home.Device;
import Home.PowerState;
import com.zeroc.Ice.Current;
import server.Server;

public class DeviceImplementation implements Device {
    private PowerState powerState = PowerState.OFF;
    @Override
    public PowerState getPowerState(Current current) {
        Server.logger.info("Power state checked!");
        return powerState;
    }

    @Override
    public void setPowerState(PowerState powerState, Current current) {
        Server.logger.info("Power state set");
        this.powerState = powerState;
    }
}
