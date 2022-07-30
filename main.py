import bluetooth
import subprocess

def discover_all_devices():
    devices = {} # device name to device address mapped
    print ("performing inquiry...")

    nearby_devices = bluetooth.discover_devices(lookup_names = True)

    print ("found %d devices" % len(nearby_devices))

    for name, addr in nearby_devices:
        print (addr, name)
        devices[addr] = name.decode("utf-8")

    return devices

def connect_to_device(devices, device_name, passkey=None):
    print("connecting to ", device_name, " ...")

    if not (device_name in devices):
        print("cant find device name in search")
        return
    
    addr = devices[device_name]
    RFCOMM_PORT = 1 # Default Radio Frequency Communication

    if passkey:
        # Start a new "bluetooth-agent" process where XXXX is the passkey
        subprocess.call("bluetooth-agent " + passkey + " &",shell=True)

    # Now, connect in the same way as always with PyBlueZ
    try:
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((addr,RFCOMM_PORT))
    except bluetooth.btcommon.BluetoothError as err:
        # Error handler
        pass

devices = discover_all_devices()
connect_to_device(devices, 'H1')