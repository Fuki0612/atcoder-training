c = input()

colors = ["B","Y","R"]

index = colors.index(c)

print(colors[(index + 1) % 3])