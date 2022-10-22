import turtle
import matplotlib.pyplot as plt

print("-------For Printing The Shape You Have To Put Number-------")
print("For Creation Of Triangle Press [1]:--")
print("For Creation Of Square Shape   [2]:--")
print("For Creation Of Pentagon Shape [3]:--")
print("           TO Exit             [4]:--")
a = int(input("Enter Number"))
for j in a:
   if a==1:
      def tri(side):
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
      print(a)
      a.Screen()

      side = 300

      for i in range(10):
         tri(side)
         side -= 30

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
   
   elif a==3:
      sp = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
      sp.append(sp[0]) 
      s1, s2 = zip(sp)
      plt.figure()
      plt.plot(s1,s2) 
      plt.show() 
         
   elif a==4:
      break
   
   else:
      break














































     

