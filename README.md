# Microstructure Project: Copeland & Galai Model

## Contexto

Basado en los hallazgos de Bagehot, Copeland & Galai, y Richard Roll, este modelo explica cómo puede existir un spread bid-ask incluso sin costos de transacción asumiendo la asimetría de información.

---

## 📚 Teoría

### Supuestos principales:
- El valor fundamental del activo es una variable aleatoria (normal o exponencial).
- El market maker no sabe si el trader es informado o no.
- Con probabilidad \( \phi \), el trader está informado.
- El market maker ajusta el spread para que su ganancia esperada sea cero.

### Fórmula de ganancia esperada:
\[
\Pi(a, b) = \frac{1}{2} \left[ (1 - \phi)(a - \mathbb{E}[V]) + \phi(a - \mathbb{E}[V \mid V > a]) + (1 - \phi)(\mathbb{E}[V] - b) + \phi(\mathbb{E}[V \mid V < b] - b) \right]
\]

---

## ⚙️ Estructura del código

```bash
microstructure_project/
│
├── technical_analysis/
│   ├── __init__.py
│   ├── utils.py          # ConditionalExpectationCalculator
│   └── model.py          # MarketMakerModel
│
├── main.py               # Script de ejecución
├── report.ipynb          # Resultados y comparaciones
├── README.md             # Este archivo
├── requirements.txt      # Dependencias
└── .gitignore
```

---

## 📈 Cómo ejecutar

1. Crear entorno virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
```

2. Instalar requerimientos:
```bash
pip install -r requirements.txt
```

3. Ejecutar:
```bash
python main.py
```

4. Abrir `report.ipynb` para ver visualizaciones y comparaciones.

---

## 📖 Bibliografía
- Copeland, T.E. & Galai, D. (1983). "Information Effects on the Bid-Ask Spread". *The Journal of Finance.*
- Bagehot, W. (1971). "The Only Game in Town"
- Roll, R. (1984). "A Simple Implicit Measure of the Effective Bid-Ask Spread"