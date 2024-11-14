import socket

def get(url, addr_family=0, use_stream=False):
    # Split the given URL into components.
    proto, _, host, path = url.split(b"/", 3)
    assert proto == b"http:"

    # Lookup the server address, for the given family and socket type.
    ai = socket.getaddrinfo(host, 80, addr_family, socket.SOCK_STREAM)
    print("Address infos:", ai)

    # Select the first address.
    ai = ai[0]

    # Create a socket with the server's family, type and proto.
    s = socket.socket(ai[0], ai[1], ai[2])

    # Connect to the server.
    addr = ai[-1]
    print("Connect address:", addr)
    s.connect(addr)

    # Send request and read response.
    request = b"GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host)
    if use_stream:
        # MicroPython socket objects support stream (aka file) interface
        # directly, but the line below is needed for CPython.
        s = s.makefile("rwb", 0)
        s.write(request)
        print(s.read())
    else:
        s.send(request)
        print(s.recv(4096))

    # Close the socket.
    s.close()

if len(args) == 2:
    if args[0] == 'get':
        get(str.encode(args[1]))