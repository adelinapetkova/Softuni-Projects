class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        mylist = []
        for el in self.products:
            if el[0] == first_letter:
                mylist.append(el)
        return mylist

    def __repr__(self):
        output = f'Items in the {self.name} catalogue:\n'
        output += '\n'.join(sorted(self.products))

        return output


catalogue = Catalogue('Furniture')
catalogue.add_product('Sofa')
catalogue.add_product('Mirror')
catalogue.add_product('Desk')
catalogue.add_product('Chair')
catalogue.add_product('Carpet')
print(catalogue.get_by_letter('C'))
print(catalogue)
