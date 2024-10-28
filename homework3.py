from z3 import *
# File 1 
l1, u1, l2, u2, z, w = Reals('l1 u1 l2 u2 z w')
inner_formula = And(l1 < w, w < u1, l2 < w, w < u2, w != z)
qe_result = Tactic('qe')(Exists(w, inner_formula))
print("Quantifier elimination result for inner formula:", qe_result)
# File 2
from z3 import *
# Define the real variables
l1, u1, l2, u2, z = Reals('l1 u1 l2 u2 z')
inner_result = Or(
    And(Not(l1 < u2), Not(u1 < u2), Not(l2 < u2), Or(Not(z < u2), Not(z > u2))),
    And(Not(l1 < z), Not(u1 > z), Not(l2 < z), u2 <= z),
    And(Not(l1 < u1), Not(l2 < u1), u2 <= u1, Or(z <= u1, Not(z > u1)))
)
outer_formula_with_sub = ForAll(z, Implies(And(l1 < z, z < u1, l2 < z, z < u2), inner_result))
final_qe_result = Tactic('qe')(outer_formula_with_sub)
print("Quantifier elimination result for the outer formula with substitution:", final_qe_result)
# File 3
from z3 import *
x, y = Reals('x y')
inner_formula = And(2 * y > 3 * x, 4 * y < 8 * x + 10)
formula = ForAll([x], Exists([y], inner_formula))
qe = Tactic('qe')
qe_result = qe(formula)
print(qe_result)
