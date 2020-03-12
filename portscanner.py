import socket
srv_addr = input("Type ip : ")
srv_portr = input("Type range of ports ex 5-200 : ")
lowp = int(srv_portr.split('-')[0])
highp = int(srv_portr.split('-')[1])
print("Scanning host", srv_addr, "from port", lowp, "to port", highp)
for port in range(lowp, highp):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = soc.connect_ex((srv_addr, port))
    if status == 0:
        print(port, "is open")
    else:
        print(port, "is closed")
    soc.close()
