
import pytest
import solucion_correcta as sol

def test_creacion_de_bebidas():
    flan = sol.Postre("flan", 5000, False, 100,  ["dulce de leche", "crema"])
    assert flan.nombre == "flan"
    assert flan.precio_base == 5000

def test_precio_de_bebidas():
    agua_mini = sol.Bebida("agua", 1000, True, 1, 300)
    agua_mediana = sol.Bebida("agua", 2000, True, 1, 500)
    agua_grande = sol.Bebida("agua", 3000, True, 1, 1000)

    assert agua_mini.precio() == 1000
    assert agua_mediana.precio() == 2800 # 2000 + 2000*0.4 = 2800
    assert agua_grande.precio() == 4200

def test_precio_de_bebidas_con_diccionario():
    agua_mini = sol.Bebida("agua", 1000, True, 1, 300)
    agua_mediana = sol.Bebida("agua", 2000, True, 1, 500)
    agua_grande = sol.Bebida("agua", 3000, True, 1, 1000)
    
    valores_esperados = {
        agua_mini: 1000,
        agua_mediana: 2800,
        agua_grande: 4200
    }

    for agua, valor in valores_esperados.items():
        assert agua.precio() == valor


def test_precio_de_postres():
    postre_sin_topping = sol.Postre("helado", 1000, True, 1, [])
    assert postre_sin_topping.precio() == postre_sin_topping.precio_base

    flan_con_ddl = sol.Postre("flan", 1000, False, 1, ["dulce de leche"])
    assert flan_con_ddl.precio() == flan_con_ddl.precio_base + len(flan_con_ddl.toppings)*300