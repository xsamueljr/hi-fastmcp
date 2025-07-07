from math import sqrt


class CalculateSquareRootUseCase:

    def __init__(self) -> None:
        pass
    
    def run(self, x: int) -> float:
        return sqrt(x)
