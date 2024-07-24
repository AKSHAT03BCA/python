choice=0
while(choice!=4):
    print("1.find area of circle")
    print("2.find area of triangle")
    print("3.find area  of square and rectangle")
    print("4.find simmple interest")
    print("5.exit")
    
choice=int(input("enter the chooice "))
if choice == 1:
    pi=3.14   #find area of circle
    radius=float(input("enter the value of radius"))
    area=pi*radius*radius
    print("area of a circle = %.2f" %area)
    print("circumfarence of a circle =%.2f"%circumfarence)
elif choice == 2:
    a=float(input("enter the value of first side"))
    b=float(input("enter the value of second side")) 
    c=float(input("enter the value of third side"))
    
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))*0.5
    print('area of triangle is %0.2f'%area)
elif  choice == 3:
    side=int(input("enter side length oof square : "))
    area_square=side*side
    print("area of square =",area_square)
    width=int(input("enter value of width"))
    height=int(input("enter the value of length"))
    area=height*width
    perimeter=2*(width+height)
    print("area of rectangle is: %.2f"%area)
    print("perimeter is: %.2f"%area)
elif choice == 4:
    p=int(input("enter p:"))
    r=int(input("enter r:"))
    n=int(input("enter n:"))
    i=(p*r*n)/100
    print(i)    
elif choice==5:
     exit()
else:
    print("bye bye")