```
RESERVA (#Reserva, #Agencia, nombreAgencia, fechaReservaVuelo, ciudadOrigen, ciudadDestino, tipoPago, nombreAerolínea, #Vuelo, dniPasajero, nombrePasajero, dirPasajero, telPasajero, clase, fechaPartida, fechaLlegada, horaPartida, horaLlegada, modeloAvión, #Asiento, tipoComida, compañíaPasajero, dirCompañía, telCompañía)
```

```
#Agencia --> nombreAgencia
dniPasajero --> nombrePasajero, telPasajero
nombreAerolínea, #Reserva, #Vuelo --> clase, fechaReservaVuelo, fechaPartida, fechaLlegada
nombreAerolínea, #Reserva, #Vuelo, dniPasajero --> tipoPago, #Asiento
nombreAerolínea, #Reserva --> #Agencia
nombreAerolínea, #Vuelo --> modeloAvión, ciudadOrigen, horaPartida, ciudadDestino, horaLlegada
nombreAerolínea, #Reserva, dniPasajero --> dirPasajero
```

```
CC: (nombreAerolínea, #Reserva, #Vuelo, dniPasajero, tipoComida, compañíaPasajero, dirCompañía, telCompañía)
```

```markdown
(**#Agencia**, nombreAgencia)
(**dniPasajero**, nombrePasajero, telPasajero)
(**nombreAerolínea**, **#Reserva**, **#Vuelo**, clase, fechaReservaVuelo, fechaPartida,fechaLlegada)
(**nombreAerolínea**, **#Reserva**, **#Vuelo**, **dniPasajero**, tipoPago, #Asiento)
(**nombreAerolínea**, **#Reserva**, #Agencia)
(**nombreAerolínea**, **#Vuelo**, modeloAvión, ciudadOrigen, horaPartida, ciudadDestino,horaLlegada)
(**nombreAerolínea**, **#Reserva**, **dniPasajero**, dirPasajero)

(**nombreAerolínea**, **#Reserva**, **#Vuelo**, **dniPasajero**, **tipoComida**, **compañíaPasajero**, **dirCompañía**, **telCompañía**)
```

```
nombreAerolínea, #Vuelo -->> tipoComida

```

```markdown
(**nombreAerolínea**, **#Vuelo**, **tipoComida**)

(**nombreAerolínea**, **#Reserva**, **#Vuelo**, **dniPasajero**, **compañíaPasajero**, **dirCompañía**, **telCompañía**)
```

```markdown

```