from sympy import symbols, Matrix, hadamard_product, Poly, div
from sympy.polys.specialpolys import interpolating_poly
from sympy.abc import x

one, out, x1, x2, x3, x4 = symbols("one out x1 x2 x3 x4")
w = Matrix([one, out, x1, x2, x3, x4])

A = Matrix([[0, 0, -1, 0, 0, 0], [0, 0, -1, 0, 0, 0], [0, 0, 0, -4, 0, 0]])
B = Matrix([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1]])
C = Matrix([[0, 0, 0, 0, -1, 0], [0, 0, 0, 0, 0, -1], [-2, -1, 0, 0, 1, 0]])

print(hadamard_product(A * w, B * w) - C * w)


def lagrange(m):
    result = Matrix()
    rows = m.shape[0]
    xs = list(range(1, rows + 1))
    zeros = [0] * rows
    for i in range(m.shape[1]):
        p = interpolating_poly(rows, x, X=xs, Y=list(m.col(i)))
        coeffs = p.as_poly().all_coeffs() if not p.is_zero else zeros
        while len(coeffs) < rows:
            coeffs.insert(0, 0)
        result = result.col_insert(i + 1, Matrix(coeffs))
    return result


U = lagrange(A)
V = lagrange(B)
W = lagrange(C)
print(U)
print(V)
print(W)

witness = Matrix([1, 74, 2, 3, 4, 6])
Ua = Poly.from_list(list(U * witness), gens=x)
Va = Poly.from_list(list(V * witness), gens=x)
Wa = Poly.from_list(list(W * witness), gens=x)

t = Poly(1, x)
for i in range(U.shape[0]):
    t *= Poly(x - i - 1)

print(Ua * Va - Wa)
print(t)
h = div(Ua * Va - Wa, t)[0]
print(h)

print(Ua * Va - Wa - h * t)
