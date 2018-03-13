import pylab as p


def mid(a,b,c):
    ra=sum((a-c)**2)
    rb=sum((b-c)**2)

    return 1.0/3.0*((ra+2.0*rb)/(ra+rb)*a+(2.0*ra+rb)/(ra+rb)*b)

def draw(a,b,color='k',**kwargs):

    p.plot((a[0],b[0]),(a[1],b[1]),color=color,**kwargs)

def scatter(a,c='k',**kwargs):
    p.scatter(a[0],a[1],c=c,**kwargs)

A=p.array((0,0,))
B=p.array((1,0,))
C=p.array((0,0.5))

AB=mid(A,B,C)
BC=mid(B,C,A)
CA=mid(C,A,B)

centroid=1.0/3.0*(A+B+C)

draw(A,B)
draw(B,C)
draw(C,A)

draw(AB,centroid)
draw(BC,centroid)
draw(CA,centroid)

scatter(0.5*(A+B))
scatter(0.5*(B+C))
scatter(0.5*(C+A))

scatter(centroid)

p.axis('equal')





