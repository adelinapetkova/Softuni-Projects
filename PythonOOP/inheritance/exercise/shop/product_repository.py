from inheritance.exercise.shop.product import Product


class ProductRepository:
    def __init__(self):
        self.products=[]

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for pr in self.products:
            if pr.name==product_name:
                return pr

    def remove(self,product_name):
        for pr in self.products:
            if pr.name==product_name:
                self.products.remove(pr)

    def __repr__(self):
        info=[]
        for pr in self.products:
            info.append(f"{pr.name}: {pr.quantity}")

        return '\n'.join(info)
