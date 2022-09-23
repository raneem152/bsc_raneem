


def RightTriangle(height):
    for i in range(int(height)):
        for j in range(i + 1):
            print('*', end='')
        print()


def Square(height):
    height = int(height)
for i in range(int(height)):
    for x in range(height, 2 * height):
        print(height * ' * ')
print('')


def tiangle(height):
    height = int(height)


for _ in range():
    for x in range(1, height + 1):
        print(x * '*')
print('')


def rectangle(height):
    height = input('Please enter the number of rows: ')


height = int(height)
for _ in range(numrect):
    for x in range(1, 2 * height):
        print(height * ' * ')
print('')

l1 = []
l2 = []
print("valid shapes: trangle , square , righttriangle , rectangle")
n = int(input("enter the number of shapes: "))
for i in range(1, n):
    shape = input("enter the shape name: ")
    height = int(input("enter th height of the shape:"))
    l1.insert(1, shape)
    l2.insert(1, height)
    l3 = list(zip(l2, l1))
    l3.sort()

print("list of tupels of shapes is :")
print(l3)
print()

# drwaing the shapes
for i in range(1, n):
    if l1[i] == "pyramid":
        triangle(l2[i])
    elif l1[i] == "square":
        square(l2[i])
    elif l1[i] == "righttriangle":
        RightTriangle(l2[i])
    elif l1[i] == "rectangle":
        rectangle(l2[i])
    else:
        print("invalid shape")
print("\n\n")


