cero=[[0,1,1,1,0],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [1,0,0,0,1],
      [0,1,1,1,0]]

uno=[[0,0,1,0,0],
     [0,1,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,0,1,0,0],
     [0,1,1,1,0]]

dos=[[0,1,1,1,0],
     [1,0,0,0,1],
     [0,0,0,1,0],
     [0,0,1,0,0],
     [0,1,0,0,0],
     [1,0,0,0,0],
     [1,1,1,1,1]]

tres=[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0]]

cuatro=[[1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,1],
        [0,0,0,0,1],
        [0,0,0,0,1]]

cinco=  [[1,1,1,1,1],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,1,1,1,1],
         [0,0,0,0,1],
         [0,0,0,0,1],
         [1,1,1,1,1]]

seis=   [[1,1,1,1,1],
         [1,0,0,0,0],
         [1,0,0,0,0],
         [1,1,1,1,1],
         [1,0,0,0,1],
         [1,0,0,0,1],
         [1,1,1,1,1]]

nuevo=[[0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
x=5
y=7 
for i in range(y):
    for j in range(x):
        nuevo[i][j]=int(input("ingresa un numero"))

if(nuevo==uno):
     print("El valor es 1")
elif(nuevo==dos):
     print("El valor es 2")
elif(nuevo==tres):
     print("El valor es 3")
elif(nuevo==cuatro):
     print("El valor es 4")
elif(nuevo==cinco):
     print("El valor es 5")
elif(nuevo==seis):
     print("El valor es 6")