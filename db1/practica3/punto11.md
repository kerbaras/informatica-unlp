### 11)

```
BUQUE (nombreBuque, nYApDueño, dniDueño, tipoBuque, tonelaje, tipoCasco, #Viaje, puertoOrigen,
puertoDestino puertoIntermedio, nomPaísPuertoDestino, nombrePaisPuertoOrigen,
nombrePaisPuertoIntermedio, posicionActual, fechaPosicionActual, nYApPasajero, dniPasajero, dirPasajero,
puertoInicioPasajero, puertoFinalPasajero)
```

**Donde:**

- El #Viaje es un número consecutivo que identifica cada partida de cada buque.
- Un buque hace varios viajes. El #Viaje se puede repetir para distintos buques
- Un buque puede tener varios dueños.
- El nombre del buque es único. Un nombreBuque se asocia a un tipo de buque.
- El tonelaje y el casco están determinados por el tipo de buque.
- Un buque reporta su posición una vez por día independientemente del viaje.
- Cada viaje de un buque tiene un puerto origen, un puerto destino y varios puertos intermedios.
- Un buque en su viaje puede pasar por varios puertos intermedios sin repetirlos.
- Un pasajero tiene una única dirección independientemente del viaje.
- Un pasajero tiene un único puerto origen y puerto destino por cada viaje de un buque.

#### Resoulción

Se buscand dependencias funcionales en `BUQUE` para luego determinar las claves candidatas, y se encuentran:

**Dependencias funcionales:**
```
df1:  nombreBuque --> tipoBuque
df2:  tipoBuque --> tonelaje, tipoCasco
df3:  dniDueño --> nYApDueño
df4:  nombreBuque, #Viaje --> puertoOrigen, puertoDestino
df5:  puertoOrigen --> nombrePaisPuertoOrigen
df6:  puertoDestino --> nomPaísPuertoDestino
df7:  puertoIntermedio --> nombrePaisPuertoIntermediol 
df8:  dniPasajero --> nYApPasajero, dirPasajero
df9:  nombreBuque, #Viaje, dniPasajero --> puertoInicioPasajero, puertoFinalPasajero
df10: nombreBuque, fechaPosicionActual --> posicionActual
```

**Clave Candidata:**
```
cc: {nombreBuque, #Viaje, dniDueño, puertoIntermedio, dniPasajero, fechaPosicionActual}
```

##### Normalización a BCNF

Como se aprecia arriba, `BUQUE` no cumple con bcnf ya que exite al menos la df2 que no es trivial ni su determinante superclave, se realiza entonces el particionado de la misma dado dicha dependencia funcional:

```markdown
r1: (**tipoBuque**, tonelaje, tipoCasco)
r2: (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**, nYApDueño, tipoBuque, puertoOrigen, puertoDestino, nomPaísPuertoDestino, nombrePaisPuertoOrigen, nombrePaisPuertoIntermedio, posicionActual, nYApPasajero, dirPasajero, puertoInicioPasajero, puertoFinalPasajero)
```
**a) ¿Perdí información?**
No, ya que la interseccion entre los atributos de ambas particiones da como resultado el determinante de la dependencia por la cual se realizó la particion.

**b) ¿Perdí dependencias funcionales?**
No, ya que df2 vale en r1 y el resto en r2

**c) ¿R1, está en BCNF?**
Si, ya que solo tiene una unica dependencia funcional y su determinante es superclave de la partición.

**d) ¿R2, está en BCNF?**
No ya que al menos existe df1 tq no es trivial y su determinante no es superclave. Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl.


```markdown
r3: (**nombreBuque**, tipoBuque)
r4: (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**, nYApDueño, puertoOrigen, puertoDestino, nomPaísPuertoDestino, nombrePaisPuertoOrigen, nombrePaisPuertoIntermedio, posicionActual, nYApPasajero, dirPasajero, puertoInicioPasajero, puertoFinalPasajero)
```
**a) ¿Perdí información?**
No, ya que la interseccion entre los atributos de ambas particiones da como resultado el determinante de la dependencia por la cual se realizó la particion.

**b) ¿Perdí dependencias funcionales?**
No, ya que df1 vale en r3 y el resto en r4

**c) ¿R3, está en BCNF?**
Si, ya que solo tiene una unica dependencia funcional y su determinante es superclave de la partición.

