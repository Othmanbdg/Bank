class bank:
    def __init__(self):
        self.account=0


    def withdraw(self,value):
        if value>self.account:
            print("T'as pas assez")
        else:
            self.account-=value

    def add(self,values):
        self.account+=values

    def sold(self):
        print(self.account)

