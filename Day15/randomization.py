import random

# 1. random() – float between 0.0 and 1.0
print("random():", random.random())

# 2. randint(a, b) – integer between a and b (inclusive)
print("randint(1, 10):", random.randint(1, 10))

# 3. uniform(a, b) – float between a and b
print("uniform(5, 15):", random.uniform(5, 15))

# 4. choice(seq) – random element from sequence
colors = ['red', 'green', 'blue']
print("choice(colors):", random.choice(colors))

# 5. choices(seq, k=n) – list of n elements (with replacement)
cards = ['A', 'K', 'Q', 'J']
print("choices(cards, k=3):", random.choices(cards, k=3))

# 6. sample(seq, k=n) – list of n unique elements (without replacement)
lottery = list(range(1, 50))
print("sample(lottery, k=6):", random.sample(lottery, k=6))

# 7. shuffle(seq) – shuffle list in place
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print("shuffle(nums):", nums)

# 8. randrange(start, stop, step) – random number from range
print("randrange(0, 10, 2):", random.randrange(0, 10, 2))

# 9. getrandbits(n) – integer with n random bits
print("getrandbits(4):", random.getrandbits(4))  # 4 bits = 0 to 15

# 10. seed(x) – set seed for reproducibility
random.seed(60)
print("Seeded randint(1, 10):", random.randint(1, 10))

