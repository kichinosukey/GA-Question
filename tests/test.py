import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(current_dir, ".."))

import numpy as np

from lib import generate


def test__crossover():

    population_01 = [1, 2, 3]
    population_02 = [3, 2, 1]

    crv_point = 1
    population_01_left = population_01[:crv_point]
    population_01_right = population_01[crv_point:]
    population_02_left = population_02[:crv_point]
    population_02_right = population_02[crv_point:]

    population_01_new = population_01_left + population_02_right
    population_02_new = population_02_left + population_01_right

    assert population_01_new == [1, 2, 1]
    assert population_02_new == [3, 2, 3]

    crv_point = 2
    population_01_left = population_01[:crv_point]
    population_01_right = population_01[crv_point:]
    population_02_left = population_02[:crv_point]
    population_02_right = population_02[crv_point:]

    population_01_new = population_01_left + population_02_right
    population_02_new = population_02_left + population_01_right

    assert population_01_new == [1, 2, 1]
    assert population_02_new == [3, 2, 3]

    population_01 = [1, 2, 3, 4]
    population_02 = [4, 3, 2, 1]

    crv_point = 1
    population_01_left = population_01[:crv_point]
    population_01_right = population_01[crv_point:]
    population_02_left = population_02[:crv_point]
    population_02_right = population_02[crv_point:]

    population_01_new = population_01_left + population_02_right
    population_02_new = population_02_left + population_01_right

    assert population_01_new == [1, 3, 2, 1]
    assert population_02_new == [4, 2, 3, 4]

    crv_point = 2
    population_01_left = population_01[:crv_point]
    population_01_right = population_01[crv_point:]
    population_02_left = population_02[:crv_point]
    population_02_right = population_02[crv_point:]

    population_01_new = population_01_left + population_02_right
    population_02_new = population_02_left + population_01_right

    assert population_01_new == [1, 2, 2, 1]
    assert population_02_new == [4, 3, 3, 4]

    crv_point = 3
    population_01_left = population_01[:crv_point]
    population_01_right = population_01[crv_point:]
    population_02_left = population_02[:crv_point]
    population_02_right = population_02[crv_point:]

    population_01_new = population_01_left + population_02_right
    population_02_new = population_02_left + population_01_right

    assert population_01_new == [1, 2, 3, 1]
    assert population_02_new == [4, 3, 2, 4]

def test__generate():
    
    number_question = 5

    questions = np.random.randint(1, 4, number_question)

    assert len(questions) == number_question

def test__gen_population():

    num_population = 10
    num_question = 5
    range_ans = (0, 1)
    population = [generate(num_question, range_ans) for i in range(num_population)]

    assert len(population) == num_population
    assert len(population[0]) == num_question


def test__evaluate():

    # all matched
    answers_original = [1, 2, 3, 4, 5]
    answers = [1, 2, 3, 4, 5]

    assert len(answers_original) == len(answers)

    result = []
    for a, b in zip(answers_original, answers):
        if a == b:
            match = 1
        else:
            match = 0
        result.append(match)
    
    assert sum(result) == 5

    # partrly matched
    answers_original = [1, 2, 3, 4, 5]
    answers = [5, 4, 3, 2, 1]

    assert len(answers_original) == len(answers)

    result = []
    for a, b in zip(answers_original, answers):
        if a == b:
            match = 1
        else:
            match = 0
        result.append(match)
    
    assert sum(result) == 1

    # nothing matched
    answers_original = [1, 2, 3, 4, 5]
    answers = [5, 4, 5, 2, 1]

    assert len(answers_original) == len(answers)

    result = []
    for a, b in zip(answers_original, answers):
        if a == b:
            match = 1
        else:
            match = 0
        result.append(match)
    
    assert sum(result) == 0

def test__mutation():

    range_min = 2
    range_max = 3
    idx_max = 1
    idx_mut = np.random.randint(0, idx_max)
    l = [1, 2, 3]

    l[idx_mut] = np.random.randint(range_min, range_max)

    assert l == [2, 2, 3]

def test__selection():

    score_dict_sorted = [(0, 2), (1, 1), (2, 1), (3, 0), (4, 0)]

    num_survive = 3

    score_selected = score_dict_sorted[:num_survive]

    assert len(score_selected) == num_survive
    
