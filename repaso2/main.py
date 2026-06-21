class Cuenta:
    def __init__(self, titular, saldo, tipo="simple", tasa=0,
                 comision_base=0, cheques=None):
        self.titular = titular
        self.saldo = saldo
        self.tipo = tipo
        self.tasa = tasa
        self.comision_base = comision_base
        self.cheques = cheques if cheques is not None else []

    def depositar(self, monto):
        self.saldo = self.saldo + monto

    def extraer(self, monto):
        if monto > self.saldo:
            return "Error: " + self.titular + " no tiene saldo suficiente"
        self.saldo = self.saldo - monto

    def interes_mensual(self):
        if self.tipo == "caja_ahorro":
            if self.saldo >= 100000:
                return self.saldo * self.tasa
            return 0
        elif self.tipo == "corriente":
            comision = self.comision_base
            for _ in self.cheques:
                comision = comision + 200
            return -comision
        else:
            return 0


class Banco:
    def __init__(self):
        self.cuentas = []

    def abrir_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def patrimonio_total(self):
        suma = 0
        for c in self.cuentas:
            suma = suma + c.saldo
        return suma


def cuentas_en_rojo(cuentas):
    resultado = []
    for c in cuentas:
        if c.saldo < 0:
            resultado.append(c)
    return resultado


def crear_ajuste(porcentaje):
    def aplicar(cuenta):
        return cuenta.saldo * (1 + porcentaje / 100)
    return aplicar


def todas_con_fondos(cuentas):
    for c in cuentas:
        if c.saldo <= 0:
            return False
    return True


def hay_cuenta_rica(cuentas, tope):
    for c in cuentas:
        if c.saldo > tope:
            return True
    return False


def transferir(origen, destino, monto):
    error = origen.extraer(monto)
    if error is not None:
        return error
    destino.depositar(monto)


def main():
    ana = Cuenta("Ana", 150000, tipo="caja_ahorro", tasa=0.05)
    beto = Cuenta("Beto", 50000, tipo="caja_ahorro", tasa=0.05)
    caro = Cuenta("Caro", 200000, tipo="corriente",
                  comision_base=1000, cheques=["luz", "gas"])
    dani = Cuenta("Dani", -5000, tipo="corriente", comision_base=1000)
    cuentas = [ana, beto, caro, dani]

    print("Interés de Ana:", ana.interes_mensual())
    print("Ajuste de Caro:", caro.interes_mensual())

    banco = Banco()
    for c in cuentas:
        banco.abrir_cuenta(c)
    print("Patrimonio total:", banco.patrimonio_total())

    en_rojo = cuentas_en_rojo(cuentas)
    print("En rojo:", [c.titular for c in en_rojo])

    con_ajuste = crear_ajuste(10)
    saldos_ajustados = []
    for c in cuentas:
        saldos_ajustados.append(con_ajuste(c))
    print("Saldos con 10% de ajuste:", saldos_ajustados)

    print("¿Todas con fondos?", todas_con_fondos(cuentas))
    print("¿Hay cuenta con más de 100000?", hay_cuenta_rica(cuentas, 100000))

    # Punto 5: extraer de más
    resultado = ana.extraer(999999)
    if type(resultado) == str:
        print("No se pudo extraer:", resultado)

    # Punto 5: transferir
    error = transferir(ana, beto, 50000)
    if error is not None:
        print("No se pudo transferir:", error)
    print("Saldo de Ana:", ana.saldo, "- Saldo de Beto:", beto.saldo)


if __name__ == "__main__":
    main()
