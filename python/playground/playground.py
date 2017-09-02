samples = [[1., 1., 1.1], [1., 1.1, 1.], [1., 1., .5]]
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import LocalOutlierFactor
neigh = NearestNeighbors(n_neighbors=1)
localn = LocalOutlierFactor(
        n_neighbors=35,
        contamination=outliers_fraction)
print(neigh.fit(samples))
print(neigh.negative_outlier_factor_)
#print(neigh.kneighbors([[1., 1., 1.]], 2)[1])