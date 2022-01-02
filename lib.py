import numpy as np

def crossover(arr_01, arr_02, crv_point):
    """Cross over

    Args:
        arr(list):
        crv_point(int): cross over point

    Returns:
        (tuple)
    
    """
    arr_01_left = arr_01[:crv_point]
    arr_01_right = arr_01[crv_point:]
    arr_02_left = arr_02[:crv_point]
    arr_02_right = arr_02[crv_point:]

    arr_01_new = arr_01_left + arr_02_right
    arr_02_new = arr_02_left + arr_01_right

    return arr_01_new, arr_02_new

def generate(number_question, range_ans):
    """Generate answer array for questions
    
    Args:
        number_question(int):
        range_ans(tuple):
    
    Returns:
        (np.array):
    """
    return np.random.randint(range_ans[0], range_ans[1], number_question)

def gen_population(num_population, num_question, range_ans):
    """Generate population
    
    Args:
        num_population(int): number of population
        num_question(int): number of question
        range_ans(tuple): range of answers, only supported int
    
    Returns:
        (dict):{index: answer_array}
    """
    return {i:list(generate(num_question, range_ans)) for i in range(num_population)}

def evaluate(answer, generated):
    """Evaluate answer array
    
    Args:
        answer(list): answer array
        generated(list): generated array
    """
    result = []
    for a, b in zip(answer, generated):
        if a == b:
            match = 1
        else:
            match = 0
        result.append(match)
    return result

def mutation(arr, range_mut):
    """Mutation

    Args:
        arr(list): array for mutation
        range_mut(tuple/list): range value for mutation
    """
    idx_max_mut = len(arr)
    idx_mut = np.random.randint(0, idx_max_mut)
    arr[idx_mut] = np.random.randint(range_mut[0], range_mut[1])
    return arr

def select(score_list, num_survive):
    """Selection method
    
    Args:
        score_list(list):
        num_survive(int): number of survival candidate
    
    Returns:
        (list)
    """
    return score_list[:num_survive]