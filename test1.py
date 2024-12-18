from test2 import FileReader

z = FileReader("sample.txt")
print(z)

z = 20
z = list(range(z))

while z > 0:
    z -= 5
    print(f"Remaining: {z}")
