# Base de Datos 1

## Práctica 2

### 1) Dados los siguientes esquemas

```markdown
DUEÑO (**id_dueño**, nombre, teléfono, dirección, dni)
CHOFER (**id_chofer**, nombre, teléfono, dirección, fecha_licencia_desde, fecha_licencia_hasta, dni)
AUTO (**patente**, id_dueño, id_chofer, marca, modelo, año)
VIAJE (**patente**, hora_desde, hora_hasta, origen, destino, tarifa, metraje)
```

#### a) Listar el dni, nombre y teléfono de todos los dueños que NO son choferes.

$$ \pi_{dni, nombre,telefono}(DUEÑO) - \pi_{dni, nombre,telefono}(CHOFER)$$

#### b) Listar la patente y el id_chofer de todos los autos a cuyos choferes les caduca la licencia el 01/01/2018.

$$ C \Longleftarrow \sigma_{fecha\_licencia\_hasta < "2018-01-01" }(CHOFER)$$

$$ \pi_{id_chofer, patente}( C \bowtie AUTO) $$

### 2) Dados los siguientes esquemas

```markdown
ALUMNO (**#alumno**, nombre_alumno, edad, provincia, beca)
MATRICULA (**#alumno**, **#asignatura**, grupo)
ASIGNATURA (**#asignatura**, nombre_asignatura, grupo, año)
PROFESOR (**#profesor, #asignatura**, nombre_prefesor, grupo)
```

#### a) Listar el nombre de los alumnos matriculados en todas las asignaturas de segundo año.

$$ ASegundo \Longleftarrow \sigma_{año = 2}(ASIGNATURA) $$

$$ AM \Longleftarrow MATRICULA \% (\pi_{\#asignatura}(ASegundo)) $$

$$\pi_{nombre\_alumno}(ALUMNO \bowtie AM)$$

####b) Listar el #alumno de los alumnos que no estén matriculados en BBDD.

$$ ANDB \Longleftarrow MATRICULA \bowtie (\sigma_{nombre\_asignatura \neq "BBDD"}(ASIGNATURA))$$

$$ \pi_{\#alumno}(ANDB)$$

### 3) Dados los siguientes esquemas

```markdown
TIPOMUEBLE (**id_tipomueble**,descripción)
FABRICANTE (**id_fabricante**,nombrefabricante,cuit)
TIPOMADERA (**id_tipomadera**,nombremadera)
AMBIENTE (**id_ambiente**,descripcionambiente)
MUEBLE (**id_mueble**, id_tipomueble, id_fabricante, id_tipomadera, precio, dimensiones, descripcion)
MUEBLEAMBIENTE (**id_mueble**,**id_ambiente**)
```

#### a) Obtener los nombres de los fabricantes que fabrican muebles en todos los tipos de Madera.

$$Fabs \Longleftarrow (\pi_{id\_fabricante,\ id\_tipomadera}(MUEBLE)) \% ( \pi_{id\_tipomadera}(TIPOMADERA))$$

$\pi_{nombrefabricante}(Fabs \bowtie FABRICANTES)$ 

#### b) Obtener los nombres de los fabricantes que sólo fabrican muebles en Pino.

$$ Pino \Longleftarrow \pi_{ id\_tipomadera }( \sigma_{ nombremadera = "pino" }( TIPOMADERA ) )$$

$$ FabPino \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie Pino ) $$ 



$$ Otras \Longleftarrow \pi_{id\_tipomadera }( \sigma_{ nombremadera \neq "pino" }( TIPOMADERA ) )$$

$$ FabOtras \Longleftarrow \pi_{ id\_fabricante, \ nombrefabricante }( FABRICANTE \bowtie Otras ) $$ 



$$ \pi_{nombrefabricante} ( FabPino - FabOtras ) $$ 

#### c) Obtener los nombres de los fabricantes que fabrican muebles para todos los ambientes.

$$AF \Longleftarrow \pi_{ id\_fabricante,\ id\_ambiente }( MUEBLE \bowtie MUEBLEAMBIENTE ) $$

$$Fabs \Longleftarrow  AF \% ( \pi_{id\_tipomadera}(TIPOMADERA))$$

$\pi_{nombrefabricante}(Fabs \bowtie FABRICANTES)$ 

#### d) Obtener los nombres de los fabricantes que sólo fabrican muebles para oficina.

$$ Ofi \Longleftarrow \pi_{ id\_ambiente }( \sigma_{ descripcionambiente = "oficina" }( AMBIENTE ) )$$

$$ MueOfi \Longleftarrow \pi_{ id\_fabricante }( MUEBLE \bowtie MUEBLEAMBIENTE \bowtie Ofi ) $$

$$ FabOfi \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie MueOfi ) $$ 



$$ Otras \Longleftarrow \pi_{id\_ambiente }( \sigma_{ descripcionambiente \neq "oficina" }( AMBIENTE ) )$$

$$ MueOtras \Longleftarrow \pi_{ id\_fabricante }( MUEBLE \bowtie MUEBLEAMBIENTE \bowtie Otras ) $$

$$ FabOtras \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie MueOtras ) $$ 



