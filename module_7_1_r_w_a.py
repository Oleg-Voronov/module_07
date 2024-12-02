class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name} {self.weight} {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name,'r')
        s_=file.read()
        file.close()
        return s_
    def add(self,*product):
        file = open(self.__file_name, 'a')
        s_= self.get_products()

        for prod in product:
            ss = prod.name +' '+str(prod.weight)+' '+prod.category
            if s_.find(ss) == -1:
                ss=ss+'\n'
                file.write(ss)
                s_+=ss
            else:
                print(f'Продукт {prod.name} уже есть в магазине')

        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Apple', 7.5, 'Vegetables')
p5 = Product('Banana', 75.3, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3,p4,p5)
print(s1.get_products())
