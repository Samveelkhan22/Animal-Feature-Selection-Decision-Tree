# #decision.py
# import numpy

# def entropy(count):
#     """count it an integer that is greater than or equal to 1

#     returns the entropy of a uniform distribution over count animals
#     """
#     return None

# def pick_feature(data,features):
#     """given a dataset of animals vs features, and a list of feature
#     names, returns a tuple (best_index,best_feature) where best_index
#     is the index of the most informative feature, and best_feature is
#     the name of the feature

#     data is an m-x-n matrix where m is the number of animals and n is
#     the number of features.  data[i][j] iff animal i answers yes to
#     question j.

#     features is a list of strings of length n.  The columns of the
#     data matrix correspond to the name of the features in this list.

#     """

#     best_index = 0
#     best_feature = features[best_index]
#     return best_index,best_feature

import numpy as np
import math

def entropy(count):
    """ 
    Calculate the entropy of a uniform distribution over 'count' animals.

    Args:
        count (int): Number of animals.

    Returns:
        float: Entropy of the uniform distribution.
    """
    if count == 0:
        return 0
    # The entropy of a uniform distribution is log2(count)
    return math.log2(count)

def pick_feature(data, features):
    """ 
    Given a dataset of animals vs features and a list of feature names, 
    returns the index and name of the most informative feature.

    Args:
        data (numpy array): An m-x-n matrix where m is the number of animals 
                            and n is the number of features. 
                            data[i][j] is True if animal i answers 'yes' to question j.
        features (list): A list of feature names.

    Returns:
        tuple: (best_index, best_feature) where best_index is the index of the most 
               informative feature, and best_feature is the name of that feature.
    """
    best_index = None
    best_entropy = float('inf')  # Start with the highest possible entropy
    m, n = data.shape  # m = number of animals, n = number of features

    for feature_index in range(n):
        # Split animals into two groups: "yes" (answers yes to this feature) and "no" (answers no)
        yes_group = data[:, feature_index] == 1
        no_group = data[:, feature_index] == 0
        
        # Count the number of animals in each group
        yes_count = np.sum(yes_group)
        no_count = np.sum(no_group)

        # Calculate the probabilities of each group
        prob_yes = yes_count / m
        prob_no = no_count / m

        # Calculate the entropy of each group
        entropy_yes = entropy(yes_count) if yes_count > 0 else 0
        entropy_no = entropy(no_count) if no_count > 0 else 0

        # Calculate the expected entropy after splitting by this feature
        expected_entropy = (prob_yes * entropy_yes) + (prob_no * entropy_no)

        # Select the feature that results in the lowest expected entropy
        if expected_entropy < best_entropy:
            best_entropy = expected_entropy
            best_index = feature_index

    # Return the best feature's index and its name
    best_feature = features[best_index]
    return best_index, best_feature
