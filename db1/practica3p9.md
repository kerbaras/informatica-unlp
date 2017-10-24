```
(propietario, infraccion)

p1 -> a1
p2 -> a1
p3 -> a2

i1 -> a1
i2 -> a1
i3 -> a3

(0, p1, i1)
(0, p1, i2)
(0, p2, i1)
(0, p2, i2)
(0, p3, i3)
###
(0, p3, i2)
(0, p2, i3)
###  ==> (0 -/->> propietario) ^ (0 -/->> infraccion) ==> (propietario <<-->> infraccion)

```

