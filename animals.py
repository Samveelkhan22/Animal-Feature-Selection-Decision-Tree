#animals.py
import numpy
from data import load_dataset
from player import *
from decision import pick_feature

def ask_animal_question(animal):
    print("Questioner: Is your animal a %s?" % animal)

def ask_feature_question(feature,question_number):
    print("Questioner (%d): Is your animal a %s animal?" % \
          (question_number,feature))

def lookup_animal(animal,animal_data):
    animal_index = (numpy.argwhere(labels == animal))[0][0] # index of animal
    animal_vals = data[animal_index,:]                      # row for animal
    animal_map = dict(zip(features,animal_vals))            # feature/value map
    return animal_map

def reduce_data(labels,features,data,best_index,answer):
    # get selection of animals corresponding to answer
    column = data[:,best_index] == answer

    # select the resulting animals (rows), and discard the rest
    data = data[column]
    labels = labels[column]

    # remove the feature (column)
    data = numpy.delete(data,best_index,axis=1)
    features = numpy.delete(features,best_index)

    return labels,features,data

def play_game(animals_data,player):
    labels,features,data = animals_data
    questions_asked = 0

    while len(data) > 1:
        """while there is not a unique animal"""

        # pick best question to ask
        best_index,best_feature = pick_feature(data,features)

        # ask question and get answer from player
        questions_asked += 1
        ask_feature_question(best_feature,questions_asked)
        answer = player.answer_feature_question(best_feature)

        # split the dataset by the answer, and remove the feature
        labels,features,data = reduce_data(labels,features,data,
                                           best_index,answer)

    if len(data) == 0:
        """we eliminated all possibilities"""
        print("Questinoer: unknown animal!")
        return False,questions_asked
    else:
        animal = labels[0] # pick the only animal left
        ask_animal_question(animal)
        answer = player.answer_animal_question(animal)
        if answer:
            print("Questioner: success! (%d questions asked)" % questions_asked)
            return True,questions_asked
        else:
            print("Questioner: failure! (%d questions asked)" % questions_asked)
            return False,questions_asked

# load the dataset
animals_data = load_dataset()
labels,features,data = animals_data

N = len(labels)   # number of animals
M = len(features) # number of features

print("== dataset statistics:")
print("  %d animals" % len(labels))
print("  %d features" % len(features))

# count how times each feature appears in an animal (sum all rows)
counts = data.sum(axis=0)
max_count,min_count = counts.max(),counts.min()
print(" - most common features, appears in %d animal(s):" % max_count)
print("   %s" % ",".join(features[counts==max_count]))
print(" - least common features, appears in %d animal(s):" % min_count)
print("   %s" % ",".join(features[counts==min_count]))
print()

# print a list of all the animals
print("== animals (%d animals):" % len(labels))
print(" ".join(labels))
print()

#player = InputPlayer()
success_count = 0
max_questions = 0
total_questions = 0
#test_animals = labels
test_animals = ["grizzly_bear"]
for animal in test_animals:
    print("================")
    print("Answerer: I picked the animal %s" % animal)

    animal_map = lookup_animal(animal,animals_data)
    player = DataPlayer(animal,animal_map)
    success,questions_asked = play_game(animals_data,player)

    success_count += success
    total_questions += questions_asked
    max_questions = max(max_questions,questions_asked)

print()
print("success rate: (%d/%d)" % (success_count,len(test_animals)))
print("avg. # of questions asked: %.4f" % (total_questions/len(test_animals),))
print("most # of questions asked: %.4f" % max_questions)
