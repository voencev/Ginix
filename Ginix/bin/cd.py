if len(args) == 0:
    sys.exit()

try:
    os.chdir(args[0])
except:
    print('Error: incorrect path')
    sys.exit()