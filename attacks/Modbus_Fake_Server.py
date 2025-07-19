from modbus_tk import modbus_tcp
from modbus_tk import defines as cst
import time

server = modbus_tcp.TcpServer()
server.start()
slave = server.add_slave(1)
slave.add_block('0', cst.HOLDING_REGISTERS, 0, 100)
slave.set_values('0', 0, [20, 30, 40, 50])

print("[+] Fake Modbus TCP Server running on 127.0.0.1:502")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("[!] Stopping server")
    server.stop()
