#!/usr/bin/env python
# coding: utf-8

# # DDA3020 - Tutorial 1: Numpy & Scikit-Learn

# *Xudong Wang 王旭东*
# 
# *xudongwang@link.cuhk.edu.cn*
# 
# *School of Data Science*
# 
# *The Chinese University of Hongkong, Shenzhen*
# 
# *2022.09.13*

# In[1]:


import warnings; warnings.filterwarnings('ignore')


# # Numpy

# Recommend NumPy version 1.1 or later.
# By convention, you'll find that most people in the SciPy/PyData world will import NumPy using ``np`` as an alias:

# In[2]:


import numpy as np 
print(np.__version__)


# To display all the contents of the numpy namespace, you can type this:
# 
# ```ipython
# In [3]: np.<TAB>
# ```
# 
# And to display NumPy's built-in documentation, you can use this:
# 
# ```ipython
# In [4]: np?
# ```
# 
# More detailed documentation, along with tutorials and other resources, can be found at http://www.numpy.org.

# ## The Basics of NumPy Arrays

# Data manipulation in Python is nearly synonymous with NumPy array manipulation: even packages like Pandas, Scipy, random are built around the NumPy array.
# This section will present several examples of using NumPy array manipulation to access data and subarrays, and to split, reshape, and join the arrays.
# While the types of operations shown here may seem a bit dry and pedantic, they comprise the building blocks of many other examples used throughout the book.
# Get to know them well!
# 
# We'll cover a few categories of basic array manipulations here:
# 
# - *Attributes of arrays*: Determining the size, shape, memory consumption, and data types of arrays
# - *Indexing of arrays*: Getting and setting the value of individual array elements
# - *Slicing of arrays*: Getting and setting smaller subarrays within a larger array
# - *Reshaping of arrays*: Changing the shape of a given array
# - *Joining and splitting of arrays*: Combining multiple arrays into one, and splitting one array into many

# ### NumPy Array Attributes

# First let's discuss some useful array attributes.
# We'll start by defining three random arrays, a one-dimensional, two-dimensional, and three-dimensional array.
# We'll use NumPy's random number generator, which we will *seed* with a set value in order to ensure that the same random arrays are generated each time this code is run:

# In[3]:


import numpy as np
np.random.seed(3020)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array


# Each array has attributes ``ndim`` (the number of dimensions), ``shape`` (the size of each dimension), and ``size`` (the total size of the array):

# In[4]:


print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)


# Another useful attribute is the ``dtype``, the data type of the array (which we discussed previously in [Understanding Data Types in Python](02.01-Understanding-Data-Types.ipynb)):

# In[5]:


print("dtype:", x3.dtype)


# Other attributes include ``itemsize``, which lists the size (in bytes) of each array element, and ``nbytes``, which lists the total size (in bytes) of the array:

# In[6]:


print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")


# In general, we expect that ``nbytes`` is equal to ``itemsize`` times ``size``.

# ### Array Indexing: Accessing Single Elements

# If you are familiar with Python's standard list indexing, indexing in NumPy will feel quite familiar.
# In a one-dimensional array, the $i^{th}$ value (counting from zero) can be accessed by specifying the desired index in square brackets, just as with Python lists:

# In[7]:


x1


# In[8]:


x1[0]


# In[9]:


x1[4]


# To index from the end of the array, you can use negative indices:

# In[10]:


x1[-1]


# In[11]:


x1[-2]


# In a multi-dimensional array, items can be accessed using a comma-separated tuple of indices:

# In[12]:


x2


# In[13]:


x2[0, 0]


# In[14]:


x2[2, 0]


# In[15]:


x2[2, -1]


# Values can also be modified using any of the above index notation:

# In[16]:


x2[0, 0] = 12
x2


# Keep in mind that, unlike Python lists, NumPy arrays have a fixed type.
# This means, for example, that if you attempt to insert a floating-point value to an integer array, the value will be silently truncated. Don't be caught unaware by this behavior!

# In[17]:


x1[0] = 3.14159  # this will be truncated!
x1


# ### Array Slicing: Accessing Subarrays

