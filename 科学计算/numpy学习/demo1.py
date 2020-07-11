import numpy as np

a = np.array([[1,2,3],[4,5,6]]) # numpy 每一个 [] 默认是一行

print(a,a.dtype,a.shape)


dt = np.dtype([('age',np.int8)]) # 规定了数据类型（int8）和别名
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a['age'])

a = np.array([[10,20,30],[10,20,30]], dtype = dt) 
print(a['age'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
