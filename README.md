## Video camera streaming server

### Project description
Video camera streaming server application is a cross-platform application that runs<br>
either android or IOS. It establishes server connection and listens to a client to connect to it.<br>
Once the connection is established, frames are sent to the client(On desktop) through the local network<br>
The client side of this application can be found on the following github repo([Video camera streaming client](https://github.com/djaliloua/ClientAppStream))

### Used libraries

 - socket
 - Kivy
 - kivymd
 - opencv




## Steps to compile the source code to andorid
### Install WSL2 for windows 11/10
type in powershell
wsl --install

### Deploy kivyMd App Android
[Deploy kivy](https://kivy.org/doc/stable/guide/packaging-android.html)

### Install buldozer
[Install Buildozer and its dependencies](https://buildozer.readthedocs.io/en/latest/installation.html)

And then run buildozer android debug deploy run or buildozer android debug deploy run logcat

### Connect Android phone Linux
first disable the firewall (optional)
- Create server connection(Windows powershell): adb -a -P 5000 nodaemon server
- Create client connection(Linux ubuntu shell): adb -P 5000 -H  192.168.56.1 devices -l
- This to set env variable: export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | awk '/nameserver/ {print $2}'):5000

### Wireless connection
- Run on Linux shell: adb -P 5000 -H 192.168.56.1 tcpip 5555
- adb connect 192.168.1.5(android ip address)
- then remove the cable

### Debug with adb logcat commands
- debug a service called Myservice: adb logcat "Myservice:D *:S"
- Debug background services: adb logcat Myservice *:S python:D


#### Use ctrl+shift+V to previeux markdown in VSC