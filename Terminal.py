import subprocess
import os
#Popen : old interface
#Run : execute the comand and waiting result

while True:
    command = input(f"{os.getcwd()} > ")
 
 # Case cd for changing directory
    command_split = command.split(" ")
    if len(command_split)== 2 and command_split[0] == "cd":
        try: 
            os.chdir(command_split[1])
        except FileNotFoundError:
            print("ERROR : file doesn't exist")


 #exit terminal
    elif command.lower() == "exit":
        break
 
    else:
        resultat = subprocess.run(f"{command}",shell=True, capture_output=True, universal_newlines=True)

        print(resultat.stdout)
        print(resultat.stderr)
        print("exit pour sortir")
        