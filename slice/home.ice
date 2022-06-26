module Home {
    interface IDevice {
        string getDeviceInfo();
    };

    class Device {
        string name;
        string type;
    };
    
    /*exception HomeStaffStateException {
        string reason;
    };
    */

    interface ILight {
        void 
        // void setBrightness(double b) throws HomeStaffStateException;
        // double getBrightness() throws HomeStaffStateException;
    };

    enum LightColor {
        RED, BLUE, GREEN
    }
    
    exception UnknownLightColor {
        string reason;
    };

    sequence<LightColor> lightColors;

    enum LightIntensity {
        LOW, MEDIUM, HIGH
    };

    exception UnknownLightIntensity {
        string reason;
    };

    sequence<LightIntensity> lightIntensities;

    struct LightMode {
        LightColor color;
        LightIntensity intensity;
    };

    sequence<LightMode> lightModes;

    
};
