import pylab as p
import matplotlib

matplotlib.ticker.rcParams['xtick.minor.size']=0


def p2(X,f):

    p.vlines(X,0,f(X),linestyles='dashed')

    XM=[f(X[0])]

    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]

        xa=0.25*(3*X[k]+X[k+1])
        xb=0.25*(X[k]+3*X[k+1])

        XM.append(X[k+1])

        def g(x):
            return (f(x0)*(x1-x)*(x2-x)/((x1-x0)*(x2-x0))
                    +f(x1)*(x-x0)*(x2-x)/((x1-x0)*(x2-x1))
                    +f(x2)*(x-x0)*(x-x1)/((x2-x0)*(x2-x1)))
         

        x=p.linspace(x0,x2,101)
        p.plot(x,g(x),c="b",ls='-')
        p.scatter(x0,f(x0),c='k')
        p.scatter(x1,f(x1),c='k')
        p.scatter(x2,f(x2),c='k')

        p.vlines(xa,0,g(xa),linestyles='dotted')
        p.vlines(xb,0,g(xb),linestyles='dotted')


    p.vlines(X,0,XM,linestyles='dashed')
    p.axis((X[0],X[-1],0,1.7))
    p.xticks([])
    p.yticks([0,1])

def p1dg(X,f):

    XM=[0]
    Xm=[0]
    p.hlines(0,X[0],X[-1])
    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]

        xa=0.25*(3*X[k]+X[k+1])
        xb=0.25*(X[k]+3*X[k+1])


        def g(x):
            return (f(x0)*(-x1-x2+2.0*x)/((x1-x0)*(x2-x0))
                    +f(x1)*(-2.0*x+x0+x2)/((x1-x0)*(x2-x1))
                    +f(x2)*(2.0*x-x0-x1)/((x2-x0)*(x2-x1)))

        XM[-1]=max(XM[-1],g(x0))
        XM.append(max(0,g(x2)))
        Xm[-1]=min(Xm[-1],g(x0))
        Xm.append(min(g(x2),0))
         

        x=p.linspace(x0,x2,101)
        p.plot(x,g(x),c="b",ls='-')
        p.scatter(x0,g(x0),c='k')
        p.scatter(x2,g(x2),c='k')

#        p.vlines(xa,min(0,g(xa)),max(0,g(xa)),linestyles='dotted')
#        p.vlines(xb,min(0,g(xb)),max(0,g(xb)),linestyles='dotted')
        p.vlines(xa,-1.5,1.5,linestyles='dotted')
        p.vlines(xb,-1.5,1.5,linestyles='dotted')
        

    p.vlines(X,-1.5,1.5,linestyles='dashed')
    p.axis((X[0],X[-1],-1.5,1.5))

    p.xticks([])
    p.yticks([-1.5,0,1.5])

def p0(X,f):
    XM=[0]
    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]

        xa=0.25*(3*X[k]+X[k+1])
        xb=0.25*(X[k]+3*X[k+1])

        def g(x):
            return f(x1)*p.ones(x.shape)

        XM[-1]=max(XM[-1],g(x0))
        XM.append(g(x2))
         

        x=p.linspace(x0,x2,101)
        p.plot(x,g(x),c="b",ls='-')

        p.vlines(xa,0,f(x1),linestyles='dotted')
        p.vlines(xb,0,f(x1),linestyles='dotted')

        p.scatter(x1,f(x1),c='k')

    p.vlines(X,0,XM,linestyles='dashed')
    p.axis((X[0],X[-1],0,1))
    p.xticks([])
    p.yticks([0,1])

def cv(X,f):
    XM=[0]
    for k in range(len(X)-1):

        x0=X[k]
        xa=0.25*(3*X[k]+X[k+1])
        x1=0.5*(X[k]+X[k+1])
        xb=0.25*(X[k]+3*X[k+1])
        x2=X[k+1]

        XM[-1]=max(XM[-1],f(x0))
        XM.append(f(x2))


        x=p.linspace(x0,xa,26)
        p.plot(x,f(x0)*p.ones(x.shape),c="b",ls='-')
        
        x=p.linspace(xa,xb,51)
        p.plot(x,f(x1)*p.ones(x.shape),c="b",ls='-')

        x=p.linspace(xb,x2,26)
        p.plot(x,f(x2)*p.ones(x.shape),c="b",ls='-')

        p.vlines(xa,0,max(f(x0),f(x1)),linestyles='dotted')
        p.vlines(xb,0,max(f(x2),f(x1)),linestyles='dotted')

        p.scatter(x0,f(x0),c='k')
        p.scatter(x1,f(x1),c='k')
        p.scatter(x2,f(x2),c='k')

    p.vlines(X,0,XM,linestyles='dashed')

    p.xticks([])
    p.yticks([0,1.5])

    p.axis((X[0],X[-1],0,1.5))