# Just as we can use square brackets to access individual array elements, we can also use them to access subarrays with the *slice* notation, marked by the colon (``:``) character.
# The NumPy slicing syntax follows that of the standard Python list; to access a slice of an array ``x``, use this:
# ``` python
# x[start:stop:step]
# ```
# If any of these are unspecified, they default to the values ``start=0``, ``stop=``*``size of dimension``*, ``step=1``.
# We'll take a look at accessing sub-arrays in one dimension and in multiple dimensions.

# #### One-dimensional subarrays

# In[18]:


x = np.arange(10)
x


# In[19]:


x[:5]  # first five elements


# In[20]:


x[5:]  # elements after index 5


# In[21]:


x[4:7]  # middle sub-array


# In[22]:


x[::2]  # every other element


# In[23]:


x[1::2]  # every other element, starting at index 1


# A potentially confusing case is when the ``step`` value is negative.
# In this case, the defaults for ``start`` and ``stop`` are swapped.
# This becomes a convenient way to reverse an array:

# In[24]:


x[::-1]  # all elements, reversed


# In[25]:


x[5::-2]  # reversed every other from index 5


# #### Multi-dimensional subarrays
# 
# Multi-dimensional slices work in the same way, with multiple slices separated by commas.
# For example:

# In[26]:


x2


# In[27]:


x2[:2, :3]  # two rows, three columns


# In[28]:


x2[:3, ::2]  # all rows, every other column


# Finally, subarray dimensions can even be reversed together:

# In[29]:


x2[::-1, ::-1]


# ##### Accessing array rows and columns
# 
# One commonly needed routine is accessing of single rows or columns of an array.
# This can be done by combining indexing and slicing, using an empty slice marked by a single colon (``:``):

# In[30]:


print(x2[:, 0])  # first column of x2


# In[31]:


print(x2[0, :])  # first row of x2


# In the case of row access, the empty slice can be omitted for a more compact syntax:

# In[32]:


print(x2[0])  # equivalent to x2[0, :]


# #### Subarrays as no-copy views
# 
# One important–and extremely useful–thing to know about array slices is that they return *views* rather than *copies* of the array data.
# This is one area in which NumPy array slicing differs from Python list slicing: in lists, slices will be copies.
# Consider our two-dimensional array from before:

# In[33]:


print(x2)


# Let's extract a $2 \times 2$ subarray from this:

# In[34]:


x2_sub = x2[:2, :2]
print(x2_sub)


# Now if we modify this subarray, we'll see that the original array is changed! Observe:

# In[35]:


x2_sub[0, 0] = 99
print(x2_sub)


# In[36]:


print(x2)


# This default behavior is actually quite useful: it means that when we work with large datasets, we can access and process pieces of these datasets without the need to copy the underlying data buffer.

# #### Creating copies of arrays
# 
# Despite the nice features of array views, it is sometimes useful to instead explicitly copy the data within an array or a subarray. This can be most easily done with the ``copy()`` method:

# In[37]:


x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)


# If we now modify this subarray, the original array is not touched:

# In[38]:


x2_sub_copy[0, 0] = 42
print(x2_sub_copy)


# In[39]:


print(x2)


# ### Reshaping of Arrays
# 
# Another useful type of operation is reshaping of arrays.
# The most flexible way of doing this is with the ``reshape`` method.
# For example, if you want to put the numbers 1 through 9 in a $3 \times 3$ grid, you can do the following:

# In[40]:


grid = np.arange(1, 10).reshape((3, 3))
print(grid)


# Note that for this to work, the size of the initial array must match the size of the reshaped array. 
# Where possible, the ``reshape`` method will use a no-copy view of the initial array, but with non-contiguous memory buffers this is not always the case.
# 
# Another common reshaping pattern is the conversion of a one-dimensional array into a two-dimensional row or column matrix.
# This can be done with the ``reshape`` method, or more easily done by making use of the ``newaxis`` keyword within a slice operation:

# In[41]:


x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3))


# In[42]:


# row vector via newaxis
x[np.newaxis, :]


# In[43]:


# column vector via reshape
x.reshape((3, 1))


# In[44]:


# column vector via newaxis
x[:, np.newaxis]


# We will see this type of transformation often throughout the remainder of the book.

