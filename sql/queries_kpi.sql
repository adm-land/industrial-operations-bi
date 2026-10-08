-- KPIs de ejemplo

-- Scrap por línea
SELECT
    linea_id,
    SUM(scrap_unidades) * 1.0 / NULLIF(SUM(unidades_totales), 0) AS scrap_pct
FROM fact_produccion
GROUP BY linea_id;

-- Horas de paro no planeado por línea
SELECT
    linea_id,
    SUM(paro_no_planeado_min) / 60.0 AS horas_paro
FROM fact_produccion
GROUP BY linea_id;

-- Cumplimiento de producción
SELECT
    fecha,
    SUM(unidades_totales) * 1.0 / NULLIF(SUM(objetivo_unidades), 0) AS cumplimiento
FROM fact_produccion
GROUP BY fecha
ORDER BY fecha;
