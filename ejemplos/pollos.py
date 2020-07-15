__author__ = "Paola Soto"

#!/usr/bin/env python3.7

"""
En una granja de pollos se da una dieta, para engordar, con una composición mínima de 15 unidades de una sustancia A y 
otras 15 de una sustancia B. En el mercado solo se encuentran dos clases de compuestos: el tipo X con una composición 
de una unidad de A y 5 de B, y el otro tipo, Y, con una composición de cinco unidades de A y una de B. El precio del 
tipo X es de 10 pesos y del tipo Y es de 30 pesos. ¿Que cantidades se han de comprar de cada tipo para cubrir las 
necesidades con un coste mínimo?
"""

import gurobipy as gp
from gurobipy import GRB

try:
    # Crea un nuevo modelo
    m = gp.Model("pollos")

    # Crea las variables
    x = m.addVar(vtype=GRB.CONTINUOUS, name="x")
    y = m.addVar(vtype=GRB.CONTINUOUS, name="y")

    # Ingrese la función objetivo
    m.setObjective(10 * x + 30 * y, GRB.MINIMIZE)

    # Añada las restricciones de composición mínima: x + 5 y >= 15 (Composiciones Sustancia A)
    m.addConstr(x + 5 * y  >= 15, "cA")

    # Añada las restricciones de composición mínima: 5 x + y >= 15 (Composiciones Sustancia b)
    m.addConstr(5 * x + y >= 15, "cB")

    # Optimice el modelo
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')