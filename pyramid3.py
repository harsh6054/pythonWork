'''
1111
222
33
4
'''
count=1
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(count,end=" ")
    count=count+1
    print(" ")