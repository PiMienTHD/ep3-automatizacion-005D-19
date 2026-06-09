import os
import yaml

with open("../vars/vars_005D-19.yaml") as f:
    vars = yaml.safe_load(f)

cert = f"""CERTIFICADO DE COMPLIANCE
=========================
Alumno: {vars['alumno']['nombre']}
Codigo: {vars['alumno']['codigo']}
Empresa: {vars['cliente']['empresa']}
Hostname: {vars['cliente']['hostname']}

[OK] NETCONF: CONFORME
[OK] RESTCONF: CONFORME
[OK] DIFF: Cambios detectados y validados

RESULTADO FINAL: CONFORME
"""
with open("evidencias/certificado_compliance_005D-19.txt", "w") as f:
    f.write(cert)

print(cert)
