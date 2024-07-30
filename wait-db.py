import socket
import time
import os

if __name__ == '__main__':
	port = int(os.environ["DB_PORT"])  # 5432
	host = os.environ["DB_HOST"]  # db
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	while True:
		try:
			s.connect((host, port))
			s.close()
			break
		except socket.error as ex:
			time.sleep(1)
