<<<<<<< HEAD
j=[]
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
=======
j=[]
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
>>>>>>> 83cfea7421cd9b531629103b160a32341d2d17f3
print (','.join(j))