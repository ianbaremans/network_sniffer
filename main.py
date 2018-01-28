import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
    raw_output = s.recvfrom(65565)
    bytes_raw_output = raw_output[0]
    bytes_output = str(bytes_raw_output).encode("utf-8").strip()
    adress_raw_output = raw_output[1]

    print(bytes_output)

