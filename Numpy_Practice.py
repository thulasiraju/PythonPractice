''' import numpy as np
print(np.__version__)
'''

import numpy as np

array1= np.array([2, 3, 4, 5, 6])
print(array1)
# 2. Create 3*3 numpy array with all Trues
boolarray_true = np.full((3,3), True, dtype=bool)
print(boolarray_true)
# Numpy array with all false
boolarray_false = np.full((3,3), False, dtype=bool)
print(boolarray_false)


