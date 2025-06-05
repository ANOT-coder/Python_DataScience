 #1 Number triangle
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print(j+1, end=" ")
        print('') 
pattern(5)'''

#11 left aligned star triangle
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print("*", end=" ")
        print()
pattern(5)'''

#4 constant row number pattern
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print(i, end=" ")
        print()
pattern(5)'''

#2 Floyds triangle
'''def pattern(n):
    num=1
    for i in range(1,n):
        for j in range(1,i+1):
            print(num,end=' ')
            num+=1
        print()
pattern(6)'''

#5 Odd Number Triangle
'''def pattern(n):
    num=1
    for i in range(1,n):
        for j in range(1,i+1):
            print(num,end=' ')
            num+=2
        print()
pattern(5)'''
# reverse number pattern
def pattern(n):
    for i in range(1,n):
        for j in range(i,0,-1):
            print(j, end=" ")
        print()
pattern(6)