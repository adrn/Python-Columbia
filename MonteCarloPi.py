# Calculate Pi using a Monte Carlo method

import math
import random

random.seed(1)

def compute_pi(number_of_iterations):
    """ Given a maximum number of iterations,
        compute the value of Pi using a Monte Carlo 
        method
    """
    number_of_points_inside_circle = 0.
    for ii in range(number_of_iterations):
        # random.random() returns a uniform random number between 0 and 1
        distance = random.random()**2 + random.random()**2
        
        # If the point we drew lies in a unit circle
        if distance <= 1.0:
            number_of_points_inside_circle += 1
    
    # Only computes it for the top right quadrant, so we have to multiply
    #   by 4 to get the true value
    return 4.0 * number_of_points_inside_circle / number_of_iterations

for number_of_iterations in [10**x for x in range(1,7)]:
    print(compute_pi(number_of_iterations))