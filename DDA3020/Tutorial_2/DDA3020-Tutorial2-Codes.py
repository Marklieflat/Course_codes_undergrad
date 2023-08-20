#!/usr/bin/env python
# coding: utf-8

# # DDA3020 - Tutorial 2: Linear Algebra \& Linear Regression

# *Xudong Wang 王旭东*
# 
# *xudongwang@link.cuhk.edu.cn*
# 
# *School of Data Science*
# 
# *The Chinese University of Hongkong, Shenzhen*
# 
# *2022.09.20*

# In[1]:


import warnings; warnings.filterwarnings('ignore')


# # Linear Algebra in Python

# ## Basic Matrix Vector Operations
# please pay attention to assigning shape and an appropriate representation based on your application for numpy Ndarray.

# In[2]:


import numpy as np
import math 
import scipy 
np.random.seed(3020)


# ## Numpy Linear Algebra Algorithms

# In[3]:


print([method for method in dir(np.linalg) if '__' not in method])


# In[4]:


print(np.linalg.norm([1,2,3,4]),np.linalg.norm([1,2,3,4],1))
print(np.linalg.matrix_rank([1,2,3,4]))
print(np.linalg.det(np.ones((2,2))),np.diag([1,2,3,4]),np.linalg.det(np.diag([1,2,3,4])))  


# In[5]:


np.linalg.eigvals(np.diag([1,2,3,4])) 


# In[6]:


np.linalg.eig(np.diag([1,2,3,4]))  


# In[7]:


# check the document.
# help(np.linalg.norm)


# ## Dot product

# In[8]:


a = np.array([1,2]).reshape(2,1)
b = np.array([3,4])
b.shape = (2,1) # This is inplace handle, directly change the shape attribute of b
print(a.shape,b.shape)


# Generic matrix/vector multiplication 

# In[9]:


print(np.vdot(a,b)) 
# print(a.dot(b)) # ValueError: shapes (2,1) and (2,1) not aligned: 1 (dim 1) != 2 (dim 0)
print(np.array([1,2]).shape) # default in 1-d, regard as vector.
print(np.array([1,2]).dot(np.array([3,4])))


# In[10]:


np.vdot(a,b).shape # Scalar


# ## Inner Product
# Note: Numpy automatically transposes the second argument, so we need to account for this implementation. This implies we define a and b as row vectors, so inner product is $A.B^T$

# In[11]:


a = a.reshape(1,2)
b = b.reshape(1,2)


# In[12]:


print(np.inner(b,a), np.inner(b,a).shape) 


# In[13]:


print(np.dot(a, np.transpose(b)),np.dot(a, np.transpose(b)).shape)
print(np.dot(a, b.T),np.dot(a, b.T).shape)
print(a.dot(b.T),a.dot(b.T).shape)


# ## Outer product
# Similar note of caution as with inner product. Outer product is $A^T.B$

# In[14]:


print(a,b)
print(np.outer(a,b), np.outer(a,b).shape) 


# In[15]:


print(np.dot(np.transpose(a), b),np.dot(np.transpose(a), b).shape)
print(np.dot(a.T, b),np.dot(a.T, b).shape)
print(a.T.dot(b),a.T.dot(b).shape)


# ## Kronecker Product - Generalization of Outer Product to Matrices
# 
# dim(A$\otimes$B) = dim(A) $\times$ dim(B)
# in the example below, A and B are each (2,2) so kron(A,B) is (4,4)

# ##Kronecker Product - Generalization of Outer Product to Matrices
# dim(A$\otimes$B) = dim(A) $\times$ dim(B)
# in the example below, A and B are each (2,2) so kron(A,B) is (4,4)

# In[16]:


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a.shape,b.shape)
print(a,'\n',b)


# In[17]:


np.kron(a,b)


# In[18]:


print(np.matmul(a, np.transpose(b)))
print(a.dot(b.T)) 
print(a.dot(b)) 


# ## Applying Functions on Arrays
# Numpy provides many functions to apply aggregate functions over arrays
# 

# In[19]:


import numpy as np
from numpy import random


# In[20]:


# ndarray support math calculate from math package.
import math
from math import sqrt
a = np.random.normal(10, 2, 100) # pick 100 values from a normal dist with mean 2 and sd of 2
print(np.sum(a)) # add them up
print(math.fsum(a))


# In[21]:


np.mean(a) # find thier mean hopefully close to 10


# In[22]:


print(sqrt(a.var())) ## similarly can find variance or std deviation
print(a.std()) 


# For multi-dimensional arrays we will have to specify the axis argument to let numpy know we are interested in running the calculation along a particular axis only

# In[23]:


a = a.reshape((10,10)) # reshape a into a 10 x 10 matrix


# Now perform any of the above operations by specifying an axis

# In[24]:


np.mean(a, axis = 0) # row wise means


