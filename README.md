# SmartHome
## Prerequisites
Make sure the following are installed:

![prereq](https://user-images.githubusercontent.com/48785655/175978769-e8ec793b-13fd-4561-ad2c-603643b2ba19.png)

## Overview
Visual representation of the [home.ice](https://github.com/Ehevi/SmartHome/blob/main/slice/home.ice) file and [implemented](https://github.com/Ehevi/SmartHome/tree/main/src/main/java/devices) device names [used](https://github.com/Ehevi/SmartHome/blob/main/src/main/java/server/Server.java):

![ice](https://user-images.githubusercontent.com/48785655/175977447-a738bde2-4323-404c-9261-8a656d781d14.png)

## Running the application
```
git clone https://github.com/Ehevi/SmartHome
cd SmartHome
gradle build
```
### Run the [Server](https://github.com/Ehevi/SmartHome/blob/main/src/main/java/server/Server.java)
Pass one of the [config](https://github.com/Ehevi/SmartHome/tree/main/config) files with the `--Ice.Config=` option. To meet the task requirements, running multiple server instances need to be allowed, preferably with the use of different config files.

![configggg](https://user-images.githubusercontent.com/48785655/175977470-1426c159-7a6a-4325-b7b5-d1b6140270c1.png)

### Client
Open the terminal in the `~/SmartHome/client` directory and run the client. The parameter you pass is the name of the corresponding server (assuming that one of the provided config files is being used).
```
python3 client.py server1
```
