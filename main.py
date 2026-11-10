from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Test the ValueError path
try:
    calculate([1, 2, 3])
except ValueError as e:
    print("ValueError:", e)