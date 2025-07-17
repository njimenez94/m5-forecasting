
# 📦 Descripción de los datasets M5 y comparación con Tricot

Este documento explica los principales datasets usados en la competencia **M5 Forecasting (Walmart)** y los compara con las columnas típicas de los sistemas de retail con venta intermitente, como los usados en Tricot (SKU–Talla–Sucursal–Semana).

---

## 🗃️ Archivos del Dataset M5

### 1. `sales_train_validation.csv`
Contiene las ventas históricas de cada producto (item_id) por tienda (store_id) en cada día `d_1` a `d_1941`.

| Columna | Descripción |
|---------|-------------|
| `id` | Identificador único del producto-tienda |
| `item_id` | Código del producto |
| `dept_id` | Departamento del producto |
| `cat_id` | Categoría del producto |
| `store_id` | Código de tienda |
| `state_id` | Estado (California, etc.) |
| `d_1` a `d_1941` | Unidades vendidas por día |

---

### 2. `calendar.csv`
Mapea cada `d_1`, `d_2`, ... con una fecha real, eventos y características del día.

| Columna | Descripción |
|---------|-------------|
| `date` | Fecha en formato `YYYY-MM-DD` |
| `wm_yr_wk` | Código semanal |
| `weekday` | Día de la semana |
| `wday` | Día numérico |
| `month`, `year` | Mes y año |
| `event_name_1/2` | Eventos (Navidad, Pascua, etc.) |
| `snap_CA/TX/WA` | Indicadores SNAP por estado |

---

### 3. `sell_prices.csv`
Indica el precio de venta de cada producto por tienda y semana.

| Columna | Descripción |
|---------|-------------|
| `store_id` | Tienda |
| `item_id` | Producto |
| `wm_yr_wk` | Semana |
| `sell_price` | Precio de venta |

---

### 4. `sales_train_evaluation.csv`
Igual que `sales_train_validation.csv` pero con más días: se usa para evaluación final.

---

### 5. `sample_submission.csv`
Archivo de ejemplo que muestra cómo debe formatearse la predicción final (`id`, `F1` a `F28` para 28 días futuros).

---

## 🔄 Comparación con tus datos en Tricot

| Concepto Tricot | M5 Dataset | Equivalencia |
|-----------------|------------|--------------|
| `cod_producto` | `item_id` | ✅ |
| `cod_sucursal` | `store_id` | ✅ |
| `cod_talla` | – | 🚫 (no incluye tallas) |
| `semana` | `wm_yr_wk`, `d_N` + `calendar.csv` | ✅ indirecto |
| `venta` | columnas `d_1` a `d_1941` | ✅ |
| `stock_sucursal` | – | 🚫 (no incluido) |
| `precio_venta` | `sell_price` | ✅ |
| `eventos` / promociones | `calendar.event_name`, `snap` | ✅ |

---

## 🌟 Diagrama Estrella (Modelo de Datos M5)

```plaintext
                     ┌────────────┐
                     │ calendar   │
                     └────┬───────┘
                          │ (d_*)
                ┌─────────▼──────────┐
                │ sales_train_*.csv │◄────────┐
                └─────────┬──────────┘         │
                          │ (item_id, store_id)│
                ┌─────────▼──────────┐         │
                │  sell_prices.csv   │◄────────┘
                └────────────────────┘
```

---

## 🧠 Comentario Final

La base M5 es ideal para experimentar con forecasting a nivel granular (producto–tienda), pero **no modela directamente la venta intermitente de SKU–talla**, que es clave en retail vestuario. Sin embargo, te sirve para:

- practicar la estructura estrella,
- integrar calendario y precio,
- y aplicar modelos ML o de series temporales con múltiples features.

Puedo ayudarte a transformar esta estructura para simular una con SKU–Talla–Sucursal y demanda intermitente si lo necesitas.

---

