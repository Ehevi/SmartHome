package devices;

import Home.*;
import com.zeroc.Ice.Current;

public class DoorImplementation extends DeviceImplementation implements Door {

    private DoorState state = DoorState.CLOSED;
    @Override
    public DoorState getState(Current current) {
        return state;
    }

    @Override
    public void setState(DoorState state, Current current) throws UnknownDoorState {
        this.state = state;
    }
}
