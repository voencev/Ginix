if len(args) == 0:
    sys.exit()

try:
    file = open(args[0], 'r')
    print(file.read())
    file.close()
except:
    print('Error: incorrect path')
    sys.exit()