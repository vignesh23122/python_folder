class a:
    def __init__(self,na) -> None:
        self.name=na
    def mymethod(self):
        return self.na
class b(a):
    def __init__(self, nu) -> None:
        super().__init__(nu)
        self.na=nu
    def inherited(rj):
        super().mymethod()
        print(rj.na,"b class printed")


k=b(input())
k.inherited()