package server;

import com.zeroc.Ice.*;

import java.util.Arrays;
import java.util.logging.Logger;

public class Server {
    public static final Logger logger = Logger.getLogger(Server.class.getName());
    private static String adapterName = "IceAdapter";
    private static ObjectAdapter adapter;

    public static void main(String[] args) {
        Communicator communicator = com.zeroc.Ice.Util.initialize(args);
        System.out.println(Arrays.toString(args));
        adapter = communicator.createObjectAdapter(adapterName);
        init();
        adapter.activate();
        logger.info("Smart home server is running...");
        communicator.waitForShutdown();

    }

    public static void init() {
        adapter.add(new devices.DeviceImplementation(), com.zeroc.Ice.Util.stringToIdentity("DeviceSample"));
        adapter.add(new devices.LightImplementation(), com.zeroc.Ice.Util.stringToIdentity("CeilingLight"));
        adapter.add(new devices.LightImplementation(), com.zeroc.Ice.Util.stringToIdentity("RecessedLight"));
        adapter.add(new devices.LightImplementation(), com.zeroc.Ice.Util.stringToIdentity("WallScone"));
        adapter.add(new devices.ColoredLightImplementation(), com.zeroc.Ice.Util.stringToIdentity("BlissBulb"));
        adapter.add(new devices.DirectedLightImplementation(), com.zeroc.Ice.Util.stringToIdentity("TrackLight"));
        adapter.add(new devices.DoorImplementation(), com.zeroc.Ice.Util.stringToIdentity("FrontDoor"));
        adapter.add(new devices.DoorImplementation(), com.zeroc.Ice.Util.stringToIdentity("BackDoor"));
        adapter.add(new devices.ThermostatImplementation(), com.zeroc.Ice.Util.stringToIdentity("Thermostat"));
    }
}
