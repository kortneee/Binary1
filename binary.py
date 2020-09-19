"""Compute the binary digits of an integer entered by the user"""
#MSC260 FALL 2020 Project 1
#Kortne Reiss
#Declaration: I, Kortnee Reiss, am the sole author of this code, which was
#developed in accordance with the rules in the course syllabus.
n = int(input())
print("x x//2 x%2")
i = 0
m=n
M=[]
while n >= 1:
    M.append(n%2)
    print(n, int(n/2), n%2)
    n = n/2
    n = int(n)
    i=i+1
M.reverse()
print("Therefore,", m ,"= 0b",1*M)