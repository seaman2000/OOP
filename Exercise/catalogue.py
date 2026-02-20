class Catalogue:
    list_of_catalogues = []

    def __init__(self, name:str):
        self.name = name

    def add_product(self, product_name:str):
        Catalogue.list_of_catalogues.append(product_name)

    def get_by_letter(self, first_letter: str):
        catalogue = [product for product in Catalogue.list_of_catalogues if product.startswith(first_letter)]
        return catalogue

    def __repr__(self):
        print (f"Items in the {self.name} catalogue:")
        for item in sorted(Catalogue.list_of_catalogues):
            print(item)

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

