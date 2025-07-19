# ICS Attacks Project – DoS & Modbus TCP Read Attack

This project demonstrates **two common attacks** against Industrial Control Systems (ICS):

1. **Application-layer DoS attack** (Slowloris) against an HTTP server
2. **Modbus TCP Read attack** targeting insecure PLC communication

> Implemented in Python  

---

## Project Structure

```
ics-attacks-project/
├── attacks/
│   ├── modbus_read_attack.py         ← Unauthorized Modbus client
│   ├── slowloris_attack.py           ← HTTP Slowloris DoS attack
│   └── Modbus_Fake_Server.py         ← Fake Modbus server 
│
├── docs/
│   ├── Report_attaqueDoS.txt          ← Full DoS attack summary
│   ├── Report_Modbus.txt              ← Full Modbus attack summary
|   ├── Modbus_attack/
│       ├── Modbus_Attack.PNG             ← Screenshot: Modbus attack client
│       └── Modbus_proof.PNG              ← Screenshot: proof of register read
|   └──  Slowloris_attack/
│       ├── Wireshark_Slowloris_attack_tcp_8080.PNG
│       ├── Before_Slowloris.PNG          ← Normal latency
│       └── during_slowloris.PNG          ← Latency during attack
│
├── README.md                         
└── requirements.txt                  ← Required libraries
```

---

## Attack 1 – HTTP DoS using Slowloris

### Objective
Send hundreds of slow connections to block the HTTP server.

### Setup
1. Start a vulnerable HTTP server ( `python -m http.server 8080`) 'if you choose to change the port , change it also in `attacks/slowloris_attack.py` '
2. Run the script:
```bash
python attacks/slowloris_attack.py
```

See:
- `Before_Slowloris.PNG`
- `during_slowloris.PNG`
- `Screenshot_Slowloris_attack_tcp_8080.PNG`

Full summary: `docs/Report_attaqueDoS.txt`

---
## Attack 2 – Unauthorized Modbus TCP Read

### Objective
Read Modbus registers from a simulated server without any authentication.

### Setup
1. Start the fake server:
```bash
python attacks/Modbus_Fake_Server.py
```

2. Launch the attack:
```bash
python attacks/modbus_read_attack.py
```

See screenshots:
- `Modbus_Attack.PNG` → running the script
- `Modbus_proof.PNG` → values read: `[20, 30, 40, 50]`

Full summary: `docs/Report_Modbus.txt`

---


## Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Libraries used:
- `pymodbus`
- `modbus-tk`


---

## Authors

- Kadri Ikram
- Houacine Yousra  
- Aissani Yudas Rafik 