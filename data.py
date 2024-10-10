#data.py
import numpy

def load_dict(filename):
    """load a dictionary from file"""
    with open(filename,'r') as f:
        lines = f.readlines()
    lines = [ line.strip().split('\t') for line in lines ]
    #return dict(lines)
    lines = [ line[-1] for line in lines ]
    return lines

def load_matrix(filename):
    """load a data matrix from file"""
    with open(filename,'r') as f:
        lines = f.readlines()
    lines = [ line.strip().split(' ') for line in lines ]
    lines = [ list(map(int,line)) for line in lines ]
    return lines

def load_dataset():
    """load the animals dataset from file"""
    data_filename = r"D:\Users\J.I Traders\Desktop\Projects\New folder\hw2 (1)\hw2\awa\predicate-matrix-binary.txt"
    label_filename = r"D:\Users\J.I Traders\Desktop\Projects\New folder\hw2 (1)\hw2\awa\classes.txt"
    feature_filename = r"D:\Users\J.I Traders\Desktop\Projects\New folder\hw2 (1)\hw2\awa\predicates.txt"

    labels = load_dict(label_filename)
    features = load_dict(feature_filename)
    data = load_matrix(data_filename)

    # convert to numpy arrays
    labels = numpy.array(labels)
    features = numpy.array(features)
    data = numpy.array(data)

    return labels,features,data

