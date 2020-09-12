import numpy as np

def datasetSave(X, totalFeature, fileName):
    np.save(arr=X, file='./Extracted-Features/{}-{}'.format(fileName, totalFeature))
    print('{}-{}.npy generated (Directory/Folder: Extracted-Features); and shape: (Sample, T, Feature) --> {}'.format(fileName, totalFeature, X.shape))
#end-def