import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from mpl_toolkits import mplot3d

iris = datasets.load_iris()

print('Features:'+str(iris.feature_names))
print('Labels'+str(iris.target_names))

X = iris.data
y = iris.target

print(X)
print(y)

plt.figure('Iris dataset', figsize=(7,5))
ax = plt.axes(projection = '3d')
ax.scatter(X[:,3],X[:,0],X[:,2],c=y);
plt.show()
