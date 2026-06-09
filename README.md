# Informe Técnico: Implementación y Auditoría - Transporte Lacustre SA

## 1. Objetivo del proyecto
El objetivo de este proyecto fue automatizar el aprovisionamiento de un nuevo router corporativo para Transporte Lacustre SA mediante herramientas de infraestructura como código. Se buscó garantizar una configuración estandarizada, validando su cumplimiento a través de auditorías independientes.

## 2. Alcance
Se automatizó la configuración de interfaces de red, parámetros de seguridad (banner), identificación corporativa, sincronización de tiempo y habilitación de APIs de gestión remota. Quedó fuera de alcance la implementación de protocolos de enrutamiento dinámico y políticas de firewall.

## 3. Infraestructura utilizada
- Estación de trabajo: DEVASC VM ejecutando Linux.
- Dispositivo administrado: Cisco CSR1kv ejecutando Cisco IOS-XE.
- Herramientas: Ansible (aprovisionamiento), pyATS/Genie (auditoría de estado), Python con ncclient y requests (validación de APIs).

## 4. Tecnologías empleadas y justificación
- **pyATS / Genie:** Se utilizó para crear instantáneas agnósticas (baselines) del estado operativo del router, permitiendo comparar el antes y el después.
- **Ansible:** Empleado en la fase de aprovisionamiento por su enfoque declarativo, garantizando consistencia en múltiples ejecuciones.
- **NETCONF:** Se usó para auditar la configuración del equipo obteniendo el modelo YANG en formato estructurado (XML).
- **RESTCONF:** Seleccionado para validar parámetros atómicos mediante peticiones HTTP estructuradas en JSON.

## 5. Configuración aplicada
- **Hostname:** RTR-TRANLAC
- **IP Loopback 10:** 10.5.19.1 / 255.255.255.0
- **Descripción GigabitEthernet1:** Enlace-WAN-Curico
- **Banner MOTD:** ACCESO RESTRINGIDO - TRANLAC
- **Servidor NTP:** 9.9.9.9

## 6. Resultados de validación
- Hostname vía RESTCONF: CONFORME
- Interfaz Loopback vía RESTCONF: CONFORME
- Descripción WAN vía RESTCONF: CONFORME
- Servidor NTP vía RESTCONF: CONFORME
- Auditoría global NETCONF: CONFORME

## 7. Conclusiones
El dispositivo fue aprovisionado exitosamente cumpliendo al 100% con los requerimientos técnicos de Transporte Lacustre SA. Las verificaciones automáticas certifican que el router RTR-TRANLAC está apto para operaciones.
