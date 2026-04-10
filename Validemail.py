email=input("Enter Mail ID:")
if " " in email :
   print("Invalid Email(Contains Space)")
elif email.count("@")!=1:
   print("Invalid Email(Must Contains exactly one @)")
elif (email[0].isupper() or email[0].isdigit()):
   print("Invalid Email(Mail Should not Start with uppercase or Number)")
else:
   at_pos=email.index("@")
   dot_pos=email.rindex('.')
   if at_pos==0:
      print("Invalid Email(No username before @)")
   elif dot_pos<at_pos+2:
      print("Invalid Email(Invalid Domain Name)")
   elif dot_pos==len(email)-1:
      print("Invalid  Email(No Domain Extension)")
   else:
      print("Valid MAIL_ID")