# ### Array Concatenation and Splitting
# 
# All of the preceding routines worked on single arrays. It's also possible to combine multiple arrays into one, and to conversely split a single array into multiple arrays. We'll take a look at those operations here.

# #### Concatenation of arrays
# 
# Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines ``np.concatenate``, ``np.vstack``, and ``np.hstack``.
# ``np.concatenate`` takes a tuple or list of arrays as its first argument, as we can see here:

# In[45]:


x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])


# You can also concatenate more than two arrays at once:

# In[46]:


z = [99, 99, 99]
print(np.concatenate([x, y, z]))


# It can also be used for two-dimensional arrays:

# In[47]:


grid = np.array([[1, 2, 3],
                 [4, 5, 6]])


# In[48]:


# concatenate along the first axis
np.concatenate([grid, grid])


# In[49]:


# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)


# For working with arrays of mixed dimensions, it can be clearer to use the ``np.vstack`` (vertical stack) and ``np.hstack`` (horizontal stack) functions:

# In[50]:


x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])

# vertically stack the arrays
np.vstack([x, grid])


# In[51]:


# horizontally stack the arrays
y = np.array([[99],
              [99]])
np.hstack([grid, y])


# Similary, ``np.dstack`` will stack arrays along the third axis.

# #### Splitting of arrays
# 
# The opposite of concatenation is splitting, which is implemented by the functions ``np.split``, ``np.hsplit``, and ``np.vsplit``.  For each of these, we can pass a list of indices giving the split points:

# In[52]:


x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)


# Notice that *N* split-points, leads to *N + 1* subarrays.
# The related functions ``np.hsplit`` and ``np.vsplit`` are similar:

# In[53]:


grid = np.arange(16).reshape((4, 4))
grid


# In[54]:


upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)


# In[55]:


left, right = np.hsplit(grid, [2])
print(left)
print(right)


# Similarly, ``np.dsplit`` will split arrays along the third axis.

# # Introducing Scikit-Learn

# There are several Python libraries which provide solid implementations of a range of machine learning algorithms.
# One of the best known is [Scikit-Learn](http://scikit-learn.org), a package that provides efficient versions of a large number of common algorithms.
# Scikit-Learn is characterized by a clean, uniform, and streamlined API, as well as by very useful and complete online documentation.
# A benefit of this uniformity is that once you understand the basic use and syntax of Scikit-Learn for one type of model, switching to a new model or algorithm is very straightforward.
# 
# This section provides an overview of the Scikit-Learn API; a solid understanding of these API elements will form the foundation for understanding the deeper practical discussion of machine learning algorithms and approaches in the following chapters.
# 
# We will start by covering *data representation* in Scikit-Learn, followed by covering the *Estimator* API, and finally go through a more interesting example of using these tools for exploring a set of images of hand-written digits.

# ## Data Representation in Scikit-Learn

# Machine learning is about creating models from data: for that reason, we'll start by discussing how data can be represented in order to be understood by the computer.
# The best way to think about data within Scikit-Learn is in terms of tables of data.

# #### Data as table
# 
# A basic table is a two-dimensional grid of data, in which the rows represent individual elements of the dataset, and the columns represent quantities related to each of these elements.
# For example, consider the [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), famously analyzed by Ronald Fisher in 1936.
# We can download this dataset in the form of a Pandas ``DataFrame`` using the [seaborn](http://seaborn.pydata.org/) library (Based on Matplotlib):

# In[56]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()


# Here each row of the data refers to a single observed flower, and the number of rows is the total number of flowers in the dataset.
# In general, we will refer to the rows of the matrix as *samples*, and the number of rows as ``n_samples``.
# 
# Likewise, each column of the data refers to a particular quantitative piece of information that describes each sample.
# In general, we will refer to the columns of the matrix as *features*, and the number of columns as ``n_features``.

