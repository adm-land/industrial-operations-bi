# Medidas DAX sugeridas

```DAX
Unidades Totales = SUM(Produccion[unidades_totales])

Unidades Buenas = SUM(Produccion[unidades_buenas])

Scrap Unidades = SUM(Produccion[scrap_unidades])

Scrap % = DIVIDE([Scrap Unidades], [Unidades Totales])

Tiempo Programado Min = SUM(Produccion[min_programados])

Paro Planeado Min = SUM(Produccion[paro_planeado_min])

Paro No Planeado Min = SUM(Produccion[paro_no_planeado_min])

Tiempo Operación Min = SUM(Produccion[tiempo_operacion_min])

Tiempo Planificado Producción = [Tiempo Programado Min] - [Paro Planeado Min]

Disponibilidad = DIVIDE([Tiempo Operación Min], [Tiempo Planificado Producción])

Capacidad Ideal = SUMX(Produccion, Produccion[tiempo_operacion_min] * Produccion[velocidad_ideal_u_min])

Rendimiento = DIVIDE([Unidades Totales], [Capacidad Ideal])

Calidad = DIVIDE([Unidades Buenas], [Unidades Totales])

OEE = [Disponibilidad] * [Rendimiento] * [Calidad]

Cumplimiento Producción = DIVIDE([Unidades Totales], SUM(Produccion[objetivo_unidades]))

OTIF % = DIVIDE(CALCULATE(COUNTROWS(Logistica), Logistica[a_tiempo] = TRUE()), COUNTROWS(Logistica))

Tiempo Descarga Promedio = AVERAGE(Logistica[tiempo_descarga_min])

Costo Mantenimiento = SUM(Mantenimiento[costo_mxn])

Cumplimiento Preventivo =
    DIVIDE(
        CALCULATE(COUNTROWS(Mantenimiento), Mantenimiento[tipo] = "Preventivo", Mantenimiento[estatus] = "Cerrada"),
        CALCULATE(COUNTROWS(Mantenimiento), Mantenimiento[tipo] = "Preventivo")
    )

MTTR Min = AVERAGEX(FILTER(Mantenimiento, Mantenimiento[tipo] = "Correctivo"), Mantenimiento[duracion_min])

Consumo Energía kWh = SUM(Energia[kwh])

Costo Energía = SUM(Energia[costo_mxn])
```

## Objetivos visuales

- OEE: meta configurable, por ejemplo 85%.
- OTIF: meta configurable, por ejemplo 95%.
- Scrap: mostrar tendencia y Pareto de defectos.
- Paros: Pareto por causa y área responsable.
- Mantenimiento: correctivo vs preventivo, costo, MTTR y cumplimiento.
