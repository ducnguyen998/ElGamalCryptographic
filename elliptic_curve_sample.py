
from elliptic_curve import (
    EllipticCurve
)

# Elliptic curve (E) : y^2 = x^3 + 2x + 6 mod 11
elliptic_curve = EllipticCurve(11,2,6)
elliptic_curve.find_ellipse()

# Elliptic curve (E) : y^2 = x^3 + 2x + 2 mod 17
elliptic_curve = EllipticCurve(17,2,2)
elliptic_curve.find_ellipse()

# Elliptic curve (E) : p = 83
elliptic_curve = EllipticCurve(83)
elliptic_curve.find_ellipse()

# Elliptic curve (E) : p = 89
elliptic_curve = EllipticCurve(89)
elliptic_curve.find_ellipse()

# Elliptic curve (E) : p = 97
elliptic_curve = EllipticCurve(97)
elliptic_curve.find_ellipse()