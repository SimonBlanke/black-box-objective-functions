# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from .._base_objective_function import MathematicalFunction


class RosenbrockFunction(MathematicalFunction):
    name = "Rosenbrock Function"
    _name_ = "rosenbrock_function"
    __name__ = "RosenbrockFunction"

    explanation = """
    
    """

    reference = """
    
    """

    dimensions = "n"
    formula = r"""f(\vec {x}) = \sum_{i=1}^{n-1} \left[ 100 \left(x_{i+1} - x_{i}^{2}\right)^{2} + \left(1 - x_{i}\right)^{2}\right]"""
    global_minimum = r"""f(1,1) = 0"""

    def __init__(
        self,
        n_dim,
        A=1,
        B=100,
        metric="score",
        input_type="dictionary",
        sleep=0,
    ):
        super().__init__(metric, input_type, sleep)
        self.n_dim = n_dim

        self.A = A
        self.B = B

    def create_objective_function(self):
        def rosenbrock_function(params):
            loss = 0
            for dim in range(self.n_dim - 1):
                dim_str = "x" + str(dim)
                dim_str_1 = "x" + str(dim + 1)

                x = params[dim_str]
                y = params[dim_str_1]

                loss += (self.A - x) ** 2 + self.B * (y - x**2) ** 2
            return loss

        self.pure_objective_function = rosenbrock_function

    def search_space(self, min=-5, max=5, step=0.1, value_types="array"):
        return super().create_n_dim_search_space(min, max, step, value_types)
