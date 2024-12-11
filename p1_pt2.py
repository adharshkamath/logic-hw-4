from z3 import *

solver = Solver()
solver.set(unsat_core=True)
s = DeclareSort('S')
e, a, b, c = Consts('e a b c', s)
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

    f(f(a, a), c) == f(a, f(a, c)),
    f(f(a, c), a) == f(a, f(c, a)),
    f(f(a, c), c) == f(a, f(c, c)),
    f(f(c, a), a) == f(c, f(a, a)),
    f(f(c, a), c) == f(c, f(a, c)),
    f(f(c, c), a) == f(c, f(c, a)),
    f(f(c, c), c) == f(c, f(c, c)),

    f(f(b, b), c) == f(b, f(b, c)),
    f(f(b, c), b) == f(b, f(c, b)),
    f(f(b, c), c) == f(b, f(c, c)),
    f(f(c, b), b) == f(c, f(b, b)),
    f(f(c, b), c) == f(c, f(b, c)),
    f(f(c, c), b) == f(c, f(c, b)),

    f(f(a, b), c) == f(a, f(b, c)),
    f(f(a, c), b) == f(a, f(c, b)),
    f(f(b, a), c) == f(b, f(a, c)),
    f(f(b, c), a) == f(b, f(c, a)),
    f(f(c, a), b) == f(c, f(a, b)),
    f(f(c, b), a) == f(c, f(b, a)),

    f(f(e, e), c) == f(e, f(e, c)),
    f(f(e, c), e) == f(e, f(c, e)),
    f(f(c, e), e) == f(c, f(e, e)),
    f(f(c, e), c) == f(c, f(e, c)),
    f(f(c, c), e) == f(c, f(c, e)),

    f(f(a, e), c) == f(a, f(e, c)),
    f(f(e, a), c) == f(e, f(a, c)),
    f(f(e, c), a) == f(e, f(c, a)),
    f(f(c, a), e) == f(c, f(a, e)),
    f(f(c, e), a) == f(c, f(e, a)),

    f(f(b, e), c) == f(b, f(e, c)),
    f(f(e, b), c) == f(e, f(b, c)),
    f(f(e, c), b) == f(e, f(c, b)),
    f(f(c, b), e) == f(c, f(b, e)),
    f(f(c, e), b) == f(c, f(e, b)),

    f(f(a, b), e) == f(a, f(b, e)),
    f(f(a, e), b) == f(a, f(e, b)),
    f(f(e, a), b) == f(e, f(a, b)),
    
    f(f(e, b), a) == f(e, f(b, a)),
    f(f(b, e), a) == f(b, f(e, a)),
    f(f(b, a), e) == f(b, f(a, e)),

    And(f(a, e) == a, f(e, a) == a),
    And(f(b, e) == b, f(e, b) == b),
    And(f(e, e) == e, f(e, e) == e),
    And(f(c, e) == c, f(e, c) == c),

    And(f(a, g(a)) == e, f(g(a), a) == e),
    And(f(b, g(b)) == e, f(g(b), b) == e),
    And(f(e, g(e)) == e, f(g(e), e) == e),
    And(f(c, g(c)) == e, f(g(c), c) == e),

    And(f(a, b) == e, f(b, a) == e, f(a, c) == e, f(c, a) == e, Not(b == c)),
]


for f in formulae:
    solver.assert_and_track(f, str(f))


# solver.add(formulae)

if solver.check() == sat:
    print(solver.model())
else:
    print("unsat")
    print(solver.unsat_core())
