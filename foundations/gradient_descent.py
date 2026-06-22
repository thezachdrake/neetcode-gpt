class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        val: int = init
        if iterations == 0:
            return val
        for epoch in range(iterations):
            val = val - (learning_rate * (2 * val))
        return round(val, 5)
