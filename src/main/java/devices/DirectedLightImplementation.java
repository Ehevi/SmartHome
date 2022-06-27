package devices;

import Home.*;
import com.zeroc.Ice.Current;

public class DirectedLightImplementation extends LightImplementation implements DirectedLight {
    private LightDirection direction = LightDirection.WEST;
    @Override
    public LightDirection getDirection(Current current) {
        return direction;
    }

    @Override
    public void setDirection(LightDirection direction, Current current) throws UnknownLightDirection {
        this.direction = direction;
    }
}
