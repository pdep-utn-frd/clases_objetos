# Repaso: Banco Delta

El banco **Banco Delta** necesita un sistema para administrar las cuentas de sus clientes y operar con ellas sin errores. El sistema tiene que representar las cuentas, calcular el interés o la comisión de cada una según su tipo, agrupar las cuentas de la sucursal y mover plata entre ellas sin sorpresas.


## Punto 1: las cuentas

Modelar las cuentas de los usuarios, de las mismas conocemos quien es su titular y el saldo actual.
Sabemos que dada una cuenta, podemos tanto depositar como extraer un determinado monto (positivo).
Ademas, se sabe que dada una cuenta, podemos preguntar cuanto es el interes mensual que genera. Por ahora el mismo debe ser 0.


## Punto 2: cajas de ahorro y cuentas corrientes

Ahora, no todas las cuentas generan el mismo interés ni cobran la misma comisión:

- **`CajaAhorro`**: además de lo anterior, tiene una `tasa` (por ejemplo `0.05` para 5%). Genera un interés de `saldo × tasa`, pero **solo si el saldo es de $100.000 o más**. Si no llega a ese mínimo, no genera interés.
- **`CuentaCorriente`**: tiene una `comision_base` (número) y una lista de `cheques` emitidos (strings). Su "interés" es **negativo**: paga `comision_base` más **$200 por cada cheque** emitido.

Pistas:

- `CajaAhorro` y `CuentaCorriente` deben ser clases y **heredar** de `Cuenta` y redefinir `interes_mensual()`.
- Los constructores deben reutilizar el de `Cuenta` mediante `super()`, sin copiar la asignación de atributos.
- El interés debe resolverse por **polimorfismo**: está prohibido preguntar de qué tipo es una cuenta (nada de `isinstance` ni atributos tipo `cuenta.tipo == "caja_ahorro"`).

## Punto 3: el banco

Modelar la clase `Banco`:

- Un banco nuevo empieza **sin cuentas**.
- Sabemos que los bancos cuentan con un metodo `abrir_cuenta(cuenta)` que agrega una cuenta al banco.
- Tambien cuentan con un metodo `patrimonio_total()` que devuelve la suma de los saldos de todas sus cuentas.

`Banco` no debe saber si una cuenta es caja de ahorro o corriente: le pide a cada una su saldo (y su `interes_mensual()` cuando haga falta) y el polimorfismo hace el resto.

## Punto 4: ajustes y consultas

Implementar las siguientes funcionalidades:

- `cuentas_en_rojo(cuentas)`: dada una lista de cuentas, devuelve las que tienen `saldo < 0`.
- `crear_ajuste(porcentaje)`: devuelve una **función** que recibe una cuenta y devuelve su saldo con el ajuste aplicado (por ejemplo, una actualización por inflación). `con_ajuste = crear_ajuste(10)` permite calcular los saldos actualizados con `list(map(con_ajuste, cuentas))`. Pista: La funcion debe devolver una expresion lambda. De esa manera su valor de retorno puede utilizarse en un map. 
- `todas_con_fondos(cuentas)`: `True` si **todas** las cuentas tienen `saldo > 0`.
- `hay_cuenta_rica(cuentas, tope)`: `True` si **al menos una** cuenta tiene saldo mayor que `tope`.

## Punto 5: operar sin mentiras

Llega el momento de mover plata, y con él los problemas:

- `Cuenta.extraer(monto)`: si el `monto` es mayor que el saldo, debe lanzar la excepción `SaldoInsuficienteError`. Si no, se descuenta del saldo.
- `Cuenta.depositar(monto)` y `Cuenta.extraer(monto)`: si el `monto` es **menor o igual a 0**, debe lanzar la excepción `MontoInvalidoError`.
- `transferir(origen, destino, monto)`: extrae `monto` de la cuenta `origen` y lo deposita en `destino`. Si la extracción falla, la excepción debe propagarse (no se deposita nada).

Requisitos:

- `SaldoInsuficienteError` y `MontoInvalidoError` deben ser clases propias que hereden de `Exception`.
- **NO** se puede señalar errores devolviendo strings o `None`.
- Escribir un `main()` que abra cuentas, opere con ellas, y muestre con `try/except` qué pasa al extraer de más, al depositar un monto inválido y al transferir.

## Ejemplo

Con estas cuentas:

| Titular | Tipo             | Saldo     | Detalle                    |
|---------|------------------|----------:|----------------------------|
| Ana     | Caja de ahorro   | $150.000  | tasa 5%                    |
| Beto    | Caja de ahorro   | $50.000   | tasa 5%                    |
| Caro    | Cuenta corriente | $200.000  | comisión $1.000, 2 cheques |
| Dani    | Cuenta corriente | -$5.000   | comisión $1.000, 0 cheques |

- La caja de ahorro de Ana genera $150.000 × 0,05 = **$7.500** de interés.
- La de Beto genera **$0** (su saldo no llega al mínimo de $100.000).
- La cuenta corriente de Caro tiene un ajuste de **-$1.400** ($1.000 + 2 × $200).
- `patrimonio_total()` del banco da **$395.000**.
- `crear_ajuste(10)` aplicado a la cuenta de Ana da **$165.000**.
- `cuentas_en_rojo(cuentas)` da `[Dani]`; `todas_con_fondos(cuentas)` da `False` (Dani está en rojo); `hay_cuenta_rica(cuentas, 100000)` da `True`.
- Extraer $999.999 de la cuenta de Ana lanza `SaldoInsuficienteError`; depositar -$100 lanza `MontoInvalidoError`.

## Tests

Escribir tests con `pytest` para los puntos 2, 3 y 5.
