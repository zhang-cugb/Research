import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
import numpy as n
import pylab as p


X1=[-0.5,0.5,0.0]
Y1=[0,0,n.sqrt(2)]

ax.plot3D((X1[0],X1[1],X1[2],X1[0]),(Y1[0],Y1[1],Y1[2],Y1[0]),c='k')

for k in range(3):
    avY=(Y1[k%3]+Y1[(k+1)%3])/2.0
    avX=(X1[k%3]+X1[(k+1)%3])/2.0
    CX=sum(X1)/3.0
    CY=sum(Y1)/3.0

    ax.plot3D((avX,CX),(avY,CY),c='k',ls=':')

k=0
av0Y=(Y1[k%3]+Y1[(k+1)%3])/2.0
av0X=(X1[k%3]+X1[(k+1)%3])/2.0
k=1
av1Y=(Y1[k%3]+Y1[(k+1)%3])/2.0
av1X=(X1[k%3]+X1[(k+1)%3])/2.0

MX=n.array([[av0X,CX],
    [X1[1],av1X]])
MY=n.array([[av0Y,CY],
    [Y1[1],av1Y]])

def f(x,y):
    return 0.4-0.1*x+0.2*y

Z=f(MX,MY)

ax.plot_surface(MX,MY,Z)



X=n.array((X1[1],X1[2]))
Y=n.array((Y1[1],Y1[2]))
Z=f(X,Y)
ax.plot3D(X,Y,zs=Z,c='k',ls='--')
X=n.array((X1[1],X1[0]))
Y=n.array((Y1[1],Y1[0]))
Z=f(X,Y)
ax.plot3D(X,Y,zs=Z,c='k',ls='--')

ax.plot((av0X,av0X),(av0Y,av0Y),zs=(0,f(av0X,av0Y)),c='k')
ax.plot((av1X,av1X),(av1Y,av1Y),zs=(0,f(av1X,av1Y)),c='k')

for k in range(3):
    ax.plot((X1[k],X1[k]),(Y1[k],Y1[k]),zs=(0,f(X1[k],Y1[k])),c='k')


ax.xaxis.set_ticklabels('')
ax.yaxis.set_ticklabels('')
ax.zaxis.set_ticklabels('')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$u(x,y)$')

ax.text3D(CX-0.05,CY-0.05,0,'C')

ax.text3D(X1[0],Y1[0],f(X1[0],Y1[0]),'F')
ax.text3D(X1[2],Y1[2],f(X1[2],Y1[2]),'G')
ax.text3D(X1[1],Y1[1],f(X1[1],Y1[1]),'E')
for k,s in enumerate(('A','B','D')):
    ax.text3D(X1[(k+1)%3]-0.05,Y1[(k+1)%3]-0.05,0,s)


ax.view_init(20,-35)

p.savefig('overlapping.eps')
p.savefig('overlapping.pdf')
