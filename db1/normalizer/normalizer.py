def is_trivial(dependency):
    (x, y) = dependency
    return y <= x;

def is_superkey(key, dependency):
    (x, y) = dependency
    return key <= x

def is_bcnf(dependency, key):
    return is_superkey(key, dependency) or is_trivial(dependency)

def str_dependency(dependency):
    (x, y) = dependency
    return f'{x}-->{y}'.replace("'", '')

def str_relation(key, subset):
    attrs = subset - key
    keys = map(lambda key: "**" + str(key) + "**", key)
    return "(" + ", ".join(list(keys) + list(attrs)).replace("'", '') + ")"

def print_header(point, stream):
    stream.write(f'# Base de Datos 1\n')
    stream.write(f'## Práctica 3\n')
    stream.write(f'### {point})\n')

def print_dependencies(dependencies, stream):
    stream.write('**Dependencias funcionales:**\n')
    stream.write('```\n')
    i = 1
    for dependency in dependencies:
        stream.write(f'df{i}: {str_dependency(dependency)}\n')
        i += 1
    stream.write('```\n')

def get_key(relation, dependencies):
    cc = relation
    for (x, y) in dependencies:
        cc = cc - y
    return cc

def print_ck(key, stream):
    stream.write('**Clave Candidata:**\n')
    stream.write('```\n')
    stream.write(f'CC: {key}\n'.replace("'", ''))
    stream.write('```\n')

def print_block(text, stream):
    stream.write('\n')
    stream.write(f'{text}\n')
    stream.write('\n')
    
def print_list_block(list, stream):
    stream.write('\n')
    stream.write('\n'.join([str(e) for e in list]))
    stream.write('\n')
    stream.write('\n')

def print_md_block(list, stream):
    print_list_block(['```markdown'] + list + ['```'], stream)

def plus(subset, dependencies):
    result = None
    newResult = subset
    while newResult != result:
        result = newResult
        for (x, y) in dependencies:
            if(x <= result):
                newResult = result | y
    return result

def loose_dependency(dependency, schema, dependencies):
    x, y = dependency
    result = None
    newResult = x
    while newResult != result:
        result = newResult
        for relation in schema:
            llego =  plus(result & relation, dependencies)
            newResult = result | (plus(result & relation, dependencies) & relation)
            if(y <= newResult):
                return False
    return not (y <= result)

def loose_dependencies(schema, dependencies):
    deps = []
    for dependency in dependencies:
        if(loose_dependency(dependency, schema, dependencies)):
            deps.append(dependency)
    return deps

class Partition:
    def __init__(self, key, attrs, number=0):
        self.key = key
        self.attrs = attrs
        self.number = number
    
    def __str__(self):
        return f'R{self.number}: {str_relation(self.key, self.attrs)}'

    def as_set(self):
        return self.key | self.attrs

    def __sub__(self, subset):
        return Partition(self.key - subset, self.attrs - subset)
    
    def denay_bcnf(self, dependencies):
        deps = [dependency for dependency in dependencies if
                 dependency in self and (not is_bcnf(dependency, self.key)) ]
        return (deps[0] if len(deps) > 0 else None)
    
    def __contains__(self, dependency):
        (x, y) = dependency
        return (x | y) <= self.as_set()

    def print_md_block(self, stream):
        stream.write('```markdown\n')
        stream.write(str(self))
        stream.write('\n')
        stream.write('```\n')
        
    def md_name(self):
        return f' `R{self.number}` '

def part(relation, dependency):
    (x, y) = dependency
    p1 = Partition(x, y)
    p2 = relation - y
    return (p1, p2)

