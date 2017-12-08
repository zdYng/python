from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('Agg')
plt.switch_backend('agg')
X,y = make_classification(
    n_samples=300,n_features=2,
     n_redundant=0,n_informative=2,
     random_state=22,n_clusters_per_class=1,
     scale=100)
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()