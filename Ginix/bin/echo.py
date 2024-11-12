if len(args) == 0:
    sys.exit()

if len(args) == 1:
    print(args[0])
elif len(args) == 3 and args[1] == '>':
    try:
        file = open(args[2], 'w')
        file.write(args[0])
        file.close()
    except:
        print('Error: incorrect path')
        sys.exit()
else:
    print('Error:')