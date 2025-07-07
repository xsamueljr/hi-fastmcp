from math import sqrt
from maths.application.dtos.quadratic_equation_result import QuadraticEquationResult
from maths.domain.exceptions.negative import NumberCannotBeNegative


class SolveQuadraticEquationUseCase:
    
    def run(self, a: int, b: int, c: int) -> QuadraticEquationResult:
        numerator = b**2 - (4 * a * c)
        
        if numerator < 0:
            raise NumberCannotBeNegative("No es posible sacar raíz cuadrada de un número negativo, operación cancelada")
        
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
        return QuadraticEquationResult(x1, x2)
