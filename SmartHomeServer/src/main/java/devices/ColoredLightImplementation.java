package devices;

import Home.ColoredLight;
import Home.LightColor;
import Home.UnknownLightColor;
import com.zeroc.Ice.Current;

public class ColoredLightImplementation extends LightImplementation implements ColoredLight {
    private LightColor color = LightColor.BLUE;

    @Override
    public LightColor getColor(Current current) {
        return color;
    }

    @Override
    public void setColor(LightColor color, Current current) throws UnknownLightColor {
        this.color = color;
    }
}
