if len(args) == 0:
    sys.exit()

if len(args) > 1:
    if args[0] == '-rf':
        try:
            os.rmdir(args[1])
        except:
            print('Error: incorrect path')
            sys.exit()
elif len(args) == 1:
    try:
        os.remove(args[0])
    except:
        print('Error: incorrect path')
        sys.exit()