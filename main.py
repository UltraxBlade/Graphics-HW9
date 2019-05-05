from Graphics import *
from matrix import *
from display import *

homeTest=True
newMode=True

def oldParse(filename,edges,polys,transform,img,zbuffer,color):
    f=open(filename,"r")
    script=f.read().split("\n")
    f.close()
    i=0
    while i<len(script):
        if script[i]=="line":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addEdge(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="triangle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addPoly(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8])
            i+=1
        elif script[i]=="ident":
            transform=I(4)
        elif script[i]=="apply":
            edges=multMatrix(transform,edges)
            polys=multMatrix(transform,polys)
        elif script[i]=="quit":
            return
        elif script[i]=="move":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            transform=multMatrix(translate(coords[0],coords[1],coords[2]),transform)
            i+=1
        elif script[i]=="scale":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=float(coords[k])
            transform=multMatrix(scale(coords[0],coords[1],coords[2]),transform)
            i+=1
        elif script[i]=="rotate":
            coords=script[i+1].split(" ")
            transform=multMatrix(rotate(coords[0],float(coords[1])),transform)
            i+=1
        elif script[i]=="save":
            clear(img)
            drawLines(img,edges,color)
            drawPolys(img,polys,color)
            if homeTest:
                save_ppm(img,script[i+1])
            else:
                save_extension(img,script[i+1])
            i+=1
        elif script[i]=="circle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            circle(edges,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="hermite":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            hermite(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="bezier":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            bezier(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="box":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            box(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="sphere":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            sphere(polys,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="torus":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            torus(polys,coords[0],coords[1],coords[2],coords[3],coords[4])
            i+=1
        elif script[i]=="clear":
            edges[0]=[]
            edges[1]=[]
            edges[2]=[]
            edges[3]=[]
            polys[0]=[]
            polys[1]=[]
            polys[2]=[]
            polys[3]=[]
        elif script[i]=="display" and not homeTest:
            clear(img,zbuffer)
            drawLines(img,zbuffer,edges,color)
            drawPolys(img,zbuffer,polys,color)
            display(img)
        i+=1

class WorldStack:
    def __init__(self):
        self.L=[I(4)]
    def push(self):
        self.L.append([r[:] for r in self.L[len(self.L)-1]])
    def peek(self):
        return self.L[len(self.L)-1]
    def pop(self):
        return self.L.pop(len(self.L)-1)

def newParse(filename,world,img,zbuffer,color):
    f=open(filename,"r")
    script=f.read().split("\n")
    f.close()
    i=0
    while i<len(script):
        edges=[[],[],[],[]]
        polys=[[],[],[],[]]
        transform=world.peek()
        if script[i]=="line":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addEdge(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="triangle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            addPoly(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8])
            i+=1
            
        elif script[i]=="move":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            transform=multMatrix(transform,translate(coords[0],coords[1],coords[2]))
            for r in range(len(world.peek())):
                world.peek()[r]=transform[r]
            i+=1
        elif script[i]=="scale":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=float(coords[k])
            transform=multMatrix(transform,scale(coords[0],coords[1],coords[2]))
            for r in range(len(world.peek())):
                world.peek()[r]=transform[r]
            i+=1
        elif script[i]=="rotate":
            coords=script[i+1].split(" ")
            transform=multMatrix(transform,rotate(coords[0],float(coords[1])))
            for r in range(len(world.peek())):
                world.peek()[r]=transform[r]
            i+=1
        elif script[i]=="circle":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            circle(edges,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="hermite":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            hermite(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="bezier":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            bezier(edges,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7])
            i+=1
        elif script[i]=="box":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            box(polys,coords[0],coords[1],coords[2],coords[3],coords[4],coords[5])
            i+=1
        elif script[i]=="sphere":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            sphere(polys,coords[0],coords[1],coords[2],coords[3])
            i+=1
        elif script[i]=="torus":
            coords=script[i+1].split(" ")
            for k in range(len(coords)):
                coords[k]=int(coords[k])
            torus(polys,coords[0],coords[1],coords[2],coords[3],coords[4])
            i+=1
        elif script[i]=="push":
            world.push()
        elif script[i]=="pop":
            world.pop()
        elif script[i]=="save":
            if homeTest:
                save_ppm(img,script[i+1])
            else:
                save_extension(img,script[i+1])
            i+=1
        elif script[i]=="display" and not homeTest:
            display(img)
        elif script[i]=="quit":
            return
        elif script[i]=="clear":
            clear(img,zbuffer)
        elif script[i]=="parseOld":
            oldParse(script[i+1],edges,polys,I(4),img,zbuffer,drawColor)
            i+=1
        if len(edges[0])>0:
            edges=multMatrix(transform,edges)
            drawLines(img,zbuffer,edges,color)
        if len(polys[0])>0:
            polys=multMatrix(transform,polys)
            drawPolys(img,zbuffer,polys)
        i+=1

img=generate(501,501)
zbuffer=zbuffer(501,501,501)
drawColor=[0,0,0]
if not newMode:
    edges=[[],[],[],[]]
    polys=[[],[],[],[]]
    transform=I(4)
    oldParse("waluigiTriangles.txt",edges,polys,transform,img,zbuffer,drawColor)
else:
    world=WorldStack()
    newParse("script",world,img,zbuffer,drawColor)