# #### Features matrix
# 
# This table layout makes clear that the information can be thought of as a two-dimensional numerical array or matrix, which we will call the *features matrix*.
# By convention, this features matrix is often stored in a variable named ``X``.
# The features matrix is assumed to be two-dimensional, with shape ``[n_samples, n_features]``, and is most often contained in a NumPy array or a Pandas ``DataFrame``, though some Scikit-Learn models also accept SciPy sparse matrices.
# 
# The samples (i.e., rows) always refer to the individual objects described by the dataset.
# For example, the sample might be a flower, a person, a document, an image, a sound file, a video, an astronomical object, or anything else you can describe with a set of quantitative measurements.
# 
# The features (i.e., columns) always refer to the distinct observations that describe each sample in a quantitative manner.
# Features are generally real-valued, but may be Boolean or discrete-valued in some cases.

# #### Target array
# 
# In addition to the feature matrix ``X``, we also generally work with a *label* or *target* array, which by convention we will usually call ``y``.
# The target array is usually one dimensional, with length ``n_samples``, and is generally contained in a NumPy array or Pandas ``Series``.
# The target array may have continuous numerical values, or discrete classes/labels.
# While some Scikit-Learn estimators do handle multiple target values in the form of a two-dimensional, ``[n_samples, n_targets]`` target array, we will primarily be working with the common case of a one-dimensional target array.
# 
# Often one point of confusion is how the target array differs from the other features columns. The distinguishing feature of the target array is that it is usually the quantity we want to *predict from the data*: in statistical terms, it is the dependent variable.
# For example, in the preceding data we may wish to construct a model that can predict the species of flower based on the other measurements; in this case, the ``species`` column would be considered the target array.
# 
# With this target array in mind, we can use Seaborn(Based on Matplotlib) to conveniently visualize the data:

# In[57]:


# get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', size=1.5);


# For use in Scikit-Learn, we will extract the features matrix and target array from the ``DataFrame``, which we can do using some of the Pandas ``DataFrame`` operations.

# In[58]:


X_iris = iris.drop('species', axis=1)
X_iris.shape


# In[59]:


y_iris = iris['species']
y_iris.shape


# To summarize, the expected layout of features and target values is visualized in the following diagram:

# ![](figures/samples-features.png)
# 

# With this data properly formatted, we can move on to consider the *estimator* API of Scikit-Learn:

# ## Scikit-Learn's Estimator API

# The Scikit-Learn API is designed with the following guiding principles in mind, as outlined in the [Scikit-Learn API paper](http://arxiv.org/abs/1309.0238):
# 
# - *Consistency*: All objects share a common interface drawn from a limited set of methods, with consistent documentation.
# 
# - *Inspection*: All specified parameter values are exposed as public attributes.
# 
# - *Limited object hierarchy*: Only algorithms are represented by Python classes; datasets are represented
#   in standard formats (NumPy arrays, Pandas ``DataFrame``s, SciPy sparse matrices) and parameter
#   names use standard Python strings.
# 
# - *Composition*: Many machine learning tasks can be expressed as sequences of more fundamental algorithms,
#   and Scikit-Learn makes use of this wherever possible.
# 
# - *Sensible defaults*: When models require user-specified parameters, the library defines an appropriate default value.
# 
# In practice, these principles make Scikit-Learn very easy to use, once the basic principles are understood.
# Every machine learning algorithm in Scikit-Learn is implemented via the Estimator API, which provides a consistent interface for a wide range of machine learning applications.

# ### Basics of the API
# 
# Most commonly, the steps in using the Scikit-Learn estimator API are as follows
# (we will step through a handful of detailed examples in the sections that follow).
# 
# 1. Choose a class of model by importing the appropriate estimator class from Scikit-Learn.
# 2. Choose model hyperparameters by instantiating this class with desired values.
# 3. Arrange data into a features matrix and target vector following the discussion above.
# 4. Fit the model to your data by calling the ``fit()`` method of the model instance.
# 5. Apply the Model to new data:
#    - For supervised learning, often we predict labels for unknown data using the ``predict()`` method.
#    - For unsupervised learning, we often transform or infer properties of the data using the ``transform()`` or ``predict()`` method.
# 
# We will now step through two simple examples of applying supervised and unsupervised learning methods.

# ### Supervised learning example: Simple linear regression
# 
# As an example of this process, let's consider a simple linear regression—that is, the common case of fitting a line to $(x, y)$ data.
# We will use the following simple data for our regression example:

# In[60]:


import numpy as np

import matplotlib.pyplot as plt
plt.style.use('seaborn')

