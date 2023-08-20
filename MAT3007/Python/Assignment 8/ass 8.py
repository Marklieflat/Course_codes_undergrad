import numpy as np
import matplotlib.pyplot as plt

#2a
def f(x):
    return x[0]**4+2/3*x[0]**3+1/2*x[0]**2-2*x[0]**2*x[1]+4/3*x[1]**2

def grad_f(x):
    return np.array([4*x[0]**3+2*x[0]**2+x[0]-4*x[0]*x[1],-2*x[0]**2+8/3*x[1]])

def hess_f(x):
    return np.array([[12*x[0]**2+4*x[0]+1-4*x[1],-4*x[0]],[-4*x[0],8/3]])

def gradient_method_backtrack(obj, grad, x0, tol=1e-5, sigma=0.5, gamma=0.1):
    x=[x0]
    d=[]
    alpha=[]
    k=0
    while np.linalg.norm(grad(x[k]))>tol:
        d.append(-grad(x[k]))
        alpha.append(1)
        #backtracking line search
        while obj(x[k]+alpha[k]*d[k])-obj(x[k])>-gamma*alpha[k]*np.linalg.norm(d[k])**2:
            alpha[k]*=sigma
        #end backtracing
    
        x.append(x[k]+alpha[k]*d[k])
        k+=1
    return x


def gradient_method_exact(obj, grad, x0, tol=1e-5, maxit=100, extol=1e-6,a=2):
    x=[x0]
    d=[]
    alpha=[]
    k=0
    while np.linalg.norm(grad(x[k]))>tol:
        d.append(-grad(x[k]))
        alpha.append(1)
        #exact line search by Golden section method
        it=0
        points=np.array([0,(3-np.sqrt(5))/2,(np.sqrt(5)-1)/2,1])*a
        vals=[f(points[i]*d[k]+x[k]) for i in range(4)]
        while it<maxit and np.abs(points[3]-points[0])>extol:
            it+=1
            if vals[1]<vals[2]:
                points[3]=points[2]
                vals[3]=vals[2]
                points[2]=points[1]
                vals[2]=vals[1]
                points[1]=points[0]*(np.sqrt(5)-1)/2+points[3]*(3-np.sqrt(5))/2
                vals[1]=f(points[1]*d[k]+x[k])
            else:
                points[0]=points[1]
                vals[0]=vals[1]
                points[1]=points[2]
                vals[1]=vals[2]
                points[2]=points[0]*(3-np.sqrt(5))/2+points[3]*(np.sqrt(5)-1)/2
                vals[2]=f(points[2]*d[k]+x[k])
        alpha[k]=points[1]
        #end exact
        
        x.append(x[k]+alpha[k]*d[k])
        k+=1
    return x

back_x=gradient_method_backtrack(f, grad_f, x0=np.array([3,3]), tol=1e-5, sigma=0.5, gamma=0.1)
print('Backtracking: '+str(len(back_x)))
print(back_x[-1])
print(f(back_x[-1]))
exact_x=gradient_method_exact(f, grad_f,  x0=np.array([3,3]), tol=1e-5, maxit=100, extol=1e-6,a=2)
print('Exact: '+str(len(exact_x)))
print(exact_x[-1])
print(f(exact_x[-1]))
         
plt.show()

#2b
x = np.arange(-3.5,3.5,0.1); y = np.arange(-3.5,4,0.1) 
X,Y = np.meshgrid(x,y)
Z=f(np.array([X,Y]))
plt.contour(X, Y, Z, 1000)
for x0 in [[-3,-3],[3,-3],[-3,3],[3,3],]:
    x=gradient_method_backtrack(f, grad_f, x0=np.array(x0), tol=1e-5, sigma=0.5, gamma=0.1)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('backtracking')
    plt.plot(np.array(x)[:,0],np.array(x)[:,1])
plt.show()

x = np.arange(-3.5,3.5,0.1); y = np.arange(-3.5,4,0.1) 
X,Y = np.meshgrid(x,y)
Z=f(np.array([X,Y]))
plt.contour(X, Y, Z, 1000)
for x0 in [[-3,-3],[3,-3],[-3,3],[3,3],]:
    x=gradient_method_exact(f, grad_f, x0=np.array(x0), tol=1e-5, maxit=100, extol=1e-6,a=2)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('exact')
    plt.plot(np.array(x)[:,0],np.array(x)[:,1])
plt.show()

