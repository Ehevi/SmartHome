module Home {
    exception HomeStaffStateException {
        string reason;
    };

    enum PowerState { ON, OFF };

    interface Device {
        PowerState getPowerState();
        void setPowerState(PowerState powerState);
    };

    interface Light {
        void setBrightness(double b) throws HomeStaffStateException;
        double getBrightness() throws HomeStaffStateException;
    };
};
