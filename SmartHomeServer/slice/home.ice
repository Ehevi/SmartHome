module Home {
exception HomeStaffStateException {
    string reason;
};

interface Light {
    void setBrightness(double b) throws HomeStaffStateException;
    double getBrightness() throws HomeStaffStateException;
};