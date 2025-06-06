 #1 Number triangle
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print(j+1, end=" ")
        print('') 
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

#3 reverse row number pattern
'''def pattern(n):
    for i in range(1,n):
        for j in range(i,0,-1):
            print(j, end=" ")
        print()
pattern(6)'''

#4 constant row number pattern
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print(i, end=" ")
        print()
pattern(5)'''


#5 Odd Number Triangle
'''def pattern(n):
    num=1
    for i in range(1,n):
        for j in range(1,i+1):
            print(num,end=' ')
            num+=2
        print()
pattern(5)'''

#6 Multiplies Triangle
'''def pattern(n):
    
    for i in range(1,n):
        for j in range(i):
            print(i*(j+1),end=" ")
        print()
pattern(5)
'''
#8 Checkerboard Binary triangle
'''def pattern(n):
    num=1
    for i in range(1,n):
        for j in range(i):
            print(num, end=' ')
            num=1-num
        print()
pattern(5)'''

#9 Alternating Binary Triangle
'''def pattern(n):
    for i in range(1,n+1):
        val = 1 if i == 1 or i % 2 == 0 else 0
        for j in range(i):
            print(val,end=" ")
            val=1-val
        print()

pattern(4)'''

#10 reverse number triangle
'''def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
pattern(4)
'''


#11 left aligned star triangle
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print("*", end=" ")
        print()
pattern(5)'''


#13 inverted left aligned star triangle
'''def pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print('*',end=" ")
        print()
pattern(4)'''


#21 Alphabet triangle
'''def pattern(n):
    alpha=['A','B','C','D']
    for i in range(1,n):
        for j in range(i):
            print(alpha[j],end=" ")
        print()
pattern(5)
'''
#or
'''def pattern(n):
    
    for i in range(1,n):
        for j in range(i):
            print(chr(64+i),end=" ")
        print()
pattern(5)'''


#22 Repeating alphabet Triangle
'''def pattern(n):
    for i in range(1,n):
        for j in range(i):
            print(chr(65+j),end=" ")
            
        print()
pattern(5)'''


#23 Continuous Alphabet Pattern 
'''def pattern(n):
    num=0
    for i in range(1,n):
        for j in range(i):
            print(chr(num+65),end=" ")
            num+=1
        print()
pattern(5)'''

#24 Reverse Alphabet Pattern 
def pattern(n):
    for i in range(n,-1,-1):
        for j in range(i,n):
            print(chr(j+65),end=' ')
        print()
pattern(4)


#25 Inverted  Alphabet Pyramid
'''def pattern(n):
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            print(chr(j+65),end=" ")
        print()
pattern(5)'''