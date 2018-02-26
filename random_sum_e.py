# Python simulation of the following proof, via Fermat's Library:

# "If you pick a uniformly random real number in [0,1] and repeat this until the sum of the 
# numbers picked is greater than 1, you'll on average pick e = 2.718... numbers."
# Source: https://twitter.com/fermatslibrary/status/924263998589145090

# by Andrew Chamberlain, Ph.D.
# October 2017
# achamberlain.com

# Import packages. 
import numpy as np

# Create an empty array for counts of guessed random numbers.
n = []

for i in range(100000): 
    a = [] # Create an empty array for the set of summed random numbers. 
    x = np.random.uniform(low=0.0, high=1.0,size=1) # Start with first random number.
    a.append(x) # Put first random number in the array a.
    while x <= 1: # As long as sum of random numbers is <= 1, run this. 
        x += np.random.uniform(low=0.0, high=1.0,size=1) # Add another random number. 
        a.append(x) # Add new sum to array a.
    d = len(a) # Count the number of guesses in array a. 
    n.append(d) # Once x > 1, put the number of guesses into array n.

mu = np.mean(n) # Across N replications show the mean number of guesses to get x > 1. Converges to e = 2.718...
print("Average numbers picked:", mu)