# In[25]:


print([np.mean(a[:,i]) for i in range(a.shape[1])]) 


# In[26]:


np.var(a, axis = 0) # row wise variances


# In[27]:


np.sum(a, axis = 0)


# ## Comparing Arrays
# Operations on arrays are performed element by element. This can be used to perform logical selections

# In[28]:


a = np.array([1,2,3])
b = np.array([4,5,6])
a > b 


# In[29]:


c = np.concatenate((a,b)) # Ref tut1, you can have many way to concatenate, like use stack.
print ("c is a and b concatenated : " + str(c))
select = c > 2
cp = c[select]
print("Values in c that are greater than 2: " + str(cp))


# ## Applying Functions on Arrays
# Functions are applied element by element

# In[30]:


a = np.array([2,4,8, 16])
np.log2(a) # apply the log function along a


# ## Arithmetic Operations Using Arrays
# Element-Wise
# 
# 
# Again, these are performed element by element - please note that this not matrix type operation.

# In[31]:


a = np.array([[1,2],[3,4]], float)
b = np.array([[5,6],[7,8]], float)


# In[32]:


a + b


# In[33]:


a*b


# In[34]:


a/b # watch out for divide by zero - need to use special techniques if arrays contain very small numbers


# ## Numpy Broadcasting
# Broadcasting is an important concept in numpy to handle situations where we perform arithmetic opertions where the operands are not of the same size. For example adding a scalar to a matrix. In this case, numpy converts the smaller operand to the size of the bigger operand behind the scenes so that this addition is possible. This is a crucial concept to keep in mind. The rules are quite elaborate and can be found here: https://numpy.org/doc/stable/user/basics.broadcasting.html

# **General Broadcasting Rules**

# <p>When operating on two arrays, NumPy compares their shapes element-wise.
# It starts with the trailing (i.e. rightmost) dimensions and works its
# way left.  Two dimensions are compatible when</p>

# <ol class="arabic simple">
# <li><p>they are equal, or</p></li>
# <li><p>one of them is 1</p></li>
# </ol>

# <p>If these conditions are not met, a
# <code class="docutils literal notranslate"><span class="pre">ValueError:</span> <span class="pre">operands</span> <span class="pre">could</span> <span class="pre">not</span> <span class="pre">be</span> <span class="pre">broadcast</span> <span class="pre">together</span></code> exception is
# thrown, indicating that the arrays have incompatible shapes. The size of
# the resulting array is the size that is not 1 along each axis of the inputs.</p>

# ![A scalar is broadcast to match the shape of the 1-d array it is being multiplied to.](./broadcasting_1.png)
# 
# > _Figure 1_#
# 
# > _In the simplest example of broadcasting, the scalar_ `b` _is stretched to become an array of same shape as_ `a` _so the shapes are compatible for element-by-element multiplication._

# In[35]:


a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b


# ![A 1-d array with shape (3) is stretched to match the 2-d array of shape (4, 3) it is being added to, and the result is a 2-d array of shape (4, 3).](./broadcasting_2.png)
# 
# > _Figure 2_#
# 
# > _A one dimensional array added to a two dimensional array results in broadcasting if number of 1-d array elements matches the number of 2-d array columns._

# ![A huge cross over the 2-d array of shape (4, 3) and the 1-d array of shape (4) shows that they can not be broadcast due to mismatch of shapes and thus produce no result.](./broadcasting_3.png)
# 
# > _Figure 3_#
# 
# > _When the trailing dimensions of the arrays are unequal, broadcasting fails because it is impossible to align the values in the rows of the 1st array with the elements of the 2nd arrays for element-by-element addition._

# In[36]:


