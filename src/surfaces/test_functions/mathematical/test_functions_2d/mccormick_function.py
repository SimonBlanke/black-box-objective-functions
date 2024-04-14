# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import numpy as np

from .._base_objective_function import MathematicalFunction


class McCormickFunction(MathematicalFunction):
    name = "Mc Cormick Function"
    _name_ = "mccormick_function"
    __name__ = "McCormickFunction"

    explanation = """
    
    """

    reference = """
    
    """

    dimensions = "2"
    formula = (
        r"""f(x,y) = \sin \left(x+y\right) + \left(x-y\right)^{2} - 1.5x + 2.5y + 1"""
    )
    global_minimum = r"""f(-0.54719, -1.54719) = -1.9133"""

    def __init__(self, metric="score", input_type="dictionary", sleep=0):
        super().__init__(metric, input_type, sleep)
        self.n_dim = 2

    def create_objective_function(self):
        def mccormick_function(params):
            x = params["x0"]
            y = params["x1"]

            return np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

        self.pure_objective_function = mccormick_function

    def search_space(self, value_types="array", size=10000):
        return super().create_n_dim_search_space(
            min=-5, max=5, size=size, value_types=value_types
        )
