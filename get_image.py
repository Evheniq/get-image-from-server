import socket
import io
import time
import PIL.Image as Image
from threading import Thread


class GetImageFromServer:
    def __init__(self, host, port, imagePath='./image/saved.png'):
        self.host = host
        self.port = port
        self.imagePath = imagePath
        Thread(target=self.main, daemon=True).start()
        time.sleep(1)

    def main(self):
        bytesImage = self.get_bytes_from_server()
        if self.save_bytes_to_image(bytesImage):
            print('Image saved into:', self.imagePath)
        else:
            print('Can`t save image')

    def get_bytes_from_server(self):
        maxChunks = 256

        bytesSortedList = [b'' for _ in range(maxChunks)]

        sock = socket.socket()
        sock.connect((self.host, self.port))
        print('Socket connected')

        for index_request in range(maxChunks):
            print('Request number:', index_request)
            print()

            sock.send('next'.encode())
            data = sock.recv(2048)

            if data == b'':
                break

            numberOfChunk = data[0]
            bytesSortedList[numberOfChunk] = data[1:]

            print('Number of chunk:', numberOfChunk)
            print('Data:', data[:20] + b'...')
            print()
            print()

        print('Socket close')
        sock.close()

        return b''.join(bytesSortedList)

    def save_bytes_to_image(self, bytesImage):
        try:
            image = Image.open(io.BytesIO(bytesImage))
            image.save(self.imagePath)
            return self.imagePath
        except FileNotFoundError:
            print('Not found path.')
