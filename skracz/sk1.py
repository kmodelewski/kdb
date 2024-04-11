class Product:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def transform_name_for_sku(self):
        return self.name.uppper

    def transofrm_color_for_sku(self):
        return self.color.upper

    def generate_sku(self):
        name = self.transform_name_for_sku()
        color = self.transofrm_color_for_sku()
        return f'{name}-{self.size}-{self.color}'

