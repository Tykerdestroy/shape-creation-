import turtle
import matplotlib.pyplot as plt

 
  



print("-------For Printing The Shape You Have To Put Number-------")
print("For Creation Of Triangle shape [1]:--")
print("For Creation Of Square shpae   [2]:--")
print("For Creation Of Pentagon shape [3]:--")
print("For Creation Of parallelogram shape [4]:--")
print("           TO Exit             [5]:--")
a = int(input("Enter Number"))
for j in a:
   if a==1:
      def tri(side):
         #For Loop For creating The triagle shape of coding.
         for i in range(3):
            my_pen.fd(side)
            my_pen.left(120)
            side -= 10


      a = turtle.Screen()

      a.bgcolor("black")
      a.title("Turtle")

      my_pen = turtle.Turtle()
      my_pen.color("white")
      a = turtle.Screen()

      side = 300

      for i in range(10):
         tri(side)
         side -= 30
   
   #for creating the shape of square the loop of the code helps in creating the shape of it.
   elif a==2:
      def squa(side):
         for i in range(4):
            my_pen.fd(side)
            my_pen.left(90)
            side -= 5

      b = turtle.Screen()
      b.bgcolor("green")
      b.title("Turtle")

      my_pen = turtle.Turtle()
      my_pen.color("orange")
      b = turtle.Screen()           

      side = 200
      for i in range(10):
         squa(side)
         side-= 20
   
   #to exit the line of code it ends with the code of line break.
   elif a==3:
      sp = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
      sp.append(sp[0]) 
      s1, s2 = zip(sp)
      plt.figure()
      plt.plot(s1,s2) 
      plt.show() 
   elif a==4:  
       a = int(input("Enter rows:-"))
       b = int(input("Enter Columns:-"))

       for i in range(0, a):
           for j in range(1, i+1):
               print(" ", end="")
          for j in range(0, b):
               print("*", end="")
          print()
   elif a==5:
      break
   
   else:
      break














































     

