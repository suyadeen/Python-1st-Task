#Min

li=[10,3,32,40,6,40,70]

for i in li:
    for j in li:
        if j<i:
            i=j
print(i)


#Max

li=[10,3,32,40,6,40,70]

for i in li:
    for j in li:
        if j>i:
            i=j
print(i)