rng = np.random.RandomState(3020) # get a random seeds generator
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);


# With this data in place, we can use the recipe outlined earlier. Let's walk through the process: 

# #### 1. Choose a class of model
# 
# In Scikit-Learn, every class of model is represented by a Python class.
# So, for example, if we would like to compute a simple linear regression model, we can import the linear regression class:

# In[61]:


from sklearn.linear_model import LinearRegression


# Note that other more general linear regression models exist as well; you can read more about them in the [``sklearn.linear_model`` module documentation](http://Scikit-Learn.org/stable/modules/linear_model.html).

# #### 2. Choose model hyperparameters
# 
# An important point is that *a class of model is not the same as an instance of a model*.
# 
# Once we have decided on our model class, there are still some options open to us.
# Depending on the model class we are working with, we might need to answer one or more questions like the following:
# 
# - Would we like to fit for the offset (i.e., *y*-intercept)?
# - Would we like the model to be normalized?
# - Would we like to preprocess our features to add model flexibility?
# - What degree of regularization would we like to use in our model?
# - How many model components would we like to use?
# 
# These are examples of the important choices that must be made *once the model class is selected*.
# These choices are often represented as *hyperparameters*, or parameters that must be set before the model is fit to data.
# In Scikit-Learn, hyperparameters are chosen by passing values at model instantiation.
# We will explore how you can quantitatively motivate the choice of hyperparameters in [Hyperparameters and Model Validation](05.03-Hyperparameters-and-Model-Validation.ipynb).
# 
# For our linear regression example, we can instantiate the ``LinearRegression`` class and specify that we would like to fit the intercept using the ``fit_intercept`` hyperparameter:

# In[62]:


model = LinearRegression(fit_intercept=True)
print(model) # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
# get_ipython().run_line_magic('pinfo', 'model')


# Keep in mind that when the model is instantiated, the only action is the storing of these hyperparameter values.
# In particular, we have not yet applied the model to any data: the Scikit-Learn API makes very clear the distinction between *choice of model* and *application of model to data*.

# #### 3. Arrange data into a features matrix and target vector
# 
# Previously we detailed the Scikit-Learn data representation, which requires a two-dimensional features matrix and a one-dimensional target array.
# Here our target variable ``y`` is already in the correct form (a length-``n_samples`` array), but we need to massage the data ``x`` to make it a matrix of size ``[n_samples, n_features]``.
# In this case, this amounts to a simple reshaping of the one-dimensional array:

# In[63]:


X = x[:, np.newaxis] # Recap the numpy usage. We can also use X = x.reshape(-1,1)
X.shape


# #### 4. Fit the model to your data
# 
# Now it is time to apply our model to data.
# This can be done with the ``fit()`` method of the model:

# In[64]:


model.fit(X, y) # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)


# This ``fit()`` command causes a number of model-dependent internal computations to take place, and the results of these computations are stored in model-specific attributes that the user can explore.
# In Scikit-Learn, by convention all model parameters that were learned during the ``fit()`` process have trailing underscores; for example in this linear model, we have the following:

# In[65]:


model.coef_


# In[66]:


model.intercept_


# These two parameters represent the slope and intercept of the simple linear fit to the data.
# Comparing to the data definition, we see that they are close to the input slope of 2 and intercept of -1.
# 
# One question that frequently comes up regards the uncertainty in such internal model parameters.
# In general, Scikit-Learn does not provide tools to draw conclusions from internal model parameters themselves: interpreting model parameters is much more a *statistical modeling* question than a *machine learning* question.
# Machine learning rather focuses on what the model *predicts*.
# If you would like to dive into the meaning of fit parameters within the model, other tools are available, including the [Statsmodels Python package](http://statsmodels.sourceforge.net/).

# #### 5. Predict labels for unknown data
# 
# Once the model is trained, the main task of supervised machine learning is to evaluate it based on what it says about new data that was not part of the training set.
# In Scikit-Learn, this can be done using the ``predict()`` method.
# For the sake of this example, our "new data" will be a grid of *x* values, and we will ask what *y* values the model predicts:

# In[67]:


xfit = np.linspace(-1, 11)  # default num = 50


