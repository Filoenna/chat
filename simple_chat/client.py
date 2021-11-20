import logging

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import threading


class ChatClient:
    def __init__(self, host, port):
        self.logger = self._setup_logger()
        self.socket = self._setup_socket(host, port)

        thread = Thread(target=self.send_message)
        thread.daemon = True
        thread.start()

        while True:
            data = self.socket.recv(4096)
            if not data:
                break
            self.logger.info(data.decode())

    def send_message(self):
        while True:
            user_message = input()
            self.socket.send(user_message.encode("utf-8", "backslashreplace"))

    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        return sock

    @staticmethod
    def _setup_logger():
        logger = logging.getLogger("chat_server")
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger


if __name__ == "__main__":
    client = ChatClient("localhost", 4333)
