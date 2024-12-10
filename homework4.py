from z3 import *

f = Function('f', IntSort(), IntSort(), IntSort())
e = Int('e')
c = Int('c')

g = Function('g', IntSort(), IntSort())

constraints = [
    f(f(e, e), e) == f(e, f(e, e)),
    f(f(e, e), c) == f(e, f(e, c)),
    f(f(e, c), e) == f(e, f(c, e)),
    f(f(e, c), c) == f(e, f(c, c)),
    f(f(c, e), e) == f(c, f(e, e)),
    f(f(c, e), c) == f(c, f(e, c)),
    f(f(c, c), e) == f(c, f(c, e)),
    f(f(c, c), c) == f(c, f(c, c)),
    f(e, e) == e,
    f(c, e) == c,
    f(e, c) == c,
    f(e, g(e)) == e,
    f(g(e), e) == e,
    f(e, c) == e,
    f(c, e) == e,
    e != c,
    f(c, c) == c,
]

solver = Solver()
solver.add(constraints)

if solver.check() == sat:
    print("The formulas are satisfiable.")
    print("Example model:")
    print(solver.model())
else:
    print("The formulas are unsatisfiable.")
