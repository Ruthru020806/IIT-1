s=set()
s1=set()
s2=set()
n=int(input("Enter no of students in class:"))
for i in range (n):
   ele=int(input("Enter Roll no:"))
   s.add(ele)
n1=int(input("Enter no of students present in class on day 1:"))
for i in range (n1):
   ele1=int(input("Enter Roll no:"))
   s1.add(ele1)
n2=int(input("Enter no of students present in class on day 2:"))
for i in range (n2):
   ele2=int(input("Enter Roll no:"))
   s2.add(ele2)
s4=s1.intersection(s2)
print("The Students present on both days:",s4)
s5=s1|s2
print("The Students present on either one days:",s5)
s6=s-s5
print("The Students not present on both days:",s6)