def to_bcnf(relation, dependencies, key=None, file=None):
    if(key == None):
        key = get_key(relation, dependencies)

    dependencyBag = [ d for d in dependencies ]

    schema = []

    def loose_information(p1, p2, dependency):
        x, y = dependency
        text = ['**a) ¿Perdí información?**']
        if(x <= p1.as_set() & p2.as_set()):
            text.append('No, ya que la interseccion entre las dos relaciones da el determinate de la dependencia funcional')
            text.append('')
            text.append('**b) ¿Perdí dependencias funcionales?**')
            
            deps = loose_dependencies([part.as_set() for part in schema + [p1, p2]], dependencies)
            
            if( len(deps) > 0 ):
                text.append('Si, se perdieron las dependencias funcionales: ' + " ".join([
                    f'`{str_dependency(dep)}`' for dep in deps
                ]))
                print_list_block(text, file)
                return True
            text.append("No se perdio ninguna dependencia funcional")
            print_list_block(text, file)
            return False

        text.append("Si ya que las particiones no comparten al determinante.")
        print_list_block(text, file)
        return True


    def bcnf_process(original):
        dependency = original.denay_bcnf(dependencyBag)
        text = [f'**¿{original.md_name()} está en bcnf?**']
        if( dependency != None ):
            text.append(f'No, exite la dependencia funciona `{str_dependency(dependency)}` que no es trivail ni superclave')
            text.append('Se realiza entonces el particionado de esta relación por medio de dicha dependencia funcioanl')
            dependencyBag.remove(dependency)
            (p1, p2) = part(original, dependency)
            p1.number = original.number + 1
            p2.number = original.number + 2

            text.append('')
            text.append('Se proponen los siguientes esquemas:')
            print_list_block(text, file)
            print_md_block([p1, p2], file)
            if(loose_information(p1, p2, dependency)):
                print("Perdi Informacion")
            else:
                print("No perdi informacion")
            bcnf_process(p1)
            bcnf_process(p2)

        elif len(dependencies) > 0:
            text.append(f'Si, todas sus dependencias funcionales son o triviales o sus determinantes son superclave')
            print_list_block(text, file)
            schema.append(original)

        else:
            text.append(f'Si, todas sus dependencias funcionales son o triviales o sus determinantes son superclave')
            print_list_block(text, file)
            schema.append(original)

    p0 = Partition(key, relation, 0)

    print_block(f'Se plantea ahora una nueva relacion {p0.md_name()} para realizar el proceso de normalizacion:',file)
    p0.print_md_block(file)
    bcnf_process(p0)
    print_block('El esquema final en en bcnf sera:', file)
    print_md_block(schema, file)


    
def normalize(relation, dependencies, filename, point=0):
    with open(filename, 'w') as file:
        file.seek(0)
        print_header(point, file)
        print_block('Se buscand dependencias funcionales en la relacion para luego determinar las claves candidatas, y se encuentran:', file)
        
        print_dependencies(dependencies, file)
        
        key = get_key(relation, dependencies)
        print_ck(key, file)

        to_bcnf(relation, dependencies, key, file)

if(__name__ == '__init__'):
    relation = { 'nombreBuque', 'nYApDueño', 'dniDueño', 'tipoBuque', 'tonelaje', 'tipoCasco', '#Viaje', 'puertoOrigen',
                'puertoDestino', 'puertoIntermedio', 'nomPaísPuertoDestino', 'nombrePaisPuertoOrigen',
                'nombrePaisPuertoIntermedio', 'posicionActual', 'fechaPosicionActual', 'nYApPasajero', 
                'dniPasajero', 'dirPasajero', 'puertoInicioPasajero', 'puertoFinalPasajero' }

    dependencies = [
        ({'tipoBuque'}, {'tonelaje', 'tipoCasco'}),
        ({'nombreBuque'}, {'tipoBuque'}),
        ({'dniDueño'}, {'nYApDueño'}),
        ({'puertoOrigen'}, {'nombrePaisPuertoOrigen'}),
        ({'puertoDestino'}, {'nomPaísPuertoDestino'}),
        ({'puertoIntermedio'}, {'nombrePaisPuertoIntermedio'}),
        ({'nombreBuque', '#Viaje'}, {'puertoOrigen', 'puertoDestino'}),
        ({'dniPasajero'}, {'nYApPasajero', 'dirPasajero'}),
        ({'nombreBuque', '#Viaje', 'dniPasajero'}, {'puertoInicioPasajero', 'puertoFinalPasajero'}),
        ({'nombreBuque', 'fechaPosicionActual'}, {'posicionActual'})
    ]


    normalize(relation, dependencies, 'prueba.md')
