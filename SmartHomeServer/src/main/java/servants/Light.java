package servants;
import Home.HomeStaffStateException;
import com.zeroc.Ice.Current;

public class Light implements Home.Light {

    public Light() {

    }
    @Override
    public void setBrightness(double b, Current current) throws HomeStaffStateException {

    }

    @Override
    public double getBrightness(Current current) throws HomeStaffStateException {
        return 0;
    }
}
