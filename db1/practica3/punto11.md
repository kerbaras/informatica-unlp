```
BUQUE (nombreBuque, nYApDueño, dniDueño, tipoBuque, tonelaje, tipoCasco, #Viaje, puertoOrigen, puertoDestino, puertoIntermedio, nomPaísPuertoDestino, nombrePaisPuertoOrigen, nombrePaisPuertoIntermedio, posicionActual, fechaPosicionActual, nYApPasajero, dniPasajero, dirPasajero, puertoInicioPasajero, puertoFinalPasajero)
```

```
nombreBuque --> tipoBuque
tipoBuque --> tonelaje, tipoCasco
dniDueño --> nYApDueño
nombreBuque, #Viaje --> puertoOrigen, puertoDestino
puertoOrigen --> nombrePaisPuertoOrigen
puertoDestino --> nomPaísPuertoDestino
puertoIntermedio --> nombrePaisPuertoIntermediol 
dniPasajero --> nYApPasajero, dirPasajero
nombreBuque, #Viaje, dniPasajero --> puertoInicioPasajero, puertoFinalPasajero
nombreBuque, fechaPosicionActual --> posicionActual
```

```
CC: (nombreBuque, #Viaje, dniDueño, puertoIntermedio, dniPasajero, fechaPosicionActual)
```

```markdown
(**tipoBuque**, tonelaje, tipoCasco)
(**nombreBuque**, tipoBuque)
(**dniDueño**, nYApDueño)
(**puertoOrigen**, nombrePaisPuertoOrigen)
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

