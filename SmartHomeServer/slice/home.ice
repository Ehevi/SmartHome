module Home {
    exception UnknownException { string reason; };

    enum PowerState { ON, OFF };

    interface Device {
        PowerState getPowerState();
        void setPowerState(PowerState powerState);
    };

    enum LightIntensity { LOW, MEDIUM, HIGH };

    exception UnknownLightIntensity { string reason; };

    interface Light extends Device {
        LightIntensity getIntensity();
        void setIntensity(LightIntensity intensity) throws UnknownLightIntensity;
    };

    enum LightColor { RED, BLUE, GREEN };

    exception UnknownLightColor { string reason; };

    interface ColoredLight extends Light {
       LightColor getColor();
       void setColor(LightColor color) throws UnknownLightColor;
    };

    enum LightDirection { NORTH, SOUTH, EAST, WEST };

    exception UnknownLightDirection { string reason; };

    interface DirectedLight extends Light {
        LightDirection getDirection();
        void setDirection(LightDirection direction) throws UnknownLightDirection;
    };

    enum DoorState { OPEN, CLOSED };

    exception UnknownDoorState { string reason; };

    interface Door extends Device {
        DoorState getState();
        void setState(DoorState state) throws UnknownDoorState;
    };

    interface Thermostat extends Device {
        int getTemperature();
        void setTemperature(int temperature) throws UnknownException;
    };
};
