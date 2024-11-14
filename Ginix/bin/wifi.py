if len(args) == 0:
    if wifi.active() == True:
        print('Wi-Fi connected')
    else:
        print('Wi-Fi not connected')
elif len(args) == 1:
    if args[0] == 'connect':
        ssid = ''
        password = ''
        import json
        with open("/config/networks.json","r") as file:
            file_data = json.load(file)
            if file_data['current'] == -1:
                print('Error: network not selected')
                file.close()
                sys.exit()
            ssid = file_data["networks"][file_data['current']]["ssid"]
            password = file_data["networks"][file_data['current']]["pass"]
        wifi.active(True)
        wifi.connect(ssid, password)
        for i in range(0,10):
            if not wifi.isconnected():
                print('.',end='')
                time.sleep(1)
            else:
                break
        if wifi.isconnected():
            print()
            print('Wi-Fi connected')
        else:
            print("Error: can't connect")
    elif args[0] == 'disconnect':
        wifi.active(False)
    elif args[0] == 'config':
        print(wifi.ipconfig('addr4'))
    elif args[0] == 'saved':
        import json
        with open("/config/networks.json",'r+') as file:
            file_data = json.load(file)
            for i in range(0,len(file_data["networks"])):
                print(i,'. ',sep='',end='')
                print(file_data["networks"][i]["ssid"],'[',file_data["networks"][i]["pass"],']', end=' ')
                if file_data["current"] == i:
                    print('*')
                else:
                    print()
    elif args[0] == 'list':
        pass
elif len(args) == 2:
    if args[0] == 'select':
        import json
        with open("/config/networks.json",'r+') as file:
            file_data = json.load(file)
            if int(args[1]) < len(file_data["networks"]):
                file_data["current"] = int(args[1])
            else:
                print("Error: id doesn't exists")
        open('/config/networks.json', 'w').close()
        with open("/config/networks.json","r+") as file:
            json.dump(file_data, file)
    elif args[0] == 'delete':
        import json
        with open("/config/networks.json","r+") as file:
            file_data = json.load(file)
            if file_data["current"] == int(args[1]):
                file_data["current"] = -1
            file_data["networks"].pop(int(args[1]))
        open('/config/networks.json', 'w').close()
        with open("/config/networks.json","r+") as file:
            json.dump(file_data, file)
elif len(args) == 3:
    if args[0] == 'new':
        import json
        with open("/config/networks.json",'r+') as file:
            file_data = json.load(file)
            file_data["networks"].append({'ssid':args[1],'pass':args[2]})
            file.seek(0)
            json.dump(file_data, file)
