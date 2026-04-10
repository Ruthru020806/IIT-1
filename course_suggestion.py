s1=set()
s2=set()
n1=int(input("Enter no of intrested course by user 1:"))
for i in range (n1):
   cou1=input("Enter Course Name:")
   s1.add(cou1)
n2=int(input("Enter no of intrested course by user 2:"))
for i in range (n2):
   cou2=input("Enter Course Name:")
   s2.add(cou2)
s3=s1 & s2
print("Common intreseted Course:",s3)
s4=s1-s2
print("Suggested course for user2 from user1 :",s4)
s5=s2-s1
print("Suggested course for user1 from user2 :",s5)