#3b
def adagrad_method_backtrack(obj, grad, x0, eps=1e-6, m=25, tol=1e-5, sigma=0.5, gamma=0.1):
    x=[x0]
    d=[]
    D=[]
    alpha=[]
    k=0
    while np.linalg.norm(grad(x[k]))>tol:
        d.append(-grad(x[k]))
        D.append(np.zeros(len(x0)))
        
        tmk=np.max([0,k-m])
        D[k]=np.sqrt(eps+np.sum(np.array(d[tmk:])**2,axis=0))
        alpha.append(1)
        #backtracking line search
        while obj(x[k]+alpha[k]*d[k])-obj(x[k])>-gamma*alpha[k]*np.linalg.norm(d[k])**2:
            alpha[k]*=sigma
        #end backtracing
        x.append(x[k]+alpha[k]*d[k]/D[k])
        k+=1
    return x



x = np.arange(-3.5,3.5,0.1); y = np.arange(-3.5,4,0.1) 
X,Y = np.meshgrid(x,y)
Z=f(np.array([X,Y]))
plt.contour(X, Y, Z, 1000)

for x0 in [[-3,-3],[3,-3],[-3,3],[3,3],]:
    x=adagrad_method_backtrack(f, grad_f, x0=np.array(x0), eps=1e-6, m=25, tol=1e-5, sigma=0.5, gamma=0.1)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('adagrad')
    plt.plot(np.array(x)[:,0],np.array(x)[:,1])
plt.show()

#3c
x = np.arange(-3.5,3.5,0.1); y = np.arange(-3.5,4,0.1) 
X,Y = np.meshgrid(x,y)
Z=f(np.array([X,Y]))
plt.contour(X, Y, Z, 1000)

for m in [5,10,15,25,35,50,75,100,200,400]:
    x=adagrad_method_backtrack(f, grad_f, x0=np.array([-3,-3]), eps=1e-6, m=m, tol=1e-5, sigma=0.5, gamma=0.1)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('adagrad')
    plt.plot(np.array(x)[:,0],np.array(x)[:,1])
    print('mermory: '+str(m)+', numberof iterations: '+str(len(x)))
plt.show()

#4a
def newton_glob(obj, grad, hess, x0, gamma, gamma1, gamma2, sigma, tol):
    x=[x0]
    d=[]
    s=[]
    alpha=[]
    k=0
    alwaysNewtondirect=True
    alwaysaplha1=True
    while np.linalg.norm(grad(x[k]))>tol:
        d.append(-grad(x[k]))
        s.append(np.linalg.solve(hess(x[k]),d[k]))
        
        if d[k].T@s[k]>=gamma1*np.min([1,np.linalg.norm(s[k])**gamma2])*np.linalg.norm(s[k])**2:
            d[k]=s[k]
        elif alwaysNewtondirect:
            print('Not always Newton direction')
            alwaysNewtondirect=False
        alpha.append(1)
        #backtracking line search
        while obj(x[k]+alpha[k]*d[k])>obj(x[k])-gamma*alpha[k]*np.linalg.norm(d[k])**2+tol:
            alpha[k]*=sigma
        if alpha[k]<1-tol and alwaysNewtondirect:
            alwaysNewtondirect=False
            print('Not always full step size')
        #end backtracing
        x.append(x[k]+alpha[k]*d[k])
        k+=1
    return x


def Rosenbrock(x):
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

def grad_Rosenbrock(x):
    return np.array([-400*(x[1]-x[0]**2)*x[0]-2*(1-x[0]),200*(x[1]-x[0]**2)])


def hess_Rosenbrock(x):
    return np.array([[-400*x[1]+1200*x[0]**2+2,-400*x[0]],[-400*x[0],200]])

newton_x=newton_glob(Rosenbrock, grad_Rosenbrock,hess_Rosenbrock, x0=np.array([-1,-0.5]), gamma=1e-4, gamma1=1e-6, gamma2=0.1, sigma=0.5, tol=1e-7)
grad_x=gradient_method_backtrack(Rosenbrock, grad_Rosenbrock,x0=np.array([-1,-0.5]), tol=1e-7, sigma=0.5, gamma=1e-4)

print('number of Newton iterations: '+str(len(newton_x)))
print('number of Gradient descent iterations: '+str(len(grad_x)))

#4b
x = np.arange(-3.5,3.5,0.1); y = np.arange(-3.5,6,0.1) 
X,Y = np.meshgrid(x,y)
Z=f(np.array([X,Y]))
plt.contour(X, Y, Z, 1000)

for x0 in [[-3,-3],[3,-3],[-3,3],[3,3],]:
    x=newton_glob(f, grad_f,hess_f, x0=np.array(x0), gamma=0.1, gamma1=1e-6, gamma2=0.1, sigma=0.5, tol=1e-5)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Newton')
    plt.plot(np.array(x)[:,0],np.array(x)[:,1])
plt.show()