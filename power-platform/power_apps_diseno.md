# Diseño de Power App

## Objetivo
Capturar desde piso de planta un paro, desviación o acción de mantenimiento sin depender de una hoja de Excel manual.

## Pantallas
1. Inicio: línea, turno y usuario.
2. Nuevo evento: tipo de evento, causa, hora inicio, descripción, severidad.
3. Acción correctiva: responsable, fecha compromiso y evidencia.
4. Consulta: eventos abiertos por línea.
5. Cierre: causa raíz, acción final y validación.

## Fuente de datos
Para una demo:
- Lista de SharePoint.

Para una implementación empresarial:
- Dataverse.

## Campos mínimos
- Fecha/hora
- Línea
- Turno
- Equipo
- Tipo de evento
- Causa
- Duración
- Descripción
- Responsable
- Estado
- Severidad
- Acción correctiva

## Reglas
- No cerrar un evento sin causa raíz.
- Si la severidad es Alta, solicitar responsable y fecha compromiso.
- Si la duración supera 20 minutos, generar alerta automática.
