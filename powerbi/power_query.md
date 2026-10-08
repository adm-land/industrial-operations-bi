# Power Query

Ejemplo de limpieza para `produccion.csv`:

```powerquery
let
    Origen = Csv.Document(
        File.Contents("data/raw/produccion.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    Encabezados = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    Tipos = Table.TransformColumnTypes(
        Encabezados,
        {
            {"id", Int64.Type},
            {"fecha", type date},
            {"linea_id", type text},
            {"linea", type text},
            {"turno", type text},
            {"producto_id", type text},
            {"producto", type text},
            {"min_programados", Int64.Type},
            {"paro_planeado_min", Int64.Type},
            {"paro_no_planeado_min", Int64.Type},
            {"tiempo_operacion_min", Int64.Type},
            {"velocidad_ideal_u_min", type number},
            {"objetivo_unidades", Int64.Type},
            {"unidades_totales", Int64.Type},
            {"unidades_buenas", Int64.Type},
            {"scrap_unidades", Int64.Type}
        }
    ),
    SinDuplicados = Table.Distinct(Tipos, {"id"}),
    LineaLimpia = Table.TransformColumns(SinDuplicados, {{"linea", Text.Trim, type text}})
in
    LineaLimpia
```

En Power BI conviene transformar cada archivo como una consulta separada y después construir relaciones por fecha, línea, producto, proveedor y material.
