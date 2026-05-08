import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())

# Generating sequence
sequence = np.arange(start, stop, step)

# Printing result
print(sequence)
