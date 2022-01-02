import numpy as np

from lib import crossover, evaluate, gen_population, select, mutation

if __name__ == '__main__':

    answer = [1, 2, 3]
    num_question = len(answer)
    num_survive = 3
    num_population = 5

    population = gen_population(num_population, num_question, (min(answer), max(answer)))
    score_dict = {idx:sum(evaluate(answer, result)) for idx, result in population.items()}
    score_list_sorted = sorted(score_dict.items(), reverse=True, key=lambda x: x[1])
    
    print(score_list_sorted[0])
    cnt = 0
    while score_list_sorted[0][1] != 3:
        

        score_list_selected = select(score_list_sorted, num_survive)
        idx_selected = [t[0] for t in score_list_selected]
        population_selected = [population[idx] for idx in idx_selected]

        pop01 = population[score_list_sorted[0][0]]
        pop02 = population[score_list_sorted[1][0]]
        crv_point = np.random.randint(1, num_question-1)
        new01, new02 = crossover(pop01, pop02, crv_point)
        new01 = mutation(new01, (1, 4))
        new02 = mutation(new02, (1, 4))

        population_selected.append(new01)
        population_selected.append(new02)

        population = population_selected[:]
        population = {i:pop for i, pop in enumerate(population)}
        score_dict = {idx:sum(evaluate(answer, result)) for idx, result in population.items()}
        score_list_sorted = sorted(score_dict.items(), reverse=True, key=lambda x: x[1])       

        print(score_list_sorted[0])

        cnt += 1

        if cnt > 100:
            print(population)
            break