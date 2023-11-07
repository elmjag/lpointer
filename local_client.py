import socket
import struct

PORT = 9000


class LocalClient:
    def set_angles(self, base, mount):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", PORT))

        sock.sendall(struct.pack("<ff", base, mount))

        sock.close()
