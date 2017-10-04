# TTPS Ruby - Práctica 2

## Métodos

### 1. Implementá un método que reciba como parámetro un arreglo de números, los ordene y devuelva el resultado

```ruby
def ordenar(nums)
    nums.sort
end
```

### 2. 

```ruby
def ordenar(*nums)
  nums.sort
end
```

### 3.

```ruby
ordenar *array
```

### 4.

```ruby
def longitud(*args)
  args.map { |arg| arg.to_s }.each { |arg| puts( arg + ' --> ' + arg.length.to_s ) }
end
```

