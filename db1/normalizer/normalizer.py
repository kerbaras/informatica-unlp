from functools import reduce

def to_bsnf(relation, dependencies):
    schema = {}
    part = relatiot & relation
    for dependency in dependencies:
        (x, y) = dependency
        schema['r' + str(count(schema))] = (*x,'@', *y)
        part = part - y
        if(True):
            pass

