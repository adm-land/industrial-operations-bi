# Modelo de datos propuesto

Modelo estrella:

- `DimFecha`
- `DimLinea`
- `DimProducto`
- `DimProveedor`
- `DimMaterial`
- `Produccion`
- `Paros`
- `Mantenimiento`
- `Calidad`
- `Logistica`
- `Inventario`
- `Energia`

Relaciones principales:

- `DimFecha[Fecha]` 1:* a todas las tablas de hechos.
- `DimLinea[LineaId]` 1:* a Produccion, Paros, Mantenimiento, Calidad y Energia.
- `DimProducto[ProductoId]` 1:* a Produccion.
- `DimProveedor[ProveedorId]` 1:* a Logistica.
- `DimMaterial[MaterialId]` 1:* a Inventario.

Evitar relaciones muchos-a-muchos salvo que sean realmente necesarias.
