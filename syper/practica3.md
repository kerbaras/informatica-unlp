# Practica 3

## Seguridad y Privacidad en Redes

### Ataques contra la confidencialidad e integridad de la información

1. Para cada una de las siguientes situaciones identifique la información que corre riesgo de
   perder su confidencialidad:
   - Olvidar mi celular en lo de un amigo
   - Perder el celular
   - Perder la notebook:
     - Fotos
     - Contactos
     - E-mails
     - Contraseñas
     - Basicamente tu vida
   - Presencia de un visitante ocasional en la oficina en la que trabajo:
     - Documentos importantes y privados
     - Conversaciones clasificadas de la organización
   - Uso ocasional de una PC que posiblemente esté infectada con algún malware:
     - Todo, desde contraseñas, hasta conversaciones y fotos
   - Uso de correo institucional utilizando POP3 e IMAP: 
     - Correo con informacion sensible (horarios, reuniones, conversaciones, contraseñas)
   - Acceso a sitio WEB para compras online a través de HTTP: 
     - Información de tarjetas (Número, Vencimiento, CVC)
     - Información personal sensible (Dirección, DNI, Teléfono)
     - Credenciales

2. Para cada una de las situaciones del ejercicio 1: ¿Qué contramedidas se podrían llevar a cabo para minimizar el riesgo?

3. ¿Qué es un sniffer? Un analizador de protocolos, ¿puede ser usado como sniffer?

   En informática, un Sniffer es un programa de captura de las tramas de una red de computadoras con el fin de observar su contenido.

   Un analizador de protocolos puede ser considerado como sniffer, cuando este se usa para espiar el tráfico de la red.

4. ¿En cuáles de las situaciones del ejercicio 1 tiene sentido el uso de un sniffer?
   - Olvidar mi celular en lo de un amigo: NO
   - Perder el celular: NO
   - Perder la notebook: NO
   - Presencia de un visitante ocasional en la oficina en la que trabajo: NO
   - Uso ocasional de una PC que posiblemente esté infectada con algún malware: NO
   - Uso de correo institucional utilizando POP3 e IMAP: SI
   - Acceso a sitio WEB para compras online a través de HTTP: SI 

5. ¿Que es MITM? ¿Todos los sniffing requieren de un MITM? 
   Man-in-the-middle (MITM) is an attack where the attacker secretly relays and possibly alters the communication between two parties who believe they are directly communicating with each other.

   No, algunos sniffing no requieren de un MITM, ya que la topologia de su red les permite interceptar el tráfico usando su placa de red en modo promiscuo (Usualmente tramas conectadas a un Hub).

### Conceptos generales de redes y servicios de red

6. Para realizar un ataque de sniffing, se pueden intentar distintas alternativas. Analice en cada una de las opciones, de que manera se logra el sniffing identificando cuál sería el dispositivo engañado (PC, SWITCH o ROUTER).
   - Enviando tramas Ethernet con direcciones MAC origen spoofeadas (MAC Spoofing): SWITCH
   - Inundando la red con tramas Ethernet con MACs origen aleatorias (MAC Flooding): SWITCH
   - Enviando respuestas ARP falsas (ARP Spoofing): PC
   - Enviando paquetes ICMP-REDIRECTs falsos (ICMP-REDIRECT attack): ROUTER

### Sniffing en una red switcheada

7. Cree una topología como la siguiente para realizar distintos tipos de ataques de sniffing:

![Topología de la red a atacar](https://raw.githubusercontent.com/matias-pierobon/informatica-unlp/master/syper/p3-Topologia.png)
