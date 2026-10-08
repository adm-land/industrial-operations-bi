# Arquitectura

```text
Excel / CSV / exportaciones simuladas de SAP-MES-SCADA
                    |
              Power Query
                    |
            Modelo de datos
            /             \
        Power BI        SQL/Python
           |                |
        KPIs           validación/ETL

Power App -> SharePoint/Dataverse -> Power Automate -> alertas y acciones
```

La demo no se conecta a un SAP, MES ni SCADA real. El objetivo es demostrar el flujo de datos y la lógica que se usaría para integrar exportaciones de esos sistemas.
