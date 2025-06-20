marks= int(input("enter your marks:"))

match marks:
    case _ if marks>=90:
     print("excellent")
    case _ if marks>=75 and marks<=89:
     print("excellent")
    case _ if marks>=50 and marks<=74:
     print("average")
    case _ :
     print("fail")
     
     

 