from sklearn.ensemble import RandomForestClassifier
import numpy as np

#Import the dataset

#X = dataset
#Y = labels. First 9600 are powerlaw; second 9600 are exponential; third are neighbourhood
Y = np.repeat(np.array([0, 1, 2]), 9600)
clf = RandomForestClassifier(n_estimators=1000)
clf = clf.fit(X, Y) 
