# port-scanner-automation

Simple Python port scanner with multi-threading made for VM testing and labs.

## Requirements
* Python 3.x
* Built-in Python modules (`socket`, `concurrent.futures`)

## How to run
```bash
python scanner.py
```

## How I Tested (My Lab Scenario)
1. Started a target Virtual Machine (VM).
2. Opened port 8000 on the VM (e.g., running `python3 -m http.server 8000`).
3. Got the VM's IP address.
4. Pasted the IP inside the script on my host machine.
5. Ran the script to successfully detect the open port.

## Disclaimer
Educational and local lab use only.
