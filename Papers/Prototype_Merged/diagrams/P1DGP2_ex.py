import pylab as p

def p2(X,f):

    p.vlines(X,0,f(X),linestyles='dashed')

    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]


        def g(x):
            return (f(x0)*(x1-x)*(x2-x)/((x1-x0)*(x2-x0))
                    +f(x1)*(x-x0)*(x2-x)/((x1-x0)*(x2-x1))
                    +f(x2)*(x-x0)*(x-x1)/((x2-x0)*(x2-x1)))
         

        x=p.linspace(x0,x2,101)
        p.plot(x,g(x),c="b",ls='-')


def p1dg(X,f):

    XM=[0]
    for k in range(len(X)-1):
        x0=X[k]
        x1=0.5*(X[k]+X[k+1])
        x2=X[k+1]


        def g(x):
            return (f(x0)*(x1+x2-2.0*x)/((x1-x0)*(x2-x0))
                    +f(x1)*(2.0*x-x0+x2)/((x1-x0)*(x2-x1))
                    +f(x2)*(2.0*x-x0-x1)/((x2-x0)*(x2-x1)))

        XM[-1]=max(XM[-1],g(x0))
        XM.append(g(x2))
         

        x=p.linspace(x0,x2,101)
        p.plot(x,g(x),c="b",ls='-')

    p.vlines(X,0,XM,linestyles='dashed')

        
def f(x):
    return p.exp(-(x-5)**2/10.0)*(2.5+p.sin(x)+p.cos(2*x+0.4))

X=p.array([0,1,2,3.5,7,9,10])


p2(X,f)
p.figure()
p1dg(X,f)
