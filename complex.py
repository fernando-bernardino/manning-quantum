import math
import cmath
import matplotlib.pyplot as plot

complex_numbers = [
    complex(1,1), 
    complex(2,1), 
    complex(6,3), 
    complex(-3,4), 
    complex(6,-1)
]

acc = complex(0, 0)
[acc := acc + x  for x in complex_numbers]
print(acc)

[plot.scatter(x.real, x.imag) for x in complex_numbers]
plot.show()
