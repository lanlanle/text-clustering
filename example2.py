from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2).fit_transform(X)
y_pred = KMeans(n_clusters=3, random_state=0).fit_predict(pca)

plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()


