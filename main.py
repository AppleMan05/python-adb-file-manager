from ppadb.client import Client as AdbClient
import subprocess
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

def change_dir(directory):
    output =device.shell(f'ls -m /sdcard/{directory.strip()}').split(",")
    for i in output:
        print(str(output.index(i)) + ": " + i)
for device in devices:
    #print(device.cpu_count())
    #print(device.shell("ls /sdcard"))
    output = device.shell(("ls /sdcard -m")).split(",")
    for i in output:
        print(str(output.index(i)) + ": " + i)
        #print(output)
    choice = int(input("\nChoose your choice: \n 1: Change directory     2: Pull a file      3: Push a file      0: Exit "))
    if choice == 1:
        directory_index = int(input("Please enter the index of the directory you wish to change to: "))
        directory = output[directory_index]
        print(directory.strip())
        change_dir(directory)

