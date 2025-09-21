from tasktypes.ballistics1 import Ballistics1
N = int(input("Введите количество траекторий которые хотите задать: "))
all_results = []
graph = Ballistics1()
for i in range(N):
    graph.userinput()
    graph.calculate()
    if graph.calculated_data and 'X_val' in graph.calculated_data:
        all_results.append(graph.calculated_data.copy())

graph.result(all_results)
graph.graph_static(all_results)
