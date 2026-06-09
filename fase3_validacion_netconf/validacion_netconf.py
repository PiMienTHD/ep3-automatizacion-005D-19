import yaml
from ncclient import manager
import datetime
import socket

print(f"=== REPORTE NETCONF ===")
print(f"Script: validacion_netconf.py")
print(f"Fecha: {datetime.datetime.now()}")
print(f"Host: {socket.gethostname()}\n")

with open("../vars/vars_005D-19.yaml") as f:
    vars = yaml.safe_load(f)

filter_xml = '''<filter><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"></native></filter>'''

try:
    with manager.connect(host=vars['router']['ip'], port=830, username=vars['router']['usuario'], password=vars['router']['password'], hostkey_verify=False, look_for_keys=False, allow_agent=False) as m:
        netconf_reply = m.get_config(source='running', filter=filter_xml)
        xml_data = netconf_reply.xml
        
        with open("evidencias/rpc_reply_raw.xml", "w") as f:
            f.write(xml_data)

    criterios = [
        ("Hostname", vars['cliente']['hostname']),
        ("Loopback IP", vars['router']['loopback_ip']),
        ("Loopback Mask", vars['router']['loopback_mask']),
        ("Descripcion WAN", vars['router']['descripcion_wan']),
        ("Servidor NTP", vars['router']['ntp_server'])
    ]
    
    ok_count = 0
    for name, value in criterios:
        if value in xml_data:
            print(f"[OK] {name}: {value}")
            ok_count += 1
        else:
            print(f"[FAIL] {name}: {value} no encontrado en XML")
            
    if ok_count == 5:
        print("\nRESULTADO GLOBAL: CONFORME")
    else:
        print("\nRESULTADO GLOBAL: NO CONFORME")
        
except Exception as e:
    print(f"Error de conexion NETCONF: {e}")
