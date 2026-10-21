height = 100
rebounce = 3 / 5

for i in range(10):
    height = height * rebounce
    print(i + 1, round(height, 4))
