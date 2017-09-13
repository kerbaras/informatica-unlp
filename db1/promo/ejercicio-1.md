# Ejecricio de Promoción

## Presentación

Sean las relaciones $CD$, $LT$ y $CR$ definidas como:

```
LT(empleado, departamento)
CD(curso, departamento)
CR(empleado, curso)
```

se quiere obtener los empleados que hicieron todos los cursos requeridos por su departamento.

Notesé que CR hace referencia a los Cursos Realizados, LT a Lugar de Trabajo y CD a los Cursos requeridos por Departamento.

## Proposición

Para resolver dicho interrogante se propone la nueva relación $CN​$ (Cursos Necesarios) la cual contiene las tuplas $(empleado, curso)​$ tales que para todo departamento donde trabaja el empleado, exista una restricción del curso para un departamento:

$$ CN = \left\{ \left( empleado, curso \right) \mid  \left( \forall curso \right)  \left( \forall (empleado, departamento) \in LT \right)\left( \exists (curso, departamento) \in CD  \right)   \right\}$$

Luego se observa que todos los elementos presentes en $CN-CR​$ describen los cursos necesarios que le falta realizar a un empleado:

$$ CN - CR = \{ x \in CN \mid x \notin CR \} \implies (e, c) \in CN-CR \implies (e,c) \in CN \land (e, c) \notin CR $$ 

$$ \therefore e \text{ necesita realizar } c$$

Se define entonces, $E = \{ e \mid (e,d) \in LT \} - \{ e \mid (e,c) \in CN - CR \}  $ como el conjunto de empleados que no necesitan realizar algún curso requerido por sus departamentos.

## Resolución

$$ CN \Leftarrow \pi_{empleado, curso}\left( CD \bowtie LT \right)$$

$$ \pi_{empleado} \left( LT \right ) -  \pi_{empleado} \left( CN - CR \right )  $$