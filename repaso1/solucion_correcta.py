class Producto:
    def __init__(self, nombre, precio_base, apto_vegano, stock):
        self.nombre = nombre
        self.precio_base = precio_base
        self.apto_vegano = apto_vegano
        self.stock = stock

    def precio(self):
        return self.precio_base

class Bebida(Producto):
    def __init__(self, nombre, precio_base, apto_vegano, stock, ml):
        self.nombre = nombre
        self.precio_base = precio_base
        self.apto_vegano = apto_vegano
        self.stock = stock
        self.ml = ml

    def precio(self):
        if self.ml >= 500:
            return round(self.precio_base * 1.4, 2)
        return self.precio_base

class Postre(Producto):
    def __init__(self, nombre, precio_base, apto_vegano, stock, toppings):
        self.nombre = nombre
        self.precio_base = precio_base
        self.apto_vegano = apto_vegano
        self.stock = stock
        self.toppings = toppings

    def precio(self):
        precios_de_toppings = {
            "ddl": 300,
            "crema": 200,
            "pistacho": 400
        }
        cantidad_de_toppings = len(self.toppings)
        return self.precio_base + cantidad_de_toppings * 300