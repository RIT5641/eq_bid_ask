# Microstructure Project: Copeland & Galai Model

## Contexto

Basado en los hallazgos de Bagehot, Copeland & Galai, y Richard Roll, este modelo explica cómo puede existir un spread bid-ask incluso sin costos de transacción asumiendo la asimetría de información.

---

## Proyecto
El objetivo principal de este proyecto es el de tomar una acción listada en la base de datos de yfinance y obtener tanto el spread como el valor del bid y el ask del activo, usando una distribución dada (normal y exponencial).

## Teoría

### Supuestos:
- El valor fundamental del activo es una variable aleatoria (normal o exponencial).
- El market maker no sabe si el trader es informado o no.
- Con probabilidad $( \phi $), el trader está informado.
- El market maker ajusta el spread para que su ganancia esperada sea cero.

### Fórmula de ganancia esperada:
$[
\Pi(a, b) = \frac{1}{2} \left[ (1 - \phi)(a - \mathbb{E}[V]) + \phi(a - \mathbb{E}[V \mid V > a]) + (1 - \phi)(\mathbb{E}[V] - b) + \phi(\mathbb{E}[V \mid V < b] - b) \right]
$]

---

## Cómo ejecutar

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate en Windows
```

2. Instalar requerimientos:
```bash
pip install -r requirements.txt
```

3. Ejecutar:
```bash
python main.py
```

4. Abrir `report.ipynb` para ver las visualizaciones y comparaciones.

---
