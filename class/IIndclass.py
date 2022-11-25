class first():
    def __init__(self, name):
        self.name = name

    def add(rally, age):
        rally.age = age
        print(rally.name, rally.age, "im first")

    def __str__(self) -> str:
        return f'{self.name}("hello")'


class third():
    def ss(sss):
        print("im third")

    def diff(self):
        a = int(input())
        b = list(map(str, input("enter the desired special characters").split()))
        for i in range(1, a):
            for j in range(i, a):
                if j == i or i == 1:
                    print(b[0], end=" ")
                else:
                     print(" ", end=" ")
            if i != a-1:
                for k in range(0, i):
                    if k == 0 or k == (i-1):
                        print(b[1], end=" ")
                    else:
                        print(" ", end=" ")
            else:
                for k in range(0, i):
                    print(b[1], end=" ")
            print()
