import os
import sys

args = []


def file_exists(file_path,file_name):
    if file_name in os.listdir(file_path):
        return True
    else:
        return False

while True:
    command = []
    print(os.getcwd(),'>',sep='',end=' ')
    
    input_str = input()
    tmp_str = ''
    is_str = False
    for i in range(0,len(input_str)):
        if input_str[i] == ' ' and is_str == False:
            command.append(tmp_str)
            tmp_str = ''
        elif input_str[i] == "'":
            is_str = not is_str
        else:
            tmp_str += input_str[i]
        
    command.append(tmp_str)
    tmp_str = ''
       
    if len(command) == 0:
        continue
    
    if command[0] == 'exit':
        break

    if file_exists(os.getcwd(),command[0]+'.py') == True:
        for i in range(1,len(command)):
            args.append(command[i])
        try:
            with open(os.getcwd()+'/'+command[0]+'.py') as program:
                exec(program.read())
        except SystemExit:
            pass
        args.clear()
        continue
    
    if file_exists('/bin/',command[0]+'.py') == True:
        for i in range(1,len(command)):
            args.append(command[i])
        try:
            with open('/bin/'+command[0]+'.py') as program:
                exec(program.read())
        except SystemExit:
            pass
        args.clear()
        continue
        
    print('Unknown command:', command[0])