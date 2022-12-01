points = int(input ("Enter the number of polygon points: "))
n = points

if n<3:
    quit("Incorrect input data! Minimal number of points is 3. Please, try once more!")
#0_Variables
lst_out = []
lstX =[]
lstY = []

A = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0
xT = 0
yT = 0
I_Tx = 0
I_Ty = 0
I_Txy = 0

print("Please, enter coordinates of the points following COUNTER clockwise direction.")
#1_Input and creating list of X and Y
for i in range(n):
    lst_xy =[]
    xy = input("Enter X and Y coordinates, using coma as a delimiter for P"+str(i+1)+": ")
    try:
        x = xy.split(",")[0].replace(" ","")
        y = xy.split(",")[1].replace(" ","")
        lstX.append(float(x))
        lstY.append(float(y))
    except:
        quit("Incorrect input data! Two coordinates with the coma as a delimeter are needed. Please, try once more!")

#2_Calculating geometric chararasterustucs
lstX.append(lstX[0])
lstY.append(lstY[0])

for i in range(n):
    x0 =lstX[i]
    x1 =lstX[i+1]
    y0 =lstY[i]
    y1 =lstY[i+1]
    A= A+0.5*((x0+x1)*(y1-y0))
    Sx= Sx-(1/6)*(x1-x0)*(y1**2+y1*y0+y0**2)
    Sy= Sy+(1/6)*(y1-y0)*(x1*x1+x1*x0+x0*x0)
    Ix= Ix-(1/12)*(x1-x0)*(y1**3+y1**2*y0+y0**2*y1+y0**3)
    Iy= Iy+(1/12)*(y1-y0)*(x1**3+x1**2*x0+x0**2*x1+x0**3)
    Ixy = Ixy-(1/24)*(y1-y0)*(y1*(3*x1**2+2*x1*x0+x0**2)+y0*(3*x0**2+2*x1*x0+x1**2))
    
if A==0:
        quit("Incorrect input data! Points do not form a polygon. Please, try once more!")
elif A<0:
        quit("Incorrect input data! The points must be ordered COUNTER clockwise. Please, try once more!")

xT = Sy/A
yT = Sx/A
I_Tx = Ix-yT**2*A
I_Ty = Iy-xT**2*A
I_Txy= Ixy+xT*yT*A

#Output_1_(Table with coordinates)
print ("")
print ("Point |  X    |   Y")
print ("______________________")
for i in range(points):
    print ("P"+str(i+1)+ "   |   "+str(lstX[i])+ "  | "+ str(lstY[i]))
    print ("----------------------")
print ()

#Output_2_(Geometric charasteristics)
print("Area: "+str(round(A,3)))
print("Sx: "+str(round(Sx,3)))
print("Sy: "+str(round(Sy,3)))
print("Ix: "+str(round(Ix,3)))
print("Iy: "+str(round(Iy,3)))
print("Ixy: "+str(round(Ixy,3)))
print("xT: "+str(round(xT,3)))
print("yT: "+str(round(yT,3)))
print("I_Tx: "+str(round(I_Tx,3)))
print("I_Ty: "+str(round(I_Ty,3)))
print("I_Txy: "+str(round(I_Txy,3)))