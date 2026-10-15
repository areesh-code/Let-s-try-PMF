import math

# Number of coin flips
n = 10

# Probability of getting heads
p = 0.5

# Calculate the probability for 2, 3, and 4 heads
total = 0

for k in range(2, 5):
    probability = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    
    print("Probability of", k, "heads:", probability)
    
    total += probability

# Final answer
print()
print("Probability of getting between 2 and 4 heads:", total)
print("Percentage:", total * 100, "%")