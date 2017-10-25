# Base de Datos 1

## Práctica 3

**Para los esquemas propuestos en cada ejercicio aplicar el proceso de normalización**

Todos los esquemas ya se encuentran en 1FN. Utilizar las claves candidatas y Dependencias Funcionales provistas.

### 1)
```
LIBRERIAS_ASOCIADAS ( idLibreria, nombreLibreria, idArticulo, nombreArticulo, idComponente,
nombreComponente, idFabricanteArticulo, idDueño)
```

**Donde:**

- Para cada librería se conoce su identificador, el cual es único. Además se conoce su nombre, que puede repetirse en distintas librerías.
- Cada librería posee uno o varios dueños (idDueño)
- Cada librería registra los artículos (idArticulo) que tiene en su inventario. Para cada artículo de una librería se conoce su nombre.
- Los identificadores de artículos se pueden repetir en diferentes librerías, pero no dentro de una misma librería.
- Los artículos de una librería están compuestos por diversos componentes (idComponente).
- Los identificadores de componentes se pueden repetir en diferentes librerías para diferentes artículos, pero no
para el mismo componente de un artículo dentro de una misma librería.
- Para cada componente de un artículo de una librería se conoce su nombre.
- Cada artículo de una librería tiene varios fabricantes que lo proveen (idFabricanteArticulo)

**Clave Candidata:**
```
Cc1: (idLibreria, idArticulo, idComponente, idFabricanteArtículo, idDueño)
```

**Dependencias funcionales:**

```
idLibreria -> nombreLibreria
idLibreria, idArticulo -> nombreArticulo
idLibreria, idArticulo, idComponente-> nombreComponente
```

### 2)

```
EMPLEADO ( idEmpleado, nombreEmpleado, idOficina, nombreOficina, idResponsableOficina,
cargaHorariaEnOficina, nombreResponsableOficina, añoIngresoOficina, idActividadEmpleadoOficina,
nombreActividadOficina, dniEmpleado)
```

**Donde:**

- El idEmpleado es único por oficina. El mismo idEmpleado no se repite en diferentes oficinas
- Cada empleado tiene asignada una única carga horaria para la oficina en la que trabaja e ingreso a la oficina en un año determinado
- El nombre del empleado no es único, es decir puede haber más de un “Juan Perez” trabajando en una oficina
- El nombre del responsable de la oficina no es único, es decir puede haber más de un “Juan Perez” responsable de una oficina
- En una oficina existen muchos responsables (tener en cuenta que el esquema ya se encuentra en 1FN)
- Los responsables de oficina pueden repetirse para diferentes oficinas
- idActividadEmpleadoOficina es cada actividad que un empleado realiza en la oficina


**Claves candidatas:**

```
Cc1: (idEmpleado, idResponsableOficina, idActividadEmpleadoOficina)
Cc2: (dniEmpleado, idResponsableOficina, idActividadEmpleadoOficina)
```

**Dependencias funcionales:**

```
idOficina -> nombreOficina
idResponsableOficina, idOficina -> nombreResponsableOficina
idEmpleado -> nombreEmpleado, idOficina, añoIngresoOficina, dniEmpleado, cargaHorariaEnOficina
dniEmpleado -> nombreEmpleado, idOficina, añoIngresoOficina, idEmpleado, cargaHorariaEnOficina
idActividadEmpleadoOficina -> nombreActividadOficina
```

**Para los esquemas propuestos en cada ejercicio aplicar el proceso de normalización**

Tener en cuenta que los esquemas dados ya se encuentran en 1FN.

### 3)

```
INFORME_MEDICO (idMedico, apynMedico, tipoDocM, nroDocM, fechaNacM, matricula, direcciónM, teléfonoM,
idPaciente, apynPaciente, tipoDocP, nroDocP, fechaNacP, idObraSoc, nroAfiliado, direcciónP, teléfonoP,
nombreOS, direcciónOS, teléfonoOS, idÓrgano, descripción, idEstudio, resultado, fechaEstudio, informe)
```

**Donde:**

