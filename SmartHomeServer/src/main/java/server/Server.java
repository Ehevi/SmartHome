package server;

import com.zeroc.Ice.*;
import devices.DeviceImplementation;

import java.util.Arrays;
import java.util.logging.Logger;

public class Server {
    public static final Logger logger = Logger.getLogger(Server.class.getName());
    // private List<DeviceImplementation>
    private static String adapterName = "IceAdapter";
    private static ObjectAdapter adapter;

    public static void main(String[] args) {
        Communicator communicator = com.zeroc.Ice.Util.initialize(args);
        System.out.println(Arrays.toString(args));
        logger.info("Smart home server is starting...");
        adapter = communicator.createObjectAdapter(adapterName);
        logger.info("Adapter created!");

        DeviceImplementation servant = null;

        adapter.add(new devices.DeviceImplementation(), com.zeroc.Ice.Util.stringToIdentity("device1"));
        adapter.add(new devices.LightImplementation(), com.zeroc.Ice.Util.stringToIdentity("light1"));
        adapter.add(new devices.ColoredLightImplementation(), com.zeroc.Ice.Util.stringToIdentity("coloredLight1"));
        adapter.add(new devices.DirectedLightImplementation(), com.zeroc.Ice.Util.stringToIdentity("directedLight1"));
        adapter.add(new devices.DoorImplementation(), com.zeroc.Ice.Util.stringToIdentity("door1"));
        adapter.add(new devices.ThermostatImplementation(), com.zeroc.Ice.Util.stringToIdentity("thermostat1"));
        // initObjects();

        adapter.activate();
        logger.info("Adapter activated");
        communicator.waitForShutdown();

    }
}