$$ \pi_{nombrefabricante} ( FabOfi - FabOtras ) $$ 

#### e) Obtener los nombres de los fabricantes que sólo fabrican muebles para baño y cocina.

$$ Baño \Longleftarrow \pi_{ id\_ambiente }( \sigma_{ descripcionambiente = "baño" }( AMBIENTE ) )$$

$$ MueBaño \Longleftarrow \pi_{ id\_fabricante }( MUEBLE \bowtie MUEBLEAMBIENTE \bowtie Ofi ) $$

$$ FabBaño \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie MueOfi ) $$ 



$$ Coci \Longleftarrow \pi_{ id\_ambiente }( \sigma_{ descripcionambiente = "cocina" }( AMBIENTE ) )$$

$$ MueCoci \Longleftarrow \pi_{ id\_fabricante }( MUEBLE \bowtie MUEBLEAMBIENTE \bowtie Coci ) $$

$$ FabCoci \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie MueCoci ) $$ 



$$ Otras \Longleftarrow \pi_{id\_ambiente }( \sigma_{ descripcionambiente \neq "baño"\ \land\ descripcionambiente \neq "cocina" }( AMBIENTE ) )$$

$$ MueOtras \Longleftarrow \pi_{ id\_fabricante }( MUEBLE \bowtie MUEBLEAMBIENTE \bowtie Otras ) $$

$$ FabOtras \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie MueOtras ) $$ 



$$ \pi_{nombrefabricante} ( ( FabBaño \cap FabCoci ) - FabOtras ) ​$$ 

#### f) Obtener los nombres de los fabricantes que producen muebles de cedro y roble.

$$ Cedro \Longleftarrow \pi_{ id\_tipomadera }( \sigma_{ nombremadera = "cedro" }( TIPOMADERA ) )$$

$$ FabCedro \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie Cedro ) $$ 



$$ Roble \Longleftarrow \pi_{ id\_tipomadera }( \sigma_{ nombremadera = "pino" }( TIPOMADERA ) )$$

$$ FabRoble \Longleftarrow \pi_{ id\_fabricante,\ nombrefabricante }( FABRICANTE \bowtie Roble ) $$ 



$$ \pi_{nombrefabricante} ( FabCedro \cap FabRoble ) $$ 

#### g) Obtener los nombres de los fabricantes que producen muebles de melamina o MDF.

$$ Maderas \Longleftarrow \sigma_{ nombremadera = "melamina"\ \lor\ nombremadera = "MDF" }( TIPOMADERA )$$

$$ FabMaderas \Longleftarrow \pi_{ id\_fabricante }( Maderas \bowtie MUEBLE )$$

$$ \pi_{ nombrefabricante }( FABRICANTES \bowtie FabMaderas ) $$

###4) Dados los siguientes esquemas

```markdown
CLIENTE (**id_cliente**, nombreCliente, puntaje, edad)
AUTOMOVIL (**id_automovil**, marca, color)
RESERVA (**id_cliente**, **id_automovil**, **fecha**)
```

