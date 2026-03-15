import numpy as np

data_type = [('name','S15'),('class',int),('roll',int)]

studDetails = [
    ('Ibrahim',7,17),
    ('Zainab',9,67),
    ('Ayan',5,45),
    ('Prachi',11,34),
]

stud = np.array(studDetails,dtype=data_type)
print("OriginalArray:")
print(stud)
print("Sorting with RollNumber")
print(np.sort(stud,order='roll'))
