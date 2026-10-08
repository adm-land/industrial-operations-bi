# Industrial Operations Intelligence

Proyecto de portafolio orientado a empresas de manufactura y logística de la zona de Toluca.

La idea es simular un entorno real de planta donde la información llega desde archivos de Excel/CSV y sistemas empresariales, se limpia y modela, y después se convierte en indicadores para operación, mantenimiento, calidad y cadena de suministro.

El proyecto está pensado para demostrar habilidades que aparecen con frecuencia en vacantes de Toluca: Power BI, Power Query, Excel, SQL, Python, Power Apps, Power Automate, mejora continua y análisis de KPIs.

> Los datos son sintéticos. Los archivos que simulan exportaciones de SAP/MES/SCADA no provienen de sistemas reales.

## Qué incluye

- Dataset industrial sintético de 3 meses.
- Producción, paros, mantenimiento, calidad, logística, inventario y energía.
- Generador de datos reproducible en Python.
- Modelo estrella propuesto para Power BI.
- Medidas DAX para OEE, MTTR, OTIF, scrap y cumplimiento de producción.
- Transformaciones sugeridas en Power Query.
- Script de ETL en Python.
- Esquema SQL y consultas de análisis.
- Diseño de una Power App para captura de paros y acciones.
- Flujos de Power Automate para alertas y reportes.
- Caso de mejora continua con 5 porqués y plan de acciones.
- Pruebas automáticas y GitHub Actions.

## Dashboard propuesto en Power BI

1. **Resumen ejecutivo** — OEE, producción, scrap, OTIF, costo de mantenimiento y alertas.
2. **Producción y calidad** — cumplimiento, rendimiento, defectos y scrap.
3. **Mantenimiento** — MTTR, paros, costos y preventivos.
4. **Logística e inventario** — OTIF, proveedores, tiempos de descarga y materiales bajo punto de reorden.
5. **Energía y mejora continua** — consumo, costo por línea y acciones de mejora.

## Tecnologías

- Power BI
- Power Query
- DAX
- Excel
- SQL
- Python
- Power Apps
- Power Automate
- Git / GitHub

## Generar los datos

```bash
python src/generate_demo_data.py
python src/etl.py
```

## Ejecutar validaciones

```bash
python -m unittest discover -s tests
```

## Power Platform

La Power App propuesta sirve para registrar un paro o desviación desde piso. Power Automate recibe el registro, genera una alerta cuando el evento rebasa un umbral y deja trazabilidad para que el dashboard pueda actualizarse después.

## Nota sobre Power BI

El repositorio contiene el modelo, las medidas DAX, las transformaciones Power Query y los datos necesarios para construir el dashboard. El archivo `.pbix` se agregará cuando la versión final se construya y valide en Power BI Desktop.

## Autor

**Alan Daniel Martínez Martínez**  
Estudiante de Ingeniería en Sistemas Computacionales — UNITEC
