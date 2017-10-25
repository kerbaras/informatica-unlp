# Base de Datos 1
## Práctica 3
### 0)

Se buscand dependencias funcionales en la relacion para luego determinar las claves candidatas, y se encuentran:

**Dependencias funcionales:**
```
df1: {tipoBuque}-->{tipoCasco, tonelaje}
df2: {nombreBuque}-->{tipoBuque}
df3: {dniDueño}-->{nYApDueño}
df4: {puertoOrigen}-->{nombrePaisPuertoOrigen}
df5: {puertoDestino}-->{nomPaísPuertoDestino}
df6: {puertoIntermedio}-->{nombrePaisPuertoIntermedio}
df7: {#Viaje, nombreBuque}-->{puertoOrigen, puertoDestino}
df8: {dniPasajero}-->{nYApPasajero, dirPasajero}
df9: {dniPasajero, #Viaje, nombreBuque}-->{puertoInicioPasajero, puertoFinalPasajero}
df10: {fechaPosicionActual, nombreBuque}-->{posicionActual}
```
**Clave Candidata:**
```
CC: {dniDueño, #Viaje, dniPasajero, puertoIntermedio, fechaPosicionActual, nombreBuque}
```

Se plantea ahora una nueva relacion  `R0`  para realizar el proceso de normalizacion:

```markdown
R0: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, nombrePaisPuertoOrigen, puertoInicioPasajero, dirPasajero, posicionActual, puertoFinalPasajero, nombrePaisPuertoIntermedio, puertoDestino, nomPaísPuertoDestino, tonelaje, tipoBuque, puertoOrigen, nYApPasajero, nYApDueño, tipoCasco)
```

**¿ `R0`  está en bcnf?**
No, exite la dependencia funciona `{tipoBuque}-->{tipoCasco, tonelaje}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R1: (**tipoBuque**, tipoCasco, tonelaje)
R2: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, nombrePaisPuertoOrigen, puertoFinalPasajero, dirPasajero, posicionActual, puertoInicioPasajero, nombrePaisPuertoIntermedio, puertoDestino, nomPaísPuertoDestino, tipoBuque, puertoOrigen, nYApPasajero, nYApDueño)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R2`  está en bcnf?**
No, exite la dependencia funciona `{nombreBuque}-->{tipoBuque}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R3: (**nombreBuque**, tipoBuque)
R4: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, nombrePaisPuertoOrigen, puertoFinalPasajero, dirPasajero, posicionActual, puertoInicioPasajero, nombrePaisPuertoIntermedio, puertoDestino, nomPaísPuertoDestino, puertoOrigen, nYApPasajero, nYApDueño)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R4`  está en bcnf?**
No, exite la dependencia funciona `{dniDueño}-->{nYApDueño}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R5: (**dniDueño**, nYApDueño)
R6: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, nombrePaisPuertoOrigen, puertoFinalPasajero, dirPasajero, posicionActual, puertoInicioPasajero, nombrePaisPuertoIntermedio, puertoDestino, nomPaísPuertoDestino, puertoOrigen, nYApPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R6`  está en bcnf?**
No, exite la dependencia funciona `{puertoOrigen}-->{nombrePaisPuertoOrigen}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R7: (**puertoOrigen**, nombrePaisPuertoOrigen)
R8: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, puertoFinalPasajero, dirPasajero, posicionActual, puertoInicioPasajero, nombrePaisPuertoIntermedio, puertoDestino, nomPaísPuertoDestino, puertoOrigen, nYApPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R8`  está en bcnf?**
No, exite la dependencia funciona `{puertoDestino}-->{nomPaísPuertoDestino}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R9: (**puertoDestino**, nomPaísPuertoDestino)
R10: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, dirPasajero, puertoInicioPasajero, puertoFinalPasajero, posicionActual, nombrePaisPuertoIntermedio, puertoDestino, puertoOrigen, nYApPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R10`  está en bcnf?**
No, exite la dependencia funciona `{puertoIntermedio}-->{nombrePaisPuertoIntermedio}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R11: (**puertoIntermedio**, nombrePaisPuertoIntermedio)
R12: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, dirPasajero, puertoInicioPasajero, puertoFinalPasajero, posicionActual, puertoDestino, puertoOrigen, nYApPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R12`  está en bcnf?**
No, exite la dependencia funciona `{#Viaje, nombreBuque}-->{puertoOrigen, puertoDestino}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R13: (**#Viaje**, **nombreBuque**, puertoOrigen, puertoDestino)
R14: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, dirPasajero, puertoInicioPasajero, puertoFinalPasajero, posicionActual, nYApPasajero)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R14`  está en bcnf?**
No, exite la dependencia funciona `{dniPasajero}-->{nYApPasajero, dirPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R15: (**dniPasajero**, nYApPasajero, dirPasajero)
R16: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, puertoInicioPasajero, puertoFinalPasajero, posicionActual)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R16`  está en bcnf?**
No, exite la dependencia funciona `{dniPasajero, #Viaje, nombreBuque}-->{puertoInicioPasajero, puertoFinalPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R17: (**dniPasajero**, **#Viaje**, **nombreBuque**, puertoInicioPasajero, puertoFinalPasajero)
R18: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**, posicionActual)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R18`  está en bcnf?**
No, exite la dependencia funciona `{fechaPosicionActual, nombreBuque}-->{posicionActual}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:


```markdown
R19: (**fechaPosicionActual**, **nombreBuque**, posicionActual)
R20: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**)
```


**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


El esquema final en en bcnf sera:


```markdown
R1: (**tipoBuque**, tipoCasco, tonelaje)
R3: (**nombreBuque**, tipoBuque)
R5: (**dniDueño**, nYApDueño)
R7: (**puertoOrigen**, nombrePaisPuertoOrigen)
R9: (**puertoDestino**, nomPaísPuertoDestino)
R11: (**puertoIntermedio**, nombrePaisPuertoIntermedio)
R13: (**#Viaje**, **nombreBuque**, puertoOrigen, puertoDestino)
R15: (**dniPasajero**, nYApPasajero, dirPasajero)
R17: (**dniPasajero**, **#Viaje**, **nombreBuque**, puertoInicioPasajero, puertoFinalPasajero)
R19: (**fechaPosicionActual**, **nombreBuque**, posicionActual)
R20: (**dniDueño**, **#Viaje**, **dniPasajero**, **puertoIntermedio**, **fechaPosicionActual**, **nombreBuque**)
```

