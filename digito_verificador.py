"""Calcula el dígito verificador (DV) de un RUT chileno.

El dígito verificador se obtiene con el algoritmo módulo 11: se multiplican los
dígitos del RUT de derecha a izquierda por la secuencia 2, 3, 4, 5, 6, 7, 2, 3,
...; se suman los productos; se calcula el resto de dividir esa suma por 11; y
el DV es 11 menos ese resto, con las equivalencias 11 -> 0 y 10 -> K.
"""


def calcular_dv(rut: int) -> str:
    """Devuelve el dígito verificador de un RUT numérico.

    Args:
        rut: RUT sin puntos ni dígito verificador (por ejemplo, 12345678).

    Returns:
        El dígito verificador como texto: "0".."9" o "K".
    """
    suma = 0
    multiplicador = 2

    for digito in reversed(str(rut)):
        suma += int(digito) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1

    resto = suma % 11
    dv = 11 - resto

    if dv == 11:
        return "0"
    if dv == 10:
        return "K"
    return str(dv)


def main() -> None:
    print("Este programa devuelve el dígito verificador de un RUT.")
    print("Ingresa el RUT de 8 números, sin puntos ni dígito verificador.")

    try:
        rut = int(input("RUT: ").strip())
    except ValueError:
        print("El RUT debe ser un número entero.")
        return

    print(f"El RUT con dígito verificador es: {rut}-{calcular_dv(rut)}")


if __name__ == "__main__":
    main()
