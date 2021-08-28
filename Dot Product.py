#การคูณเเบบ Scalar (must square metrix)
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
c = a.dot(b) #[[1*11+2*13, 1*12+2*14],[3*11+4*13],[3*12+4*14]]
print(c)
