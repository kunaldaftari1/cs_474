from z3 import *

p = Bool('p')
q = Bool('q')
r = Bool('r')

original_formula = And(
    Or(q, Not(r)),             # (q ∨ ¬r)
    Or(Not(p), r),             # (¬p ∨ r)
    Or(Not(q), r, p),          # (¬q ∨ r ∨ p)
    Or(p, q, Not(q)),          # (p ∨ q ∨ ¬q)
    Or(Not(r), q)              # (¬r ∨ q)
)

solver = Solver()
solver.add(original_formula)

if solver.check() == sat:
    print("The formula is satisfiable.")
    print("Model:", solver.model())
else:
    print("The formula is not satisfiable.")