def u(X,f,f1,f2): 

    F=matplotlib.ticker.FixedFormatter(['FE$_%d$'%(i+1) for i in range(len(X)-1)])
    L=matplotlib.ticker.FixedLocator([0.5*(X[k]+X[k+1]) for k in range(len(X)-1)])

    XM=[0]
    Xm=[0]

    p.hlines(0,X[0],X[-1])

    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]
        xa=0.25*(3*X[k]+X[k+1])
        xb=0.25*(X[k]+3*X[k+1])

        def g(x):
            return (f(x0)*(-x1-x2+2.0*x)/((x1-x0)*(x2-x0))
                    +f(x1)*(-2.0*x+x0+x2)/((x1-x0)*(x2-x1))
                    +f(x2)*(2.0*x-x0-x1)/((x2-x0)*(x2-x1)))

        XM[-1]=max(XM[-1],g(x0)*f1(x1)*f2(x0))
        XM.append(max(0,g(x2))*f1(x1)*f2(x2))
        Xm[-1]=min(Xm[-1],g(x0)*f1(x1)*f2(x0))
        Xm.append(min(g(x2),0)*f1(x1)*f2(x2))

        x=p.linspace(x0,xa,26)
        p.plot(x,f2(x0)*f1(x1)*g(x),c="b",ls='-')

#        p.vlines(xa,0,max(f2(x0),f2(x1))*f1(x1)*g(xa),linestyles='dotted')
    
        x=p.linspace(xa,xb,51)
        p.plot(x,f2(x1)*f1(x1)*g(x),c="b",ls='-')

#        p.vlines(xb,0,max(f2(x2),f2(x1))*f1(x1)*g(xb),linestyles='dotted')
        p.vlines(xa,-0.5,0.5,linestyles='dotted')
        p.vlines(xb,-0.5,0.5,linestyles='dotted')

        x=p.linspace(xb,x2,26)
        p.plot(x,f2(x2)*f1(x1)*g(x),c="b",ls='-')

        p.scatter(x0,f2(x0)*f1(x1)*g(x0),c='k')
        p.scatter(xa,f2(x0)*f1(x1)*g(xa),c='k')
        p.scatter(xa,f2(x1)*f1(x1)*g(xa),c='k')
        p.scatter(xb,f2(x1)*f1(x1)*g(xb),c='k')
        p.scatter(xb,f2(x2)*f1(x1)*g(xb),c='k')
        p.scatter(x2,f2(x2)*f1(x1)*g(x2),c='k')
        

    print XM

    p.vlines(X,-0.5,0.5,linestyles='dashed')
    p.xticks(X,'')
    p.yticks([0,-.5,.5])
    p.gca().xaxis.set_minor_locator(L)
    p.gca().xaxis.set_minor_formatter(F)
    p.axis((X[0],X[-1],-.5,.5))





def f(x):
    return 1.2-(0.25*x)**3+0.2*p.sin(p.pi*x)+0.01*p.cos(3*x+0.2)

def f2(x):
    return 0.9-0.2*x

def f3(x):
    return 0.9-0.6*(abs((x-1.7)/2.3))**2-0.5*p.cos(x)-0.8*(x>2)+0.5*(x>3)


X=p.array([0,1,2.5,4.0])


p.figure(figsize=(16,8))
p.subplot(5,1,1)
p2(X,f)
p.ylabel('$p$')
p.subplot(5,1,2)
p1dg(X,f)
p.ylabel(r'$\frac{\partial p}{\partial x}$')
p.subplot(5,1,3)
p0(X,f2)
p.ylabel(r'$\bf{K}$')
p.subplot(5,1,4)
cv(X,f3)
p.ylabel(r'$\lambda_k$')
p.subplot(5,1,5)
u(X,f,f2,f3)
p.ylabel('$u_k$')

p.savefig('overlapping_cartoon.eps')
p.savefig('overlapping_cartoon.pdf')

