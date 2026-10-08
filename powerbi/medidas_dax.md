# Medidas DAX sugeridas

Estas medidas están pensadas para que el dashboard no se limite a mostrar totales, sino que permita analizar eficiencia, pérdidas, mantenimiento, logística e inventario.

```DAX
Unidades Totales = SUM(Produccion[unidades_totales])

Unidades Buenas = SUM(Produccion[unidades_buenas])

Scrap Unidades = SUM(Produccion[scrap_unidades])

Scrap % = DIVIDE([Scrap Unidades], [Unidades Totales])

Tiempo Programado Min = SUM(Produccion[min_programados])

Paro Planeado Min = SUM(Produccion[paro_planeado_min])

Paro No Planeado Min = SUM(Produccion[paro_no_planeado_min])

Tiempo Operación Min = SUM(Produccion[tiempo_operacion_min])

Tiempo Planificado Producción =
    [Tiempo Programado Min] - [Paro Planeado Min]

Disponibilidad =
    DIVIDE([Tiempo Operación Min], [Tiempo Planificado Producción])

Capacidad Ideal =
    SUMX(
        Produccion,
        Produccion[tiempo_operacion_min] * Produccion[velocidad_ideal_u_min]
    )

Rendimiento = DIVIDE([Unidades Totales], [Capacidad Ideal])

Calidad = DIVIDE([Unidades Buenas], [Unidades Totales])

OEE = [Disponibilidad] * [Rendimiento] * [Calidad]

Cumplimiento Producción =
    DIVIDE(
        [Unidades Totales],
        SUM(Produccion[objetivo_unidades])
    )

Entregas Totales = COUNTROWS(Logistica)

Entregas A Tiempo =
    CALCULATE(
        COUNTROWS(Logistica),
        Logistica[a_tiempo] = TRUE()
    )

Entregas Completas =
    CALCULATE(
        COUNTROWS(Logistica),
        FILTER(
            Logistica,
            Logistica[cantidad_recibida] >= Logistica[cantidad_ordenada]
        )
    )

Entregas OTIF =
    CALCULATE(
        COUNTROWS(Logistica),
        FILTER(
            Logistica,
            Logistica[a_tiempo] = TRUE()
                && Logistica[cantidad_recibida] >= Logistica[cantidad_ordenada]
        )
    )

OTIF % = DIVIDE([Entregas OTIF], [Entregas Totales])

Fill Rate % =
    DIVIDE(
        SUM(Logistica[cantidad_recibida]),
        SUM(Logistica[cantidad_ordenada])
    )

Tiempo Descarga Promedio = AVERAGE(Logistica[tiempo_descarga_min])

Costo Mantenimiento = SUM(Mantenimiento[costo_mxn])

Ordenes Correctivas =
    CALCULATE(
        COUNTROWS(Mantenimiento),
        Mantenimiento[tipo] = "Correctivo"
    )

Ordenes Preventivas =
    CALCULATE(
        COUNTROWS(Mantenimiento),
        Mantenimiento[tipo] = "Preventivo"
    )

Cumplimiento Preventivo =
    DIVIDE(
        CALCULATE(
            COUNTROWS(Mantenimiento),
            Mantenimiento[tipo] = "Preventivo",
            Mantenimiento[estatus] = "Cerrada"
        ),
        [Ordenes Preventivas]
    )

MTTR Min =
    AVERAGEX(
        FILTER(Mantenimiento, Mantenimiento[tipo] = "Correctivo"),
        Mantenimiento[duracion_min]
    )

MTBF Horas Aproximado =
    DIVIDE(
        [Tiempo Operación Min] / 60,
        [Ordenes Correctivas]
    )

Consumo Energía kWh = SUM(Energia[kwh])

Costo Energía = SUM(Energia[costo_mxn])

kWh por 1000 Unidades =
    DIVIDE(
        [Consumo Energía kWh] * 1000,
        [Unidades Totales]
    )

Costo Energía por 1000 Unidades =
    DIVIDE(
        [Costo Energía] * 1000,
        [Unidades Totales]
    )

Materiales Bajo Reorden =
    CALCULATE(
        DISTINCTCOUNT(Inventario[material_id]),
        Inventario[bajo_reorden] = TRUE()
    )

Defectos Afectados = SUM(Calidad[cantidad_afectada])

Eventos Calidad Abiertos =
    CALCULATE(
        COUNTROWS(Calidad),
        Calidad[estatus] <> "Cerrada"
    )
```

## Metas sugeridas para la demo

Las metas deben manejarse como parámetros, no como valores fijos en las medidas.

- OEE: 85 % como referencia configurable.
- OTIF: 95 % como referencia configurable.
- Scrap: objetivo configurable por línea o producto.
- Cumplimiento de producción: 100 %.
- Cumplimiento preventivo: 95 %.

## Notas

- `OTIF` se calcula como **On Time AND In Full**. No basta con que una entrega llegue a tiempo; también debe recibirse completa.
- `MTBF Horas Aproximado` se usa como indicador didáctico de portafolio a partir de horas de operación y órdenes correctivas. En una planta real convendría calcularlo con marcas de tiempo de falla y recuperación provenientes del CMMS/MES.
- Para análisis de pérdidas, el dashboard debe permitir bajar desde OEE hasta línea, turno y causa de paro.
