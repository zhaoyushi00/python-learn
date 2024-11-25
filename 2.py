from deap import base, creator, tools, algorithms

# 遗传算法参数
POP_SIZE = 300
MAX_GEN = 40
MUT_PB = 0.2
CX_PB = 0.5

# 创建适应度函数和个体
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# 定义个体生成函数
def generate_individual():
    return [np.random.uniform(0, 1), np.random.uniform(0, 1)]

toolbox.register("individual", tools.initIterate, creator.Individual, generate_individual)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 定义评价函数
def evaluate(individual):
    airstrip_position = np.array(individual)
    coverage = np.sum(
        np.linalg.norm(demand_points[:, :2] - airstrip_position, axis=1) <= airstrip_types['type1']['range']
    )
    return -coverage,

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=POP_SIZE)
    hof = tools.HallOfFame(1)

    algorithms.eaSimple(pop, toolbox, cxpb=CX_PB, mutpb=MUT_PB, ngen=MAX_GEN, halloffame=hof, verbose=True)

    return hof[0]

best_airstrip_position = main()
print(best_airstrip_position)
