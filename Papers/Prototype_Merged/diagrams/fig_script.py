import pylab as p

import matplotlib as mpl
from copy import deepcopy

font= {'family':'times',
       'size':16}

mpl.rc('font',**font)

def av(*args):
    return sum(args)/float(len(args))

class Triangle(object):
    def __init__(self,p1,p2,p3):
        self.p=[p.array(pnt) for pnt in (p1,p2,p3)]

        self.c=(self.p[0]+self.p[1]+self.p[2])/3.0
        

    def plot(self,**kwargs):
        p.plot([self.p[0][0],self.p[1][0],self.p[2][0],self.p[0][0]],
               [self.p[0][1],self.p[1][1],self.p[2][1],self.p[0][1]],**kwargs)

    def mark(self,a=0.0,degree=1,**kwargs):

        if degree==0:
            S=p.scatter(self.c[0],self.c[1],**kwargs)
            return S

        def ac(pnt):
            return pnt+a*(self.c-pnt)/p.sqrt(sum((self.c-pnt)**2))
        
        
        for pnt in self.p:
            r=pnt+a*(self.c-pnt)/p.sqrt(sum((self.c-pnt)**2))
            S=p.scatter(r[0],r[1],**kwargs)

        if degree==2:
           for pnt in (av(ac(self.p[0]),ac(self.p[1])),
                       av(ac(self.p[2]),ac(self.p[1])),
                       av(ac(self.p[0]),ac(self.p[2]))):
               p.scatter(pnt[0],pnt[1],**kwargs)

        return S

    def subpart(self,degree=1,**kwargs):
        p1=self.p[0]
        p2=self.p[1]
        p3=self.p[2]
        if degree==2:
            for pnts in ((p1,av(p1,p2),av(p1,p3)),
                         (p2,av(p2,p1),av(p2,p3)),
                         (p3,av(p3,p2),av(p1,p3)),
                         (av(p2,p3),av(p1,p2),av(p1,p3))):
                Triangle(*pnts).subpart(**kwargs)
        else:
            for r in (av(p1,p2),av(p2,p3),av(p3,p1)):
                p.plot([r[0],self.c[0]],
                       [r[1],self.c[1]],
                       **kwargs)



p.close(1)
p.close(2)
p.close(3)
p.close(4)

                         
pa=(-.2,0)
pb=(-1,0)
pc=(1,0)
pd=(-0.5,p.sqrt(1.25)) 
pe=(0.5,p.sqrt(1.25))       
pf=(-0.5,-p.sqrt(1.25))
pg=(0.5,-p.sqrt(1.25))            


T1=Triangle(pa,pb,pd)
T2=Triangle(pa,pb,pf)
T3=Triangle(pa,pc,pe)
T4=Triangle(pa,pc,pg)
T5=Triangle(pa,pd,pe)
T6=Triangle(pa,pf,pg)



p1=av(p.array(pa),p.array(pf))
p2=av(p.array(pa),p.array(pb))
p3=av(p.array(pb),p.array(pf))
p4=av(p.array(pf),p.array(pg))
p5=av(p.array(pa),p.array(pg))

pa=p.array(pa)
pb=p.array(pb)
pf=p.array(pf)
pg=p.array(pg)


pnts=(av(p1,pa),
      av(pa,p1,p2),
      av(p1,p2),
      av(pa,pb,pf),
      av(p1,p3),
      av(p1,p3,pf),
      av(p1,pf),
      av(p1,pf,p4),
      av(p1,p4),
      av(pa,pf,pg),
      av(p1,p5),
      av(p1,pa,p5),
      )
      

if (False):
    p.figure(2)
    p.axis('off')

    smx=80

    p.fill([pnt[0] for pnt in pnts],
           [pnt[1] for pnt in pnts],
           ec='none',fc='gray',zorder=1)

    for T in (T1,T2,T3,T4,T5,T6):
        T.subpart(2,c='k',ls=':',zorder=2)
        T.plot(c='k',zorder=3)
        T.mark(degree=2,s=smx,c='#E0E0E0',edgecolors='k',zorder=4)


    p.savefig('CVFEM-diag.eps')
    p.savefig('CVFEM-diag.pdf')


if (False):
    p.figure(1)
    p.axis('off')

    smx=130

    pdof='Pressure DOF'
    vdof='Velocity DOF'

    for T in (T1,T2,T3,T4,T5,T6):

        T.plot(c='k',zorder=3,label=None)
        P=T.mark(degree=2,s=smx,c='#E0E0E0',edgecolors='k',zorder=4)
        V=T.mark(0.1,s=smx,degree=1,c='w',edgecolors='k',zorder=5)


        P=T.mark(degree=1,s=130,c='k',edgecolors='k',zorder=4)
        V=T.mark(a=0.07,degree=0,s=60,c='w',edgecolors='k',zorder=5)



        p.legend((P,V),(pdof,vdof),frameon=False,loc=3,bbox_to_anchor=(0.7,0.7),scatterpoints=1)

        p.savefig('P1DGP2-diag.eps')
        p.savefig('P1DGP2-diag.pdf')


