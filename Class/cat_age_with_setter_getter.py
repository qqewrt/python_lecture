class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return 'Cat(name='+self.name+',color='+str(self.age)+')'
    
    def set_age(self,age):
        if age>0:
            self.age = age
    def get_age(self):
        return self.age

nabi = Cat('나비',3)
print(nabi)
nabi.set_age(4)
nabi.set_age(-5)
print(nabi)