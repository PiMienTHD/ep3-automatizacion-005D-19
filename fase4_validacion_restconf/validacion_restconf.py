import requests
import yaml
import json
import urllib3
import datetime
import socket
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print(f"=== REPORTE RESTCONF ===")
print(f"Script: validacion_restconf.py")
print(f"Fecha: {datetime.datetime.now()}")
print(f"Host: {socket.gethostname()}\n")

with open("../vars/vars_005D-19.yaml") as f:
    vars = yaml.safe_load(f)

base_url = f"https://{vars['router']['ip']}/restconf/data"
auth = (vars['router']['usuario'], vars['router']['password'])
headers = {"Accept": "application/yang-data+json"}

endpoints = {
    "Hostname": ("/Cisco-IOS-XE-native:native/hostname", "evidencias/responses/get_hostname.json", vars['cliente']['hostname']),
    "Loopback": (f"/ietf-interfaces:interfaces/interface=Loopback{vars['router']['loopback_id']}", "evidencias/responses/get_loopback.json", vars['router']['loopback_ip']),
    "Interfaces": ("/ietf-interfaces:interfaces/interface=GigabitEthernet1", "evidencias/responses/get_interfaces.json", vars['router']['descripcion_wan']),
    "NTP": ("/Cisco-IOS-XE-native:native/ntp", "evidencias/responses/get_ntp.json", vars['router']['ntp_server'])
}

ok_count = 0
for name, (url, filepath, expected) in endpoints.items():
    try:
        resp = requests.get(base_url + url, auth=auth, headers=headers, verify=False)
        data = resp.json()
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        
        if expected in json.dumps(data):
            print(f"[OK] {name}")
            ok_count += 1
        else:
            print(f"[FAIL] {name}")
    except Exception as e:
         print(f"[FAIL] {name} - Error: {e}")

if ok_count == 4:
    print("\nRESULTADO GLOBAL: CONFORME")
else:
    print("\nRESULTADO GLOBAL: NO CONFORME")
