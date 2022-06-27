package devices;

import Home.*;
import com.zeroc.Ice.Current;

public class LightImplementation extends DeviceImplementation implements Light {
    private LightIntensity intensity = LightIntensity.MEDIUM;

    @Override
    public LightIntensity getIntensity(Current current) {
        return intensity;
    }

    @Override
    public void setIntensity(LightIntensity intensity, Current current) throws UnknownLightIntensity {
        this.intensity = intensity;
    }
}