a=p.array((0.0,0.0))
b=p.array((-0.5,0.7))
c=p.array((0.3,1.0))
d=p.array((0.9,0.2))
e=p.array((0.9,-0.4))
f=p.array((0.3,-1.0))
g=p.array((-0.3,-0.4))

TX=Triangle(a,b,c)
TY=Triangle(a,c,d)
TZ=Triangle(a,d,e)
TA=Triangle(a,e,f)
TB=Triangle(a,f,g)
TC=Triangle(a,g,b)

c1=av(a,b,c)
c2=av(a,c,d)

def subm1(A,B,C):

    P=av(A,B)
    X=av(A,C)
    Y=av(B,C)

    return (P,
            av(A,B,C),
            X,
            A)


def subm2(A,B,C):

    P=av(av(A,B),A)
    X=av(av(A,C),A)
    Y=av(B,C)

    return (P,
            av(av(A,B),av(A,C),A),
            X,
            A)

def subm(A,B,C):

    P=av(A,B)
    X=av(A,C)
    Y=av(B,C)

    return (av(P,A),
            av(P,A,X),
            av(P,X),
            av(P,X,Y),
            av(P,Y),
            av(P,B,Y),
            av(P,B))

def subfill(S,**kwargs):
    p.fill([pnt[0] for pnt in S],
          [pnt[1] for pnt in S],
          **kwargs)




TYp=deepcopy(TY)
for k in range(3):
    TYp.p[k]=TYp.p[k]+p.array(0.08*(c2-c1))

TYp.c=av(TYp.p[0],TYp.p[1],TYp.p[2])


S1=subm1(a,c,b)
S2=subm1(a,d,c)
S3=subm1(a,d,e)
S4=subm1(a,e,f)
S5=subm1(a,f,g)
S6=subm1(a,g,b)
S2p=subm(TYp.p[0],TYp.p[1],TYp.p[2])

SS2=subm(a,d,c)
SS3=subm(a,d,e)

SSS1=subm2(a,c,b)
SSS2=subm2(a,d,c)
SSS3=subm2(a,d,e)
SSS4=subm2(a,e,f)
SSS5=subm2(a,f,g)
SSS6=subm2(a,g,b)
 

p.figure(3)
p.axis([-0.52,1.,-1.03,1.03])
p.axis('off')
vdof='Velocity DOF'
pdof='Pressure DOF'


for S in (S1,S2,S3,S4,S5,S6):
    subfill(S,fc='gray')

for T in (TX,TY,TZ,TA,TB,TC):
    T.subpart(1,c='k',ls=':',zorder=2)
    T.plot(c='k',zorder=3,label=None)
    V=T.mark(a=0.07,degree=0,s=60,c='w',edgecolors='k',zorder=5)
    P=T.mark(degree=1,s=130,c='k',edgecolors='k',zorder=4)

p.savefig('p0dgp1-cont-sat.eps')
p.savefig('p0dgp1-cont-sat.pdf')

p.figure(4)
p.axis('off')

subfill(S1,fc='gray')
#subfill(S2p,fc='gray')

for T in (TX,TYp):
    T.subpart(1,c='k',ls=':',zorder=2)
    T.plot(c='k',zorder=3,label=None)
    V=T.mark(a=0.07,degree=2,s=30,c='w',edgecolors='k',zorder=5)
    P=T.mark(a=0.07,degree=1,s=130,c='k',edgecolors='k',zorder=4)

p.legend((P,V),(pdof,vdof),frameon=False,loc=3,bbox_to_anchor=(0.55,0.7),scatterpoints=1)

p.savefig('p2dgp1-dg-sat.eps')
p.savefig('p2dgp1-dg-sat.pdf')


p.figure(5)
p.axis([-0.52,1.,-1.03,1.03])
p.axis('off')
vdof='Velocity DOF'
pdof='Pressure DOF'


for S in (SS2,SS3):
    subfill(S,fc='gray')
for S in (SSS1,SSS2,SSS3,SSS4,SSS5,SSS6):
    subfill(S,fc='lightgray')

for T in (TX,TY,TZ,TA,TB,TC):
    T.subpart(2,c='k',ls=':',zorder=2)
    T.plot(c='k',zorder=3,label=None)
    V=T.mark(a=0.07,degree=1,s=60,c='w',edgecolors='k',zorder=4)
    P=T.mark(degree=2,s=60,c='k',edgecolors='k',zorder=5)

p.savefig('p1dgp2-cont-sat.eps')
p.savefig('p1dgp2-cont-sat.pdf')
