from tasktypes.ballistics1 import Ballistics1
N = int(input("Введите количество траекторий которые хотите задать: "))
all_results = []

for i in range(N):
    ballisticsnumber1 = Ballistics1()
    ballisticsnumber1.userinput()
    ballisticsnumber1.calculate()
    ballisticsnumber1.result()
    if ballisticsnumber1.calculated_data and 'X_val' in ballisticsnumber1.calculated_data:
        all_results.append(ballisticsnumber1.calculated_data.copy())

graph = Ballistics1()
graph.graph(all_results)
