```
INTERNACION (codHospital, cantidadHabitaciones, direcciónInternacionPaciente, telefonoInternacionPaciente, dniPaciente, domicilioPaciente, nombreApellidoPaciente, domicilioHospital, ciudadHospital, directorHospital, fechaInicioInternacion, cantDiasIntenacion, doctorQueAtiendePaciente, insumoEmpleadoInternación)
```

```
dniPaciente --> domicilioPaciente, nombreApellidoPaciente, 
codHospital --> domicilioHospital, ciudadHospital, directorHospital, cantidadHabitaciones
dniPaciente, fechaInicioInternacion --> cantDiasIntenacion, direcciónInternacionPaciente, telefonoInternacionPaciente, codHospital
domicilioHospital, ciudadHospital --> codHospital
```

```
CC (dniPaciente, fechaInicioInternacion, doctorQueAtiendePaciente, insumoEmpleadoInternación)
```

```
(**codHospital**, domicilioHospital, ciudadHospital, directorHospital, cantidadHabitaciones)
(**dniPaciente**, domicilioPaciente, nombreApellidoPaciente)
(**dniPaciente**, **fechaInicioInternacion**, cantDiasIntenacion, direcciónInternacionPaciente, telefonoInternacionPaciente, codHospital)
(**dniPaciente**, **fechaInicioInternacion**, **doctorQueAtiendePaciente**, **insumoEmpleadoInternación**)
```





persona --> domicilios

domicilio --> telefonos

(persona, telefono)



p1 -> v1

p1 -> v2

p2 -> v1

v1 -> t1

v1 -> t2

v2 -> t3

v1 -> t4



(p1, t1)

(p1, t2)

(p2, t1)

(p2, t1)

(p1, t3)

(p1, t4)

(p2, t4)