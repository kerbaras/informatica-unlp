# Base de Datos 1
## Práctica 3
### 0)

Se buscand dependencias funcionales en la relacion para luego determinar las claves candidatas, y se encuentran:

**Dependencias funcionales:**
```
df1: {tipoBuque}-->{tipoCasco, tonelaje}
df2: {nombreBuque}-->{tipoBuque}
df3: {dniDueño}-->{nYApDueño}
df4: {nombreBuque, #Viaje}-->{puertoOrigen, puertoDestino}
df5: {puertoOrigen}-->{nombrePaisPuertoOrigen}
df6: {puertoDestino}-->{nomPaísPuertoDestino}
df7: {puertoIntermedio}-->{nombrePaisPuertoIntermedio}
df8: {dniPasajero}-->{nYApPasajero, dirPasajero}
df9: {nombreBuque, dniPasajero, #Viaje}-->{puertoInicioPasajero, puertoFinalPasajero}
df10: {fechaPosicionActual, nombreBuque}-->{posicionActual}
```
**Clave Candidata:**
```
CC: {dniPasajero, puertoIntermedio, #Viaje, fechaPosicionActual, nombreBuque, dniDueño}
```

Se plantea ahora una nueva relacion  `R0`  para realizar el proceso de normalizacion:

```markdown
R0: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, puertoOrigen, tipoCasco, tonelaje, puertoDestino, nYApDueño, nombrePaisPuertoOrigen, dirPasajero, nombrePaisPuertoIntermedio, nYApPasajero, tipoBuque, nomPaísPuertoDestino, posicionActual)
```

**¿ `R0`  está en bcnf?**
No, exite la dependencia funciona `{tipoBuque}-->{tipoCasco, tonelaje}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R1: (**tipoBuque**, tipoCasco, tonelaje)
```
```markdown
R2: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, puertoOrigen, nombrePaisPuertoOrigen, puertoDestino, nYApDueño, dirPasajero, nombrePaisPuertoIntermedio, nYApPasajero, tipoBuque, nomPaísPuertoDestino, posicionActual)
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
R4: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, puertoOrigen, nombrePaisPuertoOrigen, puertoDestino, dirPasajero, nYApDueño, nombrePaisPuertoIntermedio, nYApPasajero, nomPaísPuertoDestino, posicionActual)
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
R6: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, puertoOrigen, nombrePaisPuertoOrigen, puertoDestino, dirPasajero, nombrePaisPuertoIntermedio, nYApPasajero, nomPaísPuertoDestino, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
No se perdio ninguna dependencia funcional


**¿ `R6`  está en bcnf?**
No, exite la dependencia funciona `{nombreBuque, #Viaje}-->{puertoOrigen, puertoDestino}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R7: (**nombreBuque**, **#Viaje**, puertoOrigen, puertoDestino)
```
```markdown
R8: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, nombrePaisPuertoOrigen, dirPasajero, nombrePaisPuertoIntermedio, nYApPasajero, nomPaísPuertoDestino, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{puertoOrigen}-->{nombrePaisPuertoOrigen}` `{puertoDestino}-->{nomPaísPuertoDestino}`


**¿ `R8`  está en bcnf?**
No, exite la dependencia funciona `{puertoIntermedio}-->{nombrePaisPuertoIntermedio}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R9: (**puertoIntermedio**, nombrePaisPuertoIntermedio)
```
```markdown
R10: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, dirPasajero, nombrePaisPuertoOrigen, nYApPasajero, nomPaísPuertoDestino, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{puertoOrigen}-->{nombrePaisPuertoOrigen}` `{puertoDestino}-->{nomPaísPuertoDestino}`


**¿ `R10`  está en bcnf?**
No, exite la dependencia funciona `{dniPasajero}-->{nYApPasajero, dirPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R11: (**dniPasajero**, nYApPasajero, dirPasajero)
```
```markdown
R12: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, puertoInicioPasajero, puertoFinalPasajero, nombrePaisPuertoOrigen, nomPaísPuertoDestino, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{puertoOrigen}-->{nombrePaisPuertoOrigen}` `{puertoDestino}-->{nomPaísPuertoDestino}`


**¿ `R12`  está en bcnf?**
No, exite la dependencia funciona `{nombreBuque, dniPasajero, #Viaje}-->{puertoInicioPasajero, puertoFinalPasajero}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R13: (**nombreBuque**, **dniPasajero**, **#Viaje**, puertoInicioPasajero, puertoFinalPasajero)
```
```markdown
R14: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, nomPaísPuertoDestino, nombrePaisPuertoOrigen, posicionActual)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{puertoOrigen}-->{nombrePaisPuertoOrigen}` `{puertoDestino}-->{nomPaísPuertoDestino}`


**¿ `R14`  está en bcnf?**
No, exite la dependencia funciona `{fechaPosicionActual, nombreBuque}-->{posicionActual}` que no es trivail ni superclave
Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl

Se proponen los siguientes esquemas:

```markdown
R15: (**fechaPosicionActual**, **nombreBuque**, posicionActual)
```
```markdown
R16: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, nomPaísPuertoDestino, nombrePaisPuertoOrigen)
```

**a) ¿Perdí información?**
No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional

**b) ¿Perdí dependencias funcionales?**
Si, se perdieron las dependencias funcionales: `{puertoOrigen}-->{nombrePaisPuertoOrigen}` `{puertoDestino}-->{nomPaísPuertoDestino}`


El esquema final en en bcnf sera:

```markdown
R1: (**tipoBuque**, tipoCasco, tonelaje)
```
```markdown
R3: (**nombreBuque**, tipoBuque)
```
```markdown
R5: (**dniDueño**, nYApDueño)
```
```markdown
R7: (**nombreBuque**, **#Viaje**, puertoOrigen, puertoDestino)
```
```markdown
R9: (**puertoIntermedio**, nombrePaisPuertoIntermedio)
```
```markdown
R11: (**dniPasajero**, nYApPasajero, dirPasajero)
```
```markdown
R13: (**nombreBuque**, **dniPasajero**, **#Viaje**, puertoInicioPasajero, puertoFinalPasajero)
```
```markdown
R15: (**fechaPosicionActual**, **nombreBuque**, posicionActual)
```
```markdown
R16: (**dniPasajero**, **puertoIntermedio**, **#Viaje**, **fechaPosicionActual**, **nombreBuque**, **dniDueño**, nomPaísPuertoDestino, nombrePaisPuertoOrigen)
```
