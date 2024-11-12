if len(args) == 0:
    ls = os.listdir()
    ls.sort()
    for i in range(0,len(ls)):
        ftype = ''
        if os.stat(ls[i])[0] == 16384:
            ftype = 'Dir: '
        elif os.stat(ls[i])[0] == 32768:
            ftype = 'File: '
        ls[i] = ftype + ls[i]
        print(ls[i])
else:
    path = os.getcwd()
    try:
        os.chdir(args[0])
    except:
        print('Error: incorrect path')
        sys.exit()
    ls = os.listdir()
    ls.sort()
    for i in range(0,len(ls)):
        ftype = ''
        if os.stat(ls[i])[0] == 16384:
            ftype = 'Dir: '
        elif os.stat(ls[i])[0] == 32768:
            ftype = 'File: '
        ls[i] = ftype + ls[i]
        print(ls[i])
    os.chdir(path)