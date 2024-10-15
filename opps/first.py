class first():
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def res(self):
        print("{name} is {age} years old".format(name=self.name,age=self.age))
        self.__sample()
    def __sample(self):
        print("im private")
class second(first):
    def res(self):
        super().res()
        print(self.name,self.age)

        

obj=second("john","20")
obj.res()