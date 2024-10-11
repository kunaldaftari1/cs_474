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

new_formula = And(
    Or(Not(r), q),             # Clause 1: (!r ∨ q)
    Or(r, Not(p)),             # Clause 2: (r ∨ !p)
    Or(p, r, Not(q)),          # Clause 3: (p ∨ r ∨ !q)
    Or(q, Not(p)),             # Clause 4: (q ∨ !p)
    Or(r, Not(q))              # Clause 5: (r ∨ !q)
)

equivalence = And(
    Implies(original_formula, new_formula),  # original_formula → new_formula
    Implies(new_formula, original_formula)   # new_formula → original_formula
)

solver = Solver()

solver.add(Not(equivalence))  

if solver.check() == unsat:
    print("The original formula and the new formula are equivalent.")
else:
    print("The original formula and the new formula are not equivalent.")
