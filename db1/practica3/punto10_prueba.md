# Base de Datos 1
## Práctica 3
### 0)

Se buscand dependencias funcionales en la relacion para luego determinar las claves candidatas, y se encuentran:

**Dependencias funcionales:**
```
df1: {#Agencia}-->{nombreAgencia}
df2: {dniPasajero}-->{telPasajero, nombrePasajero}
df3: {#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}
df4: {#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}
df5: {#Reserva, nombreAerolínea}-->{#Agencia}
df6: {#Vuelo, nombreAerolínea}-->{horaLlegada, ciudadDestino, modeloAvión, ciudadOrigen, horaPartida}
df7: {#Reserva, dniPasajero, nombreAerolínea}-->{dirPasajero}
```
**Clave Candidata:**
```
CC: {dniPasajero, #Reserva, tipoComida, telCompañía, compañíaPasajero, #Vuelo, dirCompañía, nombreAerolínea}
```

Se plantea ahora una nueva relacion  `R0`  para realizar el proceso de normalizacion:

```markdown
R0: (**dniPasajero**, **#Reserva**, **tipoComida**, **telCompañía**, **compañíaPasajero**, **#Vuelo**, **dirCompañía**, **nombreAerolínea**, horaPartida, fechaPartida, horaLlegada, #Asiento, dirPasajero, fechaLlegada, ciudadDestino, #Agencia, modeloAvión, nombreAgencia, ciudadOrigen, fechaReservaVuelo, telPasajero, nombrePasajero, tipoPago, clase)
```

**¿ `R0`  está en bcnf?**
No, exite la dependencia funciona `{#Agencia}-->{nombreAgencia}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R1: (**#Agencia**, nombreAgencia)
R2: (**dniPasajero**, **tipoComida**, **telCompañía**, **nombreAerolínea**, **compañíaPasajero**, **dirCompañía**, **#Reserva**, **#Vuelo**, horaPartida, fechaPartida, horaLlegada, #Asiento, dirPasajero, fechaLlegada, ciudadDestino, #Agencia, modeloAvión, ciudadOrigen, fechaReservaVuelo, telPasajero, nombrePasajero, tipoPago, clase)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R2`  está en bcnf?**
No, exite la dependencia funciona `{dniPasajero}-->{telPasajero, nombrePasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R3: (**dniPasajero**, nombrePasajero, telPasajero)
R4: (**dniPasajero**, **#Reserva**, **tipoComida**, **telCompañía**, **compañíaPasajero**, **#Vuelo**, **dirCompañía**, **nombreAerolínea**, horaPartida, fechaPartida, horaLlegada, #Asiento, dirPasajero, fechaLlegada, ciudadDestino, #Agencia, modeloAvión, ciudadOrigen, fechaReservaVuelo, tipoPago, clase)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R4`  está en bcnf?**
No, exite la dependencia funciona `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R5: (**#Reserva**, **#Vuelo**, **nombreAerolínea**, fechaReservaVuelo, fechaPartida, fechaLlegada, clase)
R6: (**dniPasajero**, **tipoComida**, **telCompañía**, **nombreAerolínea**, **compañíaPasajero**, **dirCompañía**, **#Reserva**, **#Vuelo**, horaPartida, horaLlegada, #Asiento, dirPasajero, ciudadDestino, #Agencia, modeloAvión, ciudadOrigen, tipoPago)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R6`  está en bcnf?**
No, exite la dependencia funciona `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R7: (**#Reserva**, **dniPasajero**, **#Vuelo**, **nombreAerolínea**, tipoPago, #Asiento)
R8: (**dniPasajero**, **#Reserva**, **tipoComida**, **telCompañía**, **compañíaPasajero**, **#Vuelo**, **dirCompañía**, **nombreAerolínea**, horaLlegada, dirPasajero, ciudadDestino, #Agencia, modeloAvión, ciudadOrigen, horaPartida)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R8`  está en bcnf?**
No, exite la dependencia funciona `{#Reserva, nombreAerolínea}-->{#Agencia}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R9: (**#Reserva**, **nombreAerolínea**, #Agencia)
R10: (**dniPasajero**, **#Reserva**, **tipoComida**, **telCompañía**, **compañíaPasajero**, **#Vuelo**, **dirCompañía**, **nombreAerolínea**, horaLlegada, dirPasajero, ciudadDestino, modeloAvión, ciudadOrigen, horaPartida)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R10`  está en bcnf?**
No, exite la dependencia funciona `{#Vuelo, nombreAerolínea}-->{horaLlegada, ciudadDestino, modeloAvión, ciudadOrigen, horaPartida}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R11: (**#Vuelo**, **nombreAerolínea**, horaLlegada, ciudadDestino, modeloAvión, ciudadOrigen, horaPartida)
R12: (**dniPasajero**, **tipoComida**, **telCompañía**, **nombreAerolínea**, **compañíaPasajero**, **dirCompañía**, **#Reserva**, **#Vuelo**, dirPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


**¿ `R12`  está en bcnf?**
No, exite la dependencia funciona `{#Reserva, dniPasajero, nombreAerolínea}-->{dirPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R13: (**#Reserva**, **dniPasajero**, **nombreAerolínea**, dirPasajero)
R14: (**dniPasajero**, **tipoComida**, **telCompañía**, **nombreAerolínea**, **compañíaPasajero**, **dirCompañía**, **#Reserva**, **#Vuelo**)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{#Reserva, #Vuelo, nombreAerolínea}-->{fechaReservaVuelo, fechaPartida, fechaLlegada, clase}` `{#Reserva, dniPasajero, #Vuelo, nombreAerolínea}-->{tipoPago, #Asiento}`


El esquema final en en bcnf sera:


```markdown
R1: (**#Agencia**, nombreAgencia)
R3: (**dniPasajero**, nombrePasajero, telPasajero)
R5: (**#Reserva**, **#Vuelo**, **nombreAerolínea**, fechaReservaVuelo, fechaPartida, fechaLlegada, clase)
R7: (**#Reserva**, **dniPasajero**, **#Vuelo**, **nombreAerolínea**, tipoPago, #Asiento)
R9: (**#Reserva**, **nombreAerolínea**, #Agencia)
R11: (**#Vuelo**, **nombreAerolínea**, horaLlegada, ciudadDestino, modeloAvión, ciudadOrigen, horaPartida)
R13: (**#Reserva**, **dniPasajero**, **nombreAerolínea**, dirPasajero)
R14: (**dniPasajero**, **tipoComida**, **telCompañía**, **nombreAerolínea**, **compañíaPasajero**, **dirCompañía**, **#Reserva**, **#Vuelo**)
```

