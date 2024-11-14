if len(args) == 0:
    ttime = time.localtime(time.time() + UTC_OFFSET*60*60)
    print(ttime[2],'.',ttime[1],'.',ttime[0],' ',"{:02}".format(ttime[3]),':',"{:02}".format(ttime[4]),':',"{:02}".format(ttime[5]),sep='')
elif len(args) == 1:
    if args[0] == 'sync':
        import ntptime
        ntptime.settime() # синхронизания часов с интернетом
elif len(args) == 2:
    if args[0] == 'local':
        UTC_OFFSET = int(args[1])