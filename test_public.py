#test_public.py
import numpy as np
from data import load_dataset
from player import DataPlayer
from animals import lookup_animal, play_game
from decision import entropy, pick_feature

# load the dataset
animals_data = load_dataset()
labels,features,data = animals_data

def test_01():
    assert entropy(2) == 1
    assert entropy(4) == 2
    assert entropy(8) == 3
    assert entropy(16) == 4

def test_02():
    err = 0.0001
    ent3 = 1.584962500721156
    ent10 = 3.321928094887362
    ent100 = 6.643856189774724
    ent1000 = 9.965784284662087

    assert ent3 - err <= entropy(3) <= ent3 + err
    assert ent10 - err <= entropy(10) <= ent10 + err
    assert ent100 - err <= entropy(100) <= ent100 + err
    assert ent1000 - err <= entropy(1000) <= ent1000 + err

def test_03():
    animal = "dalmatian"
    animal_map = lookup_animal(animal,animals_data)
    player = DataPlayer(animal,animal_map)
    success,questions_asked = play_game(animals_data,player)
    assert questions_asked <= 6

def test_04():
    animal = "deer"
    animal_map = lookup_animal(animal,animals_data)
    player = DataPlayer(animal,animal_map)
    success,questions_asked = play_game(animals_data,player)
    assert questions_asked <= 6

def test_05():
    animal = "pig"
    animal_map = lookup_animal(animal,animals_data)
    player = DataPlayer(animal,animal_map)
    success,questions_asked = play_game(animals_data,player)
    assert questions_asked <= 6