**d) ¿R4, está en BCNF?**
No ya que al menos existe df3 tq no es trivial y su determinante no es superclave. Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl.


```markdown
r5: (**dniDueño**, nYApDueño)
r6: (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**, puertoOrigen, puertoDestino, nomPaísPuertoDestino, nombrePaisPuertoOrigen, nombrePaisPuertoIntermedio, posicionActual, nYApPasajero, dirPasajero, puertoInicioPasajero, puertoFinalPasajero)
```
**a) ¿Perdí información?**
No, ya que la interseccion entre los atributos de ambas particiones da como resultado el determinante de la dependencia por la cual se realizó la particion.

**b) ¿Perdí dependencias funcionales?**
No, ya que df3 vale en r5 y el resto en r6

**c) ¿R5, está en BCNF?**
Si, ya que solo tiene una unica dependencia funcional y su determinante es superclave de la partición.

**d) ¿R6, está en BCNF?**
No ya que al menos existe df5 tq no es trivial y su determinante no es superclave. Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl.


```markdown
r7: (**puertoOrigen**, nombrePaisPuertoOrigen)
r8: (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**, puertoOrigen, puertoDestino, nomPaísPuertoDestino, nombrePaisPuertoIntermedio, posicionActual, nYApPasajero, dirPasajero, puertoInicioPasajero, puertoFinalPasajero)
```
**a) ¿Perdí información?**
No, ya que la interseccion entre los atributos de ambas particiones da como resultado el determinante de la dependencia por la cual se realizó la particion.

**b) ¿Perdí dependencias funcionales?**
No, ya que df5 vale en r7 y el resto en r8

**c) ¿R8, está en BCNF?**
Si, ya que solo tiene una unica dependencia funcional y su determinante es superclave de la partición.

**d) ¿R6, está en BCNF?**
No ya que al menos existe df4 tq no es trivial y su determinante no es superclave. Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl.


```markdown
(**puertoDestino**, nomPaísPuertoDestino)
(**puertoIntermedio**, nombrePaisPuertoIntermediol)
(**dniPasajero**, nYApPasajero, dirPasajero)
#####
BUQUE (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**, puertoOrigen, puertoDestino, posicionActual, puertoInicioPasajero, puertoFinalPasajero)
#####
(**nombreBuque**, **#Viaje**, puertoOrigen, puertoDestino)
(**nombreBuque**, **#Viaje**, **dniPasajero**, puertoInicioPasajero, puertoFinalPasajero)
(**nombreBuque**, **fechaPosicionActual**, posicionActual)
#####
BUQUE (**nombreBuque**, **#Viaje**, **dniDueño**, **puertoIntermedio**, **dniPasajero**, **fechaPosicionActual**)
#####
```

```
nombreBuque -->> dniDueño
nombreBuque -->> fechaPosicionActual
nombreBuque, #Viaje -->> dniPasajero
nombreBuque, #Viaje -->> puertoIntermedio
```

```markdown
(**nombreBuque**, **dniDueño**)
(**nombreBuque**, **fechaPosicionActual**)
(**nombreBuque**, **#Viaje**, **dniPasajero**)
(**nombreBuque**, **#Viaje**, **puertoIntermedio**)
```

```markdown
tipos: 		(**tipoBuque**, tonelaje, tipoCasco)
buques: 	(**nombreBuque**, tipoBuque)
dueños: 	(**dniDueño**, nYApDueño)
origenes: 	(**puertoOrigen**, nombrePaisPuertoOrigen)
destinos: 	(**puertoDestino**, nomPaísPuertoDestino)
paradas:	(**puertoIntermedio**, nombrePaisPuertoIntermediol)
pasajeros:	(**dniPasajero**, nYApPasajero, dirPasajero)
viajes: 	(**nombreBuque**, **#Viaje**, puertoOrigen, puertoDestino)
pasajes: 	(**nombreBuque**, **#Viaje**, **dniPasajero**, puertoInicioPasajero,puertoFinalPasajero)
tracking: 	(**nombreBuque**, **fechaPosicionActual**, posicionActual)
pertenece: 	(**nombreBuque**, **dniDueño**)
escalas: 	(**nombreBuque**, **#Viaje**, **puertoIntermedio**)
```

