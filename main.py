from ppadb.client import Client as AdbClient
import os
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

def change_directory(cwd, directory):
    output = device.shell(f'cd {cwd}/{directory}; ls -m').split(',')
    for i in output:
        print(str(output.index(i)) + ": " + i)
    global current_dir
    current_dir = f'{cwd}/{directory}'

def pull_a_file(file):
    file2 = file.split("/")[-1]
    device.pull(f"{file}", f"{file2}")
    print(f"The file is successfully pulled and stored as {file2}")

def push_a_file(file):
    print(file)
    file2 = file.split("\\")[-1]
    device.shell("mkdir -p /sdcard/ADBfilemanager/")
    device.push(f'{file}', f'/sdcard/ADBfilemanager/{file2}')
    print(f'The file is pushed successfully and stored as {file2}')

for device in devices:

    output = device.shell(("ls /sdcard -m")).split(",")
    current_dir = "/sdcard"
    for i in output:
        print(str(output.index(i)) + ": " + i)
    while True:
        choice = int(input("\nChoose your choice: \n 1: Change directory     2: Pull a file      3: Push a file      0: Exit "))
        if choice == 1:
            directory_index = int(input("Please enter the index of the directory you wish to change to: "))
            directory = output[directory_index].strip()
            change_directory("/sdcard", directory)
            print(current_dir)
        elif choice == 0:
            exit()
        elif choice == 2:
            files = device.shell(f"find {current_dir} -maxdepth 1 -type f").split("\n")
            for i in files:
                print(str(files.index(i)) + ": " + i)
            file_index = int(input("\nPlease enter the index of the file you wish to pull: "))
            file_to_pull = files[file_index].strip()
            print(file_to_pull)
            pull_a_file(file_to_pull)

        elif choice == 3:
            file_path = input("Please enter the full path of the file you wish to push: ")
            file_path = os.path.abspath(file_path)
            print(file_path)
            file_exists = os.path.isfile(file_path)
            print(file_exists)
            if file_exists == True:
                push_a_file(file_path)
                
            
