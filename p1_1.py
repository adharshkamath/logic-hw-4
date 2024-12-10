from z3 import *

solver = Solver()
s = DeclareSort('S')
e, e1 = Consts('e e1', s)
f = Function('f', s, s, s) # group operation
g = Function('g', s, s) # inverse operation


formulae = [
    f(f(e, e), e) == f(e, f(e, e)),
    f(f(e, e), e1) == f(e, f(e, e1)),
    f(f(e, e1), e) == f(e, f(e1, e)),
    f(f(e, e1), e1) == f(e, f(e1, e1)),
    f(f(e1, e), e) == f(e1, f(e, e)),
    f(f(e1, e), e1) == f(e1, f(e, e1)),
    f(f(e1, e1), e) == f(e1, f(e1, e)),
    f(f(e1, e1), e1) == f(e1, f(e1, e1)),
    And(f(e, e) == e, f(e, e) == e),
    And(f(e1, e) == e1, f(e, e1) == e1),
    And(f(e, g(e)) == e, f(g(e), e) == e),
    And(f(e1, g(e1)) == e, f(g(e1), e1) == e),
    And(f(e, e1) == e, f(e1, e) == e, Not(e == e1)),
    And(f(e1, e1) == e1, f(e1, e1) == e1, Not(e == e1)),
]

solver.add(formulae)

if solver.check() == sat:
    print(solver.model())
else:
    print("unsat")
