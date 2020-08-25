import numpy as np
import math
import time
import tkinter as tk
import random as rm

class particle():
    def __init__(self, p, v,r ,colour):
        self.r=r
        self.shape = canvas.create_oval(p[0]-self.r, p[1]-self.r, p[0]+self.r, p[1]+self.r, fill = colour,outline = colour)
        self.p = np.array([float(i) for i in p]) #position
        self.v =np.array([float(i) for i in v]) #velocity
        self.oldv = np.copy(v)


    def update(self, delay):
        self.v=self.oldv
        self.p += (self.v*delay)
        canvas.move(self.shape, self.v[0]*delay, self.v[1]*delay)

        if not self.r<=self.p[0]<w-self.r: #keeps it within boundaries
            self.v *= np.array([-1,1])
        if not self.r<=self.p[1]<h-self.r:
            self.v *= np.array([1,-1])

    def collide(self, other):
        x = self.p - other.p
        dist = np.sqrt(x.dot(x))  # checks distance
        if 0 < dist < self.r+other.r:
            self.oldv=self.v- (2*other.r**2)/(self.r**2+other.r**2)*np.dot(self.v-other.v,dist)/(np.linalg.norm(dist)**2.) * dist


class test(particle):
    def __init__(self, p, v, r, colour):
        super().__init__(p,v,r,colour)
        self.oldp=np.copy(p)
        self.ccount=0
        self.dcount=0

    def graph(self):
        self.ccount += 1
        self.dcount += (abs(self.p[0]-self.oldp[0])**2 + abs(self.p[1]-self.oldp[1])**2)**(1/2)

        print(self.ccount)

    def collide(self, other):
        x = self.p - other.p
        dist = np.sqrt(x.dot(x))  # checks distance
        if 0 < dist < self.r + other.r:
            self.oldv = self.v - (2 * other.r ** 2) / (self.r ** 2 + other.r ** 2) * np.dot(self.v - other.v, dist) / (
                        np.linalg.norm(dist) ** 2.) * dist
            self.graph()



#---------------------------------------------------------------------------------
def main():
    [[j.collide(i) for i in particles] for j in particles]

    [i.update(FPS) for i in particles]
    canvas.after(100,main)

#---------------------------------------------------------------------------------
#creates the window
ni=20
R=40
w,h=ni*R,ni*R
root = tk.Tk()
root.title("Elastic collision")
canvas = tk.Canvas(root, width = w, height = h)
canvas.pack()
canvas.config(bg="white")

#---------------------------------------------------------------------------------
#set variables
V=100
FPS = 1/60
NoParticles = 50
r_=5
particles = [test([10,h-10], [V,V],r_,'red')]
particles.extend([particle([rm.randint(r_,w-r_),rm.randint(r_,h-r_)], [rm.randint(-V,V),rm.randint(-V,V)],r_,'blue') for i in range(NoParticles)])

#---------------------------------------------------------------------------------

main()

root.mainloop()
