age=int(input("enter your age:"))
vip_member=bool(input("you are a vip member?:"))
have_invitation=bool(input("do you have invitation?:"))
if age>=18:
    if vip_member or have_invitation:
     print("you can enter the club")
else:
    print("you cannot enter the club")