- De cada médico se conoce su nombre y apellido, tipo y número de documento, fecha de nacimiento, matricula,
    dirección y teléfono.
- De cada paciente se conoce su nombre y apellido, tipo y número de documento, fecha de nacimiento,
    dirección, teléfono, obra social y número de afiliado. Cada obra social numera a sus afiliados de forma
    independiente, con lo cual los nroAfiliado podrían repetirse en diferentes obras sociales.
- De cada obra social se conoce su nombre, dirección y teléfono.
- Para cada órgano se conoce su descripción
- De cada estudio se registra a que paciente pertenece, que médico lo realizo, que órgano se estudio, un
    informe, el resultado y en qué fecha se realizó.

### 4)

```
AEROPUERTO (#aeropuerto, #pista, fecha, #avion)
```

**Donde:**

- \#aeropuerto y \#avion son únicos, pero el #pista se puede repetir para distintos aeropuertos.
- fecha representa la fecha de despegue de un avión. Cada avión tiene como máximo un despegue diario en
    un mismo aeropuerto.
- Un avión puede realizar despegues de distintos aeropuertos

### 5)

```
DISPOSITIVOS (Marca_id, descripMarca, modelo_id, descripModelo, equipo_tipo_id, descripEquipoTipo,
empresa_id, nombreEmpresa, cuit, direcciónEmpresa, usuario_id, apyn, nro_doc, direcciónUsuario, cuil,
plan_id, descripPlan, importe, equipo_id, imei, fec_alta, fec_baja, observaciones, línea_id, nroContrato,
fec_alta_linea, fec_baja_linea)
```

**Donde:**

- Para cada equipo interesa conocer su tipo, modelo, imei, fecha en que se dio de alta, fecha en que se da de baja
    y las observaciones que sean necesarias.
- De cada marca se conoce su descripción
- De cada modelo se conoce su descripción y a que marca pertenece.
- Para cada plan, se registra que empresa lo brinda, la descripción e importe del mismo.
- Para cada tipo de equipo se conoce la descripción
- Para cada empresa se registra el nombre, cuit y dirección
- De cada usuario se registra su nombre y apellido, número de documento, dirección y cuil.
- Para cada línea se necesita registrar el número de contrato, que plan posee, la fecha de alta de la línea, la
    fecha de baja, el equipo que la posee y el usuario de la misma.

### 6)

```
TOMAS_FOTOGRAFICAS ( idElemento, descripcionElemento, idFoto, fechaFoto, obturacionCamaraFoto,
idCamara, caracteristicaTecnicaCamara, descripcionCaracteristica)
```

Cuando se toma una fotografía, se indican todos los elementos que aparecen en ella, se registra la cámara con la que se
tomó, el valor de obturación del lente de la cámara y todas las características técnicas de la cámara con la que se toma
la foto.

- En una foto puede haber varios elementos, un elemento puede aparecer en varias fotos, pero en una misma foto
    solo parece una vez
- El idElemento y el idFoto son únicos en el sistema
- obturacionCamaraFoto es la obturación del lente de la cámara usada en una foto
- caracteristicaTecnicasCamara es una característica técnica de una cámara. Cada cámara puede tener muchas
    características, pero tener en cuenta que la misma característica NO pertenece a mas de una cámara. Dos
    caracteristicaTecnicasCamara pueden tener la misma descripción pero pertenecerán a cámaras diferentes.

### 7)

```
EMPRESA_COLECTIVO (#Línea, #Ramal, #Colectivo, dniChofer, dniInspector, dniEmpleado, nombreLinea,
nombreChofer, nombreInspector, nombreEmpleado)
```

**Donde:**

- Una línea posee varios ramales
- Los #Ramal no se repiten en distintas líneas
- Los #Colectivo se repiten en distintas líneas
- Los choferes están asignados a un único ramal
- Cada colectivo de una línea está asignado a un único ramal.
- Para cada ramal existe al menos un chofer asignado.

### 8)

