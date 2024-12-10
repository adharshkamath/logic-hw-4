from z3 import *

solver = Solver()
s = DeclareSort('S')
e, a, b = Consts('e a b', s)
f = Function('f', s, s, s) # group operation
g = Function('g', s, s) # inverse operation


formulae = [
    f(f(a, a), a) == f(a, f(a, a)),
    f(f(a, a), b) == f(a, f(a, b)),
    f(f(a, b), a) == f(a, f(b, a)),
    f(f(a, b), b) == f(a, f(b, b)),
    f(f(b, a), a) == f(b, f(a, a)),
    f(f(b, a), b) == f(b, f(a, b)),
    f(f(b, b), a) == f(b, f(b, a)),
    f(f(b, b), b) == f(b, f(b, b)),

    f(f(a, a), e) == f(a, f(a, e)),
    f(f(a, e), a) == f(a, f(e, a)),
    f(f(a, e), e) == f(a, f(e, e)),
    f(f(e, a), a) == f(e, f(a, a)),
    f(f(e, a), e) == f(e, f(a, e)),
    f(f(e, e), a) == f(e, f(e, a)),
    f(f(e, e), e) == f(e, f(e, e)),

    f(f(b, b), e) == f(b, f(b, e)),
    f(f(b, e), b) == f(b, f(e, b)),
    f(f(b, e), e) == f(b, f(e, e)),
    f(f(e, b), b) == f(e, f(b, b)),
    f(f(e, b), e) == f(e, f(b, e)),
    f(f(e, e), b) == f(e, f(e, b)),

    f(f(a, b), e) == f(a, f(b, e)),
    f(f(a, e), b) == f(a, f(e, b)),
    f(f(e, a), b) == f(e, f(a, b)),
    
    f(f(e, b), a) == f(e, f(b, a)),
    f(f(b, e), a) == f(b, f(e, a)),
    f(f(b, a), e) == f(b, f(a, e)),

    And(f(a, e) == a, f(e, a) == a),
    And(f(b, e) == b, f(e, b) == b),
    And(f(e, e) == e, f(e, e) == e),

    And(f(a, g(a)) == e, f(g(a), a) == e),
    And(f(b, g(b)) == e, f(g(b), b) == e),
    And(f(e, g(e)) == e, f(g(e), e) == e),

    And(f(a, b) == e, f(b, a) == e, Not(b == g(a))),
]




solver.add(formulae)

if solver.check() == sat:
    print(solver.model())
else:
    print("unsat")
