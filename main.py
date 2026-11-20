import sys
import numpy as np
import pandas as pd

print("Python development environment is ready!")

print("Python executable:", sys.executable)

numbers = np.array([10, 20, 30, 40, 50])

print("NumPy average:", np.mean(numbers))

data = {"Name": ["Ahmed", "Ali", "Omar"], "Age": [20, 21, 19]}

df = pd.DataFrame(data)

print(df)
