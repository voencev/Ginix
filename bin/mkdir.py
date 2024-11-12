if len(args) == 0:
    sys.exit()

try:
    os.mkdir(args[0])
except:
    print('Error: incorrect path')
    sys.exit()