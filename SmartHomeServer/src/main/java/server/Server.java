package server;

import com.zeroc.Ice.*;

import java.util.Arrays;
import java.util.logging.Logger;

public class Server {
    public static final Logger logger = Logger.getLogger(Server.class.getName());
    // private List<DeviceImplementation>
    private static String adapterName = "IceAdapter";
    private static ObjectAdapter adapter;

    public static void main(String[] args) {
        //try (
        //
        Communicator communicator = com.zeroc.Ice.Util.initialize(args);
        //System.out.println(Arrays.toString(args));
        logger.info("Smart home server is starting...");
        adapter = communicator.createObjectAdapterWithEndpoints(adapterName, "tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z");
        logger.info("Adapter created!");

        adapter.add(new servants.Light(), com.zeroc.Ice.Util.stringToIdentity("light1"));
        adapter.add(new devices.DeviceImplementation(), com.zeroc.Ice.Util.stringToIdentity("device1"));
        // initObjects();

        adapter.activate();
        logger.info("Adapter activated");
        communicator.waitForShutdown();
        /*
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException |

                 IllegalAccessException | IOException e) {
            throw new RuntimeException(e);
        }
         */
        // server.Server app = new server.Server();
    }
}
