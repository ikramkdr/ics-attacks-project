from pymodbus.client import ModbusTcpClient
import sys

print("Python version:", sys.version)

ip = "127.0.0.1"
port = 502

client = ModbusTcpClient(host=ip, port=port)
if client.connect():
    print("[+] Connected to Modbus server!")

    # reading 4 registers(unit ID = 1)
    response = client.read_holding_registers(address=0, count=4, slave=1)

    if response.isError():
        print("[!] Failed to read registers.")
    else:
        print("[+] Registers read successfully:")
        print("    Values:", response.registers)

    client.close()
else:
    print("[!] Failed to connect to Modbus server.")
