import numpy as np
np.random.seed(42)
a =np.random.randint(1,100,10)
print(a)
boola =a>30
print(boola)
print(a[boola])

