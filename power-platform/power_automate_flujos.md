# Flujos de Power Automate

## 1. Alerta de paro crítico
**Disparador:** nuevo registro en SharePoint/Dataverse.  
**Condición:** duración >= 20 minutos o severidad = Alta.  
**Acciones:** enviar aviso por Teams/correo, crear tarea en Planner y registrar fecha de notificación.

## 2. Mantenimiento próximo
**Disparador:** recurrencia diaria.  
**Condición:** mantenimiento programado dentro de 7 días.  
**Acciones:** avisar al responsable y generar lista de pendientes.

## 3. Reporte semanal
**Disparador:** lunes 07:00.  
**Acciones:** consultar KPIs, generar resumen de OEE/OTIF/scrap/paros y enviarlo al equipo.

## 4. Proveedor fuera de objetivo
**Disparador:** actualización de entrega.  
**Condición:** OTIF del proveedor < 95%.  
**Acciones:** registrar desviación, notificar a compras y abrir acción de seguimiento.

## 5. Material crítico
**Disparador:** actualización de inventario.  
**Condición:** existencia < punto de reorden.  
**Acciones:** notificar a almacén/compras y registrar prioridad.