```
INTERNACION (codHospital, cantidadHabitaciones, direcciónInternacionPaciente,
telefonoInternacionPaciente, dniPaciente, domicilioPaciente, nombreApellidoPaciente, domicilioHospital,
ciudadHospital, directorHospital, fechaInicioInternacion, cantDiasIntenacion, doctorQueAtiendePaciente,
insumoEmpleadoInternación)
```

**Donde:**

- cantidadHabitaciones es la cantidad de habitaciones que hay en cada hospital
- direcciónInternacionPaciente y telefonoInternacionPaciente, indican la dirección y el teléfono que deja un
    paciente cuando se interna
- domicilioPaciente es el domicilio que figura en el dni del paciente
- Un paciente para una internación es atendido por muchos doctores (doctorQueAtiendePaciente)
- Para una internación de un paciente, se emplean varios insumos (insumoEmpleadoInternación)
- El código de hospital (codHospital) es único.
- Existe un único director por hospital. Un director podría dirigir mas de un hospital
- Un paciente en la misma fecha no puede estar internado en diferentes hospitales
- En un domicilioHospital de una ciudad existe un único hospital

### 9)

```
INFRACCIONES_REALIZADAS (#auto, modeloAuto, #cedula, #conductor, fechaVto, #propietario, #infraccion,
fechaInfraccion, tipoInfraccion)
```

**Donde:**

- un auto tiene una o más cédulas asociadas que corresponden a los conductores autorizados. Cada cédula se
    asocia a un único auto y a un único conductor, y tiene una fecha de vencimiento.
- los #cedula y #conductor son únicos en el sistema. Si bien un conductor puede conducir varios autos, para cada
    uno de ellos tendrá una cédula diferente.
- un auto puede tener más de un propietario y un propietario puede tener más de un auto.
- de cada infracción que se labra se registra el número de cedula del conductor del auto. Además se conoce la fecha y el tipo de infracción.


### 10)

```
RESERVA (#Reserva, #Agencia, nombreAgencia, fechaReservaVuelo, ciudadOrigen, ciudadDestino,
tipoPago, nombreAerolínea, #Vuelo, dniPasajero, nombrePasajero, dirPasajero, telPasajero, clase, fechaPartida,
fechaLlegada, horaPartida, horaLlegada, modeloAvión, #Asiento, tipoComida, compañíaPasajero, dirCompañía,
telCompañía)
```

**Donde:**

- Una reserva puede involucrar uno o varios pasajeros (por ejemplo un tour).
- Si bien todos los pasajeros de una reserva viajan en la misma clase del mismo vuelo, cada uno de ellos decide el
    tipo de pago de su asiento (El tipo de pago se refiere al la forma de pago: efectivo, tarjeta de crédito, etc.). Notar
    que para cada vuelo el tipo pago puede ser potencialmente diferente.
- Una reserva puede involucrar muchos vuelos (por ejemplo para desplazarse de A a C se debe pasar por una
    escala intermedia B); tener en cuenta que no necesariamente todos los pasajeros de una reserva viajan en todos
    lo vuelos de esa reserva. Para cada vuelo de una reserva se conoce la fecha para la cual se realiza. Para una
    fecha puede haber varios vuelos de una o varias reservas.
- La reserva es realizada a través de una única agencia de turismo.
- Los pasajeros pueden estar independientemente involucrados en distintas reservas.
- Cada aerolínea maneja su propia forma de asignar el #Reserva, con lo cuál no hay garantía que estos no se
    repitan para las distintas aerolíneas.
- Las aerolíneas siempre usan el mismo modelo de avión para el mismo vuelo. Y el mismo vuelo de una aerolínea
    siempre sale de la misma ciudad a la misma hora, y llega a la misma ciudad destino a la misma hora de llegada,
    los días que ese vuelo es ofrecido por la aerolínea.
- El tipo de comida significa si corresponde desayuno, almuerzo, cena o merienda o cualquier combinación de
    ellos para cada vuelo.
- Para cada reserva de un pasajero se conoce el domicilio del pasajero y datos de su lugar de trabajo. Un pasajero
    puede trabajar en más de una compañía, una compañía puede tener más de una dirección y en cada dirección
    de una compañía puede haber más de un teléfono.

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