Tener en cuenta que un cliente puede realizar diversas reservas

#### a) Obtener los colores de los automóviles reservados por Juan.

$$ Juan \Longleftarrow \pi_{ id\_cliente }( \sigma_{ nombreCliente = "Juan" }( CLIENTE ) ) $$

$$ AutosReservados \Longleftarrow \pi_{ id\_automovil }( Juan \bowtie RESERVA ) $$

$$ \pi_{color}( AutosReservados \bowtie AUTOMOVIL ) $$

#### b) Obtener los nombres de los clientes que no han reservado un automóvil verde.

$$ AutosVerdes = \pi_{id\_automovil}( \sigma_{color = "verde"}( AUTOMOVIL ) ) $$

$$ ClientesVerdes \Longleftarrow \pi_{ id\_cliente }( AutosVerdes \bowtie RESERVA )$$

$$ ClientesOtros \Longleftarrow \pi_{id\_cliente} ( CLIENTE ) - ClientesVerdes $$

$$ \pi_{nombreCliente}( ClientesOtros \bowtie CLIENTES ) $$

#### c) Obtener los nombres de los clientes que han reservado por lo menos dos automóviles.

$$ Res \Longleftarrow \rho_{\ r1 }( RESERVA ) \bowtie_{\ r1.cliente = r2.cliente\ \land\ r1.automovil \neq r2.automovil } \rho_{\ r2 }( RESERVA )$$

$$ Res \Longleftarrow \pi_{cliente}( Res )$$

$$ \pi_{ nombreCliente }( Res \bowtie CLIENTE) $$

#### d) Obtener el id de aquel cliente con el puntaje más alto.

$$ Puntajes \Longleftarrow \pi_{ id\_cliente, puntaje }( CLIENTES ) $$

$$Menores \Longleftarrow \pi_{p1.id\_cliente}( \rho_{ \ p1 }( Puntajes ) \bowtie_{\ p1.puntaje < p2.puntaje } \rho_{ \ p2 }( Puntajes ) )$$



$$ \pi_{ id\_cliente }( Puntajes ) - Menores $$

###5) Dados los siguientes esquemas

```markdown
ESTUDIANTE (**#legajo**, nombreCompleto, nacionalidad, añoDeIngreso, codigoDeCarrera)
CARRERA (**codigoDeCarrera**, nombre)
INSCRIPCIONAMATERIA (**#legajo**, **codigoDeMateria**)
MATERIA (**codigoDeMateria**, nombre)
```

#### a) Obtener el nombre de los estudiantes con nacionalidad "Argentina" que NO estén en la carrera con código "LI07"

$$ \pi_{ nombreCompleto }( \sigma_{ nacionalidad = "Argentina" \ \land\ codigoDeCarrera \neq "LI07" }( ESTUDIANTE ) ) $$ 

#### b) Obtener el legajo de los estudiantes que se hayan anotado en TODAS las materias.

$$ INSCRIPCIONAMATERIA \ \% \ \pi_{ codigoDeMateria }( MATERIA ) $$

###6) Dados los siguientes esquemas

```markdown
ALUMNO (**#alumno**, nombre)
CURSA (**#alumno**, **#curso**)
CURSO (**#curso**, nombre_curso)
PRACTICA (**#practica**, #curso)
ENTREGA (**#alumno**, **#practica**, nota)
```

#### a) Obtener #alumno y nombre de los alumnos que aprobaron con 7 o más todas las prácticas de los cursos que realizaron.