# As before, we need to coerce these *x* values into a ``[n_samples, n_features]`` features matrix, after which we can feed it to the model:

# In[68]:


Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)


# Finally, let's visualize the results by plotting first the raw data, and then this model fit:

# In[69]:


plt.figure() 
plt.scatter(x, y,label = 'Training Data')
plt.scatter(xfit, yfit, c = 'red',marker='*',label = 'Predicted Data');
plt.plot(xfit, yfit, c = 'red', label = 'Fitted Line');
plt.title(r"Linear Regression: $y = 2 * x - 1 + \epsilon$");
plt.legend(loc = 'best')
plt.show() 


# ### Supervised learning example: Iris classification
# 
# Let's take a look at another example of this process, using the Iris dataset we discussed earlier.
# Our question will be this: given a model trained on a portion of the Iris data, how well can we predict the remaining labels?
# 
# For this task, we will use an extremely simple generative model known as Gaussian naive Bayes, which proceeds by assuming each class is drawn from an axis-aligned Gaussian distribution for more details).
# Because it is so fast and has no hyperparameters to choose, Gaussian naive Bayes is often a good model to use as a baseline classification, before exploring whether improvements can be found through more sophisticated models.
# 
# We would like to evaluate the model on data it has not seen before, and so we will split the data into a *training set* and a *testing set*.
# This could be done by hand, but it is more convenient to use the ``train_test_split`` utility function:

# In[70]:


# Load the iris datasets from sklearn
from sklearn.datasets import load_iris
X_iris, y_iris = load_iris()['data'], load_iris()['target']


# In[71]:


from sklearn.model_selection import train_test_split
# from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris,
                                                random_state=3020)


# With the data arranged, we can follow our recipe to predict the labels:

# In[72]:


from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(Xtrain, ytrain)                  # 3. fit model to data
y_model = model.predict(Xtest)             # 4. predict on new data


# Finally, we can use the ``accuracy_score`` utility to see the fraction of predicted labels that match their true value:

# In[73]:


from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)


# With an accuracy topping 97%, we see that even this very naive classification algorithm is effective for this particular dataset!

# ### Unsupervised learning example: Iris dimensionality
# 
# As an example of an unsupervised learning problem, let's take a look at reducing the dimensionality of the Iris data so as to more easily visualize it.
# Recall that the Iris data is four dimensional: there are four features recorded for each sample.
# 
# The task of dimensionality reduction is to ask whether there is a suitable lower-dimensional representation that retains the essential features of the data.
# Often dimensionality reduction is used as an aid to visualizing data: after all, it is much easier to plot data in two dimensions than in four dimensions or higher!
# 
# Here we will use principal component analysis (PCA, we will learn it at future DDA3020 lectures, Here just a use demo for Unsupervised learning), which is a fast linear dimensionality reduction technique.
# We will ask the model to return two components—that is, a two-dimensional representation of the data.
# 
# Following the sequence of steps outlined earlier, we have:

# In[74]:


from sklearn.decomposition import PCA  # 1. Choose the model class
model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified! Cuz is Unsupervised learning.
X_2D = model.transform(X_iris)         # 4. Transform the data to two dimensions


# Now let's plot the results. A quick way to do this is to insert the results into the original Iris ``DataFrame``, and use Seaborn's ``lmplot`` to show the results:

# In[75]:


plt.figure()
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);
plt.show() 

# We see that in the two-dimensional representation, the species are fairly well separated, even though the PCA algorithm had no knowledge of the species labels!
# This indicates to us that a relatively straightforward classification will probably be effective on the dataset, as we saw before. For PCA method, we will learn it at the end of this semester's DDA3020 course.

# # Summary

# In this tutorial we have covered the essential features of Numpy ndarray, the Scikit-Learn data representation, and the estimator API.
# Regardless of the type of estimator, the same import/instantiate/fit/predict pattern holds.
# Armed with this information about the estimator API, you can explore the Scikit-Learn documentation and begin trying out various machine learning models on your data.

# <center>End of this tutorial's coding part.
# 
# <center>Wang Xudong 王旭东
# <center>xudongwang@link.cuhk.edu.cn
# <center>SDS, CUHK(SZ)
#  <center>2022.09.13<center>
