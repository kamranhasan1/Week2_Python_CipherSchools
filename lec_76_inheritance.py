class h:
    def __init__(self,j,k,l,m):
        self.j=j
        self.k=k
        self.l=l
        self.m=m(print,0)
    def full_mane(self):
        return f"{self.j}{self.k}"
    def make_a_call(self,number):
        return f"calling{number}..."