$$ PracticasNecesarias \Longleftarrow \pi_{ \#alumno,\ \#practica }( PRACTICA \bowtie CURSA ) $$

$$ PracticasAprob \Longleftarrow  \pi_{ \#alumno,\ \#practica }( \sigma_{nota \geq 7}( ENTREGA ) )$$

$$ AlumnosDesap \Longleftarrow \pi_{ \#alumno }( PracticasNecesarias - PracticasAprob )$$

$$AlumnosAprob \Longleftarrow \pi_{ \#alumno }( ALUMNO ) - AlumnosDesap $$

$$ AlumnosAprob \bowtie ALUMNO $$

###7) Dados los siguientes esquemas	

```markdown
PDA (**imei**, marca, serie)
JURISDICCION (**jurisdiccion**, nombre)
CONDUCTOR (**dni**, nombre, apellido, jurisdiccion)
TIPO (**codigo**, descripcion, puntos, tipo)
ACTA (**#acta**, imei, fecha, dni, jurisdiccion)
INFRACCION (**#acta**, **codigo**)
```

#### a) Obtener los códigos de los tipos de infracciones que no fueron utilizadas en las actas labradas de la jurisdicción “La Plata”.

$$ ActasLP \Longleftarrow ACTA \bowtie_{ ACTA.jurisdiccion = JURISDICCION.jurisdiccion\ \land\ nombre = "LaPlata" } JURISDICCION  $$

$$ ActasLP \Longleftarrow \pi_{ \#acta }( ActasLP ) $$

$$ CodsLP \Longleftarrow \pi_{ codigo }( ActasLP \bowtie INFRACCION )$$

$$ \pi_{ codigo }( TIPO ) - CodsLP $$

#### b) Obtener los #Actas en donde el conductor pertenezca a la misma jurisdicción del lugar del labrado del acta

$$ Actas \Longleftarrow \rho_{a} ( ACTA ) \bowtie_{ a.dni = c.dni \ \land\ a.jurisdiccion = c.jurisdiccion } \rho_c (CONDUCTOR) $$

$$ \pi_{ \#acta } ( Actas ) $$

#### c) Obtener los imei de PDA que han labrado actas de tipo “Velocidad” sólo en la ciudad de “Mar del Plata”.

$$ Otras \Longleftarrow \pi_{jurisdiccion}( \sigma_{ nombre \neq "Mar\ del\ Plata"}( JURISDICCION ) ) $$

$$ ActasOtras \Longleftarrow \pi_{ \#acta }( ACTAS \bowtie Otras ) $$

$$ Velocidad \Longleftarrow \pi_{ codigo }( \sigma_{ tipo="Velocidad" }( TIPO  ) ) $$ 

$$ ActasVelocidad \Longleftarrow \pi_{ \#acta }( INFRACCION \bowtie Velocidad ) $$  

$$ ActasVelocidadOtras \Longleftarrow ActasVelocidad \bowtie ActasOtras $$

$$ Actas \Longleftarrow \pi_{ \#acta }( ACTA ) - ActasVelocidadOtras $$

$$ \pi_{ imei }( Actas \bowtie ACTA ) $$ 

###8) Dados los siguientes esquemas

```markdown
USUARIO (**usuario**, email, nombre)
FORMULARIO (**formulario**, titulo, fecha)
PARTICIPACION (**usuario**, **formulario**)
APORTE (**aporte**, formulario, usuario, nombre, tipo, datos, valoracion)
```

####a) Obtener los nombres de los usuarios que hicieron aportes en todos los formularios, independientemente de si participan o no en el mismo.

$$ Forms \Longleftarrow \pi_{ formulario }( FORMULARIO ) $$

$$ Aportes \Longleftarrow \pi_{usuario,\ formulario}( APORTE )\ \%\ Forms$$

$$ \pi_{ nombre }( USUARIO \bowtie Aportes ) $$

####b) Obtener los nombres de los usuarios que han realizado aportes en todos los formularios en los que participa.

$$ Aportes \Longleftarrow \pi_{usuario,\ formulario}( APORTE ) $$

$$ Extras \Longleftarrow \pi_{ usuario }( PARTICIPACION - Aportes ) $$

$$ Usuarios \Longleftarrow \pi_{ usuario }( USUARIO ) - Extras $$

$$ \pi_{ nombre }( USUARIO \bowtie Usuarios ) $$

#### c) Obtener el identificador del usuario que realizo la publicación con mayor valoración.

$$ Valoracion \Longleftarrow \pi_{ usuario, valoracion }( APORTE ) $$

$$ Minimas \Longleftarrow \pi_{ v1.usuario,\ v1.valoracion }( \rho_{\ v1 }( Valoracion ) \bowtie_{\ v1.valoracion < v2.valoracion } \rho_{\ v2 }( Valoracion ) ) $$

$$ \pi_{ usuario } ( Valoracion - Minimas ) $$

###9) Dados los siguientes esquemas

```markdown
IDIOMA (**idioma**, nombre)
DICCIONARIO (**diccionario**, lenguaje, fecha)
USUARIO (**usuario**, nombre, ingreso)
DEFINICION (**diccionario**, **usuario**, **palabra**, significado)
```

#### a) Obtener los nombres de los usuarios que hayan ingresado antes del 2010 y no hayan aportado ninguna definición

$$ Usuarios \Longleftarrow \pi_{nombre, usuario}( \sigma_{ ingreso < "2010-01-01"}( USUARIO ) ) $$

$$ Aportes \Longleftarrow \pi_{ nombre, usuario }( DEFINICION \bowtie Usuarios ) $$

$$ \pi_{ nombre }( Usuarios - Aportes ) $$ 

#### b) Obtener los nombres de todos los usuarios que hayan aportado alguna definición para el idioma Español

$$ es \Longleftarrow \pi_{ lenguaje }( \sigma_{ nombre = "Español" }( \rho_{\ lenguaje \leftarrow idioma }( IDIOMA ) ) ) $$

$$ esDic \Longleftarrow \pi_{ diccionario }( DICCIONARIO \bowtie es ) $$

$$ Usuarios \Longleftarrow \pi_{ usuario }( DEFINICION \bowtie esDic ) $$

$$ \pi_{ nombre }( USUARIO \bowtie Usuarios ) $$

#### c) Obtener el nombre de los idiomas que no tengan diccionarios posteriores al 2015

$$ Dics \Longleftarrow \pi_{ idioma }( \sigma_{ fecha > "2015-12-31" }( \rho_{\ idioma \leftarrow lenguaje }( DICCIONARIO ) ) ) $$

$$ Idiomas \Longleftarrow \pi_{ idioma }( IDIOMAS ) - Dics $$

$$ \pi_{ nombre }( Idiomas \bowtie IDIOMAS ) $$

###10) Dados los siguientes esquemas

```markdown
VIAJE (**viaje**, fecha, hora, origen, destino, vehiculo)
LUGAR (**lugar**, nombre)
VEHICULO (**vehiculo**, usuario, capacidad)
USUARIO (**usuario**, nombre, apellido)
PASAJERO (**viaje**, **usuario**)
```

#### a) Obtener fecha y hora de los viajes posteriores al 30/11 que vayan desde La Plata hacia Rosario y que no tengan pasajeros registrados.

$$ LaPlata \Longleftarrow \pi_{lugar}( \sigma_{ nombre = "La\ Plata" }( LUGAR ) ) $$

$$ Rosario \Longleftarrow \pi_{lugar}( \sigma_{ nombre = "Rosario" }( LUGAR ) ) $$

$$ Viajes \Longleftarrow VIAJE \bowtie_{ VIAJE.destino = lugar\ \land\ fecha\ >\ "2017-11-30" } Rosario $$

$$ Viajes \Longleftarrow \pi_{viaje} ( Viajes \bowtie_{ Viajes.origen = lugar\ } LaPlata ) $$



$$ VcP \Longleftarrow \pi_{ viaje } ( PASAJERO \bowtie Viajes ) $$

$$ Viajes \Longleftarrow Viajes - VcP $$

$$ \pi_{ fecha,\ hora }( VIAJE \bowtie Viajes ) $$

#### b) Obtener el identificador del usuario que posee el auto con la capacidad más alta.

$$ Capacidad \Longleftarrow \pi_{ usuario, capacidad }( VEHICULO ) $$

$$ Minimas \Longleftarrow \pi_{c1.usuario,\ c1.capacidad}( \rho_{\ c1 }( Capacidad ) \bowtie_{\ c1.capacidad\ <\ c2.cacpacidad} \rho_{\ c2 }( Capacidad ) ) $$

$$ \pi_{ usuario } ( Capacidad - Minimas ) $$