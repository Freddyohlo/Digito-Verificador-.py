# Dígito verificador de RUT chileno

Programa en Python que calcula el **dígito verificador (DV)** de un RUT chileno
usando el algoritmo **módulo 11**.

## 🧮 Cómo funciona

1. Se toma el RUT sin puntos ni dígito verificador.
2. Se multiplican sus dígitos **de derecha a izquierda** por la secuencia
   `2, 3, 4, 5, 6, 7, 2, 3, ...` (se repite al llegar a 7).
3. Se suman los productos.
4. Se calcula el resto de dividir la suma por 11.
5. El DV es `11 - resto`, con dos equivalencias:
   - si el resultado es **11** → `0`
   - si el resultado es **10** → `K`

## 🚀 Uso

Requiere **Python 3.8+**. No necesita dependencias externas.

```bash
python digito_verificador.py
```

```
Este programa devuelve el dígito verificador de un RUT.
Ingresa el RUT de 8 números, sin puntos ni dígito verificador.
RUT: 12345678
El RUT con dígito verificador es: 12345678-5
```

### Como módulo

```python
from digito_verificador import calcular_dv

calcular_dv(12345678)   # '5'
```

## 🧪 Verificación

```bash
python -c "from digito_verificador import calcular_dv; print(calcular_dv(12345678))"
```

Casos de referencia: `12345678 → 5`, `11111111 → 1`, `22222222 → 2`, `9999999 → 3`.

## 📁 Estructura

```
digito_verificador.py   Algoritmo (calcular_dv) y programa de consola (main)
```

## 📄 Licencia

Uso libre.