a = np.array([[ 0.0,  0.0,  0.0],
              [10.0, 10.0, 10.0],
              [20.0, 20.0, 20.0],
              [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])
print(a + b)
b = np.array([1.0, 2.0, 3.0, 4.0])
# a + b
# Traceback (most recent call last):
# ValueError: operands could not be broadcast together with shapes (4,3) (4,)


# In[37]:


A = np.arange(1, 10, 1)
A = A.reshape((3,3)) # create a 3 x 3 matrix
A


# In[38]:


A = A + 5
A


# In[39]:


b = np.array([1,2,3])
b = b.reshape((3,1))
b


# In[40]:


C = A + b
C


# # Least Square & Linear Regression and its Optimization



# In[41]:


import matplotlib.pyplot as plt
plt.style.use('seaborn')

rng = np.random.RandomState(3020) # get a random seeds generator
x = 10 * rng.rand(50)
X = x[:, np.newaxis] # Recap the numpy usage. We can also use X = x.reshape(-1,1)
y = 2 * x - 1 + rng.randn(50)
y.shape = (-1,1)
plt.scatter(x, y);

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
print(model) # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

model.fit(X, y) # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(model.coef_,model.intercept_)


# ## Optimization For Least Square Problem (Scipy, Close form Sol)

# ### Toy demo for one varible optimization

# In[42]:


x1 = np.asmatrix(np.linspace(0, 1, 20))
w = 10
y = w*x1


# In[43]:


def loss(wp):
    res = y - wp*x1
    return np.sum(np.power(res, 2))


# In[44]:


from scipy import optimize
p0 = 0
opt_cg = optimize.minimize(loss, p0, method='CG')
print(opt_cg) 

fprime = lambda x: optimize.approx_fprime(x, loss, 0.0001)
opt_NtCG = optimize.minimize(loss, p0,  method='Newton-CG',jac = fprime)
print(opt_NtCG)


# Ref Scipy official document for more methods. 



# ### Back to Linear Regression example with intercept

# In[45]:


rng = np.random.RandomState(3020) # get a random seeds generator
x = 10 * rng.rand(50)
X = x[:, np.newaxis] # Recap the numpy usage. We can also use X = x.reshape(-1,1)
y = 2 * x - 1 + rng.randn(50)
y.shape = (-1,1)

def loss(p):
    w = p[0]
    b = p[1]
    res = y - w*X - b
    return np.sum(np.power(res, 2))

w_0,b_0 = 0.0,0.0
opt_cg = optimize.minimize(loss,[w_0,b_0], method='CG')
print(opt_cg) 


# In[46]:


# compare sklearn 
print(model.coef_,model.intercept_)


# ### Close form Solution


# In[47]:


X_ = np.hstack((np.ones((X.shape[0],1)),X))
print(X_.shape, y.shape)


# In[48]:


# Close Form Sol
b_close, w_close = np.linalg.inv(X_.T.dot(X_)).dot(X_.T).dot(y)
print( w_close, b_close)


# ### Multivariate Optimization with Scipy

# In[49]:


from sklearn.preprocessing import normalize
x1 = np.asmatrix(np.linspace(0, 100, 20))
#x1 = np.asmatrix(2*np.linspace(50, 100, 20))
x2 = np.asmatrix(np.linspace(50, 100, 20))
x1 = normalize(x1)
x2 = normalize(x2)
X = np.concatenate([x1.T,x2.T], axis = 1) # also can use Vstack
w = np.asmatrix([[10], [20]])
noise = np.random.normal(0, 0.25, 20)
noise = np.asmatrix(noise)
Y = np.matmul(X,w) + noise.T
print(X.shape, Y.shape)


# In[50]:


def loss(wp):
    wp = np.asmatrix([[wp[0]], [wp[1]]])
    Yhat = np.matmul(X,wp)
    res = Y - Yhat
    se = np.power(res, 2)
    sse = np.sum(se)
    return sse


# In[51]:


from scipy import optimize
p0 = [0,0]
optimize.minimize(loss, p0, method='BFGS')


# **Here, the original data is no intercept, how about we fitting a intercept?**

# In[52]:


X_multi = np.hstack((np.ones((X.shape[0],1)),X))
print(X_multi.shape, Y.shape)


# In[53]:


np.linalg.matrix_rank(X.T.dot(X))


# In[54]:


np.linalg.matrix_rank(X_multi.T.dot(X_multi))


# In[55]:


np.linalg.det(X.T.dot(X))


# In[56]:


np.linalg.det(X_multi.T.dot(X_multi))


# In[57]:


# with intercept, actually here is non-singular matrix for X_multi
# print(np.linalg.inv(X_multi.T.dot(X_multi)).dot(X_multi.T).dot(Y))
print(np.linalg.pinv(X_multi.T.dot(X_multi)).dot(X_multi.T).dot(Y))
# Moore-Penrose（Moore-Penrose pseudoinverse） 
# This need knowledge of SVD, you will learn in later lecture.


# In[58]:


# Same as Scipy optimize
print(np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(Y))


# # Summary

#  - Numpy Linear Algebra
#  
#  - Least Square Problem: Linear Regression
#  
#  - Optimization with Scipy
#  
#  
#  
#  
#  - Other useful tips/hits I wanna share for u: 
#        
#       
# If you interest, Autograd is also powerful tool for calculate gradient, do optimize, actually is the basis for Pytorch Basis. autograd is PyTorch's automatic differentiation engine that powers neural network training.
#         
# Autograd interface: *import autograd.numpy as np*
#  
# if you have GPU(With CUDA support, Nvida Cards, or ROCM AMD cards in linux, you can use CUDA numpy) *import cupy as cp* can be regrad as numpy in GPU model.
# 

# <center>End of this tutorial's coding part.
# 
# <center>Wang Xudong 王旭东
# <center>xudongwang@link.cuhk.edu.cn
# <center>SDS, CUHK(SZ)
#  <center>2022.09.20<center>
