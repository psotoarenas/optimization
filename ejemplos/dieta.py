__author__ = "Paola Soto"

#!/usr/bin/env python3.7

"""
En un centro de nutrición se desea obtener la dieta de coste mínimo con unos determinados requisitos vitamínicos para 
un grupo de niños que van a asistir a campamentos de verano. El especialista estima que la dieta debe contener entre 
26 y 32 unidades de vitamina A, al menos 25 unidades de vitamina B y 30 de C, y a lo sumo 14 de vitamina D. La 
siguiente tabla nos da el numero de unidades de las distintas vitaminas por unidad de alimento consumido para seis 
alimentos elegidos, denominados 1, 2, 3, 4, 5 y 6, así como su coste por unidad

+-----------+---------------+------------+
| Alimentos | Vitaminas     | Costo por  |
|           +---+---+---+---+ Unidad     |
|           | A | B | C | D |            |
+-----------+---+---+---+---+------------+
| 1         | 1 | 1 | 0 | 1 | 10         |
+-----------+---+---+---+---+------------+
| 2         | 1 | 2 | 1 | 0 | 14         |
+-----------+---+---+---+---+------------+
| 3         | 0 | 1 | 2 | 0 | 12         |
+-----------+---+---+---+---+------------+
| 4         | 3 | 1 | 0 | 1 | 18         |
+-----------+---+---+---+---+------------+
| 5         | 2 | 1 | 2 | 0 | 20         |
+-----------+---+---+---+---+------------+
| 6         | 1 | 0 | 2 | 1 | 16         |
+-----------+---+---+---+---+------------+

Se desea conocer la cantidad de cada alimento que hay que preparar y que satisfaga los requisitos propuestos con el 
mínimo costo. 
"""

import gurobipy as gp
from gurobipy import GRB

try:
    # Crea un nuevo modelo
    m = gp.Model("dieta")

    # Crea las variables, estas variables son continuas y no negativas
    X = []
    for i in range(1, 7):
        X.append(m.addVar(0.0, GRB.INFINITY, vtype=GRB.CONTINUOUS, name="x_{}".format(i)))

    # Ingrese la función objetivo 10x_1 + 14x_2 + 12x_3 + 18x_4 + 20x_5 + 16x_6.
    m.setObjective(10 * X[0] + 14 * X[1] + 12 * X[2]+ 18 * X[3] + 20 * X[4] + 16 * X[5], GRB.MINIMIZE)

    ## Cree las restricciones del problema
    # Restriccion 1: x_1 + x_2 + 3x_4 + 2x_5 + x_6 >= 26.
    m.addConstr(X[0] + X[1] + 3 * X[3] + 2 * X[4] + X[5] >= 26, name="c1")

    # Restriccion 2: x_1 + x_2 + 3x_4 + 2x_5 + x_6 <=32.
    m.addConstr(X[0] + X[1] + 3 * X[3] + 2 * X[4] + X[5] <= 32, name="c2")

    # Restriccion 3: x_1 + 2x_2 + x_3 + x_4 + x_5 >= 25.
    m.addConstr(X[0] + 2 * X[1] + X[2] + X[3] + X[4] >= 25, name="c3")

    # Restriccion 4: x_2 + 2x_3 + 2x_5 + 2x_6 = 30.
    m.addConstr(X[1] + 2 * X[2] + 2*X[4] + 2*X[5] == 30, name="c4")

    # Restriccion 5: x_1 + x_4 + x_6 <= 14.
    m.addConstr(X[0] + X[3] + X[5] <= 14, name="c5")

    # Optimice el modelo
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')