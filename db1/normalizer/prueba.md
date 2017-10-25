# Base de Datos 1
## Práctica 3
### 0)

Se buscand dependencias funcionales en la relacion para luego determinar las claves candidatas, y se encuentran:

**Dependencias funcionales:**
```
df1: {tipoBuque}-->{tonelaje, tipoCasco}
df2: {nombreBuque}-->{tipoBuque}
df3: {dniDueño}-->{nYApDueño}
df4: {puertoOrigen}-->{nombrePaisPuertoOrigen}
df5: {puertoDestino}-->{nomPaísPuertoDestino}
df6: {puertoIntermedio}-->{nombrePaisPuertoIntermedio}
df7: {#Viaje, nombreBuque}-->{puertoOrigen, puertoDestino}
df8: {dniPasajero}-->{nYApPasajero, dirPasajero}
df9: {#Viaje, dniPasajero, nombreBuque}-->{puertoFinalPasajero, puertoInicioPasajero}
df10: {fechaPosicionActual, nombreBuque}-->{posicionActual}
```
**Clave Candidata:**
```
CC: {puertoIntermedio, dniDueño, nombreBuque, #Viaje, dniPasajero, fechaPosicionActual}
```

Se plantea ahora una nueva relacion  `R0`  para realizar el proceso de normalizacion:

```markdown
R0: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, nYApDueño, tipoCasco, posicionActual, nombrePaisPuertoOrigen, tipoBuque, dirPasajero, nomPaísPuertoDestino, puertoDestino, nYApPasajero, tonelaje, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
```

**¿ `R0`  está en bcnf?**
No, exite la dependencia funciona `{tipoBuque}-->{tonelaje, tipoCasco}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R1: (**tipoBuque**, tonelaje, tipoCasco)
```
```markdown
R2: (**puertoIntermedio**, **nombreBuque**, **dniDueño**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, nYApDueño, posicionActual, nombrePaisPuertoOrigen, tipoBuque, dirPasajero, nomPaísPuertoDestino, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
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
```
```markdown
R4: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, nYApDueño, posicionActual, nombrePaisPuertoOrigen, dirPasajero, nomPaísPuertoDestino, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
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
```
```markdown
R6: (**puertoIntermedio**, **nombreBuque**, **dniDueño**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual, nombrePaisPuertoOrigen, dirPasajero, nomPaísPuertoDestino, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
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
```
```markdown
R8: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual, dirPasajero, nomPaísPuertoDestino, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
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
```
```markdown
R10: (**puertoIntermedio**, **nombreBuque**, **dniDueño**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual, dirPasajero, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen, nombrePaisPuertoIntermedio)
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
```
```markdown
R12: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual, dirPasajero, puertoDestino, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero, puertoOrigen)
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
```
```markdown
R14: (**puertoIntermedio**, **nombreBuque**, **dniDueño**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual, dirPasajero, nYApPasajero, puertoFinalPasajero, puertoInicioPasajero)
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
```
```markdown
R16: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, puertoFinalPasajero, puertoInicioPasajero, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R16`  está en bcnf?**
No, exite la dependencia funciona `{#Viaje, dniPasajero, nombreBuque}-->{puertoFinalPasajero, puertoInicioPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R17: (**#Viaje**, **dniPasajero**, **nombreBuque**, puertoFinalPasajero, puertoInicioPasajero)
```
```markdown
R18: (**puertoIntermedio**, **nombreBuque**, **dniDueño**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**, posicionActual)
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
```
```markdown
R20: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


El esquema final en en bcnf sera:

```markdown
R1: (**tipoBuque**, tonelaje, tipoCasco)
```
```markdown
R3: (**nombreBuque**, tipoBuque)
```
```markdown
R5: (**dniDueño**, nYApDueño)
```
```markdown
R7: (**puertoOrigen**, nombrePaisPuertoOrigen)
```
```markdown
R9: (**puertoDestino**, nomPaísPuertoDestino)
```
```markdown
R11: (**puertoIntermedio**, nombrePaisPuertoIntermedio)
```
```markdown
R13: (**#Viaje**, **nombreBuque**, puertoOrigen, puertoDestino)
```
```markdown
R15: (**dniPasajero**, nYApPasajero, dirPasajero)
```
```markdown
R17: (**#Viaje**, **dniPasajero**, **nombreBuque**, puertoFinalPasajero, puertoInicioPasajero)
```
```markdown
R19: (**fechaPosicionActual**, **nombreBuque**, posicionActual)
```
```markdown
R20: (**puertoIntermedio**, **dniDueño**, **nombreBuque**, **#Viaje**, **dniPasajero**, **fechaPosicionActual**)
```
