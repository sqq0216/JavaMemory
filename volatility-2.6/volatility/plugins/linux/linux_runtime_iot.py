#!usr/bin/python
# -*- coding:utf-8 -*-
import socket
import time
def main():

    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpSocket.bind(('', 6666))
    tcpSocket.listen(5)

    try:
        print "waiting for connection..."
        client, addr = tcpSocket.accept()
        print "...connected from:", addr
            # self.conf = Conf()
            # self.conf.vconfig(self.run_command, self.stop_command)
            # self.conf.start()
    except Exception, e:
        print repr(e)

    while True:
        for i in xrange(5):
            # result1 = '<xml type="event" name="text" num="' + str(i) + '" attr="******"><x>1</x><y>2</y></xml>'
            # result2 = '<xml type="event" name="func3" num="' + str(i) + '" attr="*"><x>1.10000002384</x><y>6.59999990463</y></xml>'
            result = '<xml type="event" name="main" num="20" attr="*"><c>134</c></xml>'
            print  i, result + '\n'
            if client is not None and i < 10:
                client.sendall(result)
                time.sleep(2.0)
        tcpSocket.close()

if __name__ == "__main__":
    main()