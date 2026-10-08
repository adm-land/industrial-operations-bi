import csv
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
random.seed(42)

start = date(2026, 7, 1)
days = 92
lines = [('L1', 'Envasado A', 480), ('L2', 'Envasado B', 450), ('L3', 'Empaque', 520), ('L4', 'Etiquetado', 600)]
products = [('P001', 'Producto Alfa', 0.96), ('P002', 'Producto Beta', 0.94), ('P003', 'Producto Gamma', 0.95)]
shifts = ['Matutino', 'Vespertino']


def write_csv(name, headers, rows):
    with open(RAW / name, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


production = []
record_id = 1
for d in range(days):
    dt = start + timedelta(days=d)
    active_lines = lines[:2] if dt.weekday() == 6 else lines
    for line_id, line_name, nominal_rate in active_lines:
        for shift in shifts:
            product_id, product_name, base_quality = random.choice(products)
            scheduled = 480
            planned_stop = random.randint(15, 35)
            unplanned_stop = max(0, int(random.gauss(28, 22)))
            run_time = max(300, scheduled - planned_stop - unplanned_stop)
            ideal_rate = nominal_rate / 60.0
            performance = min(1.05, max(0.72, random.gauss(0.91, 0.045)))
            total_units = int(run_time * ideal_rate * performance)
            quality = min(0.995, max(0.90, random.gauss(base_quality, 0.012)))
            good_units = int(total_units * quality)
            scrap = total_units - good_units
            target = int((scheduled - planned_stop) * ideal_rate * 0.90)
            production.append([record_id, dt.isoformat(), line_id, line_name, shift, product_id, product_name, scheduled, planned_stop, unplanned_stop, run_time, round(ideal_rate, 2), target, total_units, good_units, scrap])
            record_id += 1

write_csv('produccion.csv', ['id','fecha','linea_id','linea','turno','producto_id','producto','min_programados','paro_planeado_min','paro_no_planeado_min','tiempo_operacion_min','velocidad_ideal_u_min','objetivo_unidades','unidades_totales','unidades_buenas','scrap_unidades'], production)

reasons = [('MEC','Falla mecánica','Mantenimiento'), ('ELE','Falla eléctrica','Mantenimiento'), ('MAT','Falta de material','Logística'), ('CAM','Cambio de formato','Producción'), ('CAL','Ajuste de calidad','Calidad')]
paros = []
pid = 1
for row in production:
    unplanned = row[9]
    if unplanned <= 0:
        continue
    code, cause, area = random.choice(reasons)
    paros.append([pid, row[1], row[2], row[3], row[4], code, cause, area, unplanned, random.choice(['Cerrada','Cerrada','Abierta']), random.choice(['Ajuste y prueba','Cambio de componente','Reinicio controlado','Abastecimiento'])])
    pid += 1
write_csv('paros.csv', ['id','fecha','linea_id','linea','turno','codigo_causa','causa','area_responsable','duracion_min','estatus','accion'], paros)

maintenance = []
mid = 1
for d in range(0, days, 2):
    dt = start + timedelta(days=d)
    for line_id, line_name, _ in random.sample(lines, k=random.choice([1,1,2])):
        mtype = random.choice(['Preventivo','Correctivo','Predictivo'])
        maintenance.append([mid, dt.isoformat(), line_id, line_name, mtype, random.choice(['Inspección general','Lubricación','Cambio de rodamiento','Revisión eléctrica','Alineación y ajuste']), mtype != 'Correctivo', random.randint(25, 240), random.choice(['Cerrada','Cerrada','En proceso']), random.choice(['Tec. A','Tec. B','Tec. C']), round(random.uniform(150, 4500), 2)])
        mid += 1
write_csv('mantenimiento.csv', ['id','fecha','linea_id','linea','tipo','descripcion','planeado','duracion_min','estatus','tecnico','costo_mxn'], maintenance)

suppliers = [('S001','Proveedor Norte'),('S002','Proveedor Centro'),('S003','Proveedor Bajío'),('S004','Proveedor Valle')]
logistics = []
lid = 1
for d in range(days):
    dt = start + timedelta(days=d)
    if dt.weekday() >= 6:
        continue
    for _ in range(random.randint(2,5)):
        sid, sname = random.choice(suppliers)
        ordered = random.randint(100,1200)
        received = int(ordered * min(1, max(0.72, random.gauss(0.96,0.06))))
        on_time = random.random() < 0.91
        delay = 0 if on_time else random.randint(1,5)
        logistics.append([lid, f'PO-{10000+lid}', sid, sname, dt.isoformat(), (dt+timedelta(days=delay)).isoformat(), ordered, received, on_time, random.choice(['Materia prima','Empaque','Refacción','Consumible']), random.randint(20,120)])
        lid += 1
write_csv('logistica.csv', ['id','orden_compra','proveedor_id','proveedor','fecha_promesa','fecha_real','cantidad_ordenada','cantidad_recibida','a_tiempo','categoria','tiempo_descarga_min'], logistics)

quality = []
qid = 1
for d in range(days):
    dt = start + timedelta(days=d)
    for _ in range(random.randint(0,2)):
        line_id, line_name, _ = random.choice(lines)
        quality.append([qid, dt.isoformat(), line_id, line_name, random.choice(['Sellado','Etiqueta','Dimensión','Color','Contaminación visual']), random.choice(['Baja','Media','Media','Alta']), random.randint(5,180), random.choice(['Ajuste de parámetros','Reentrenamiento','Cambio de lote','Inspección adicional']), random.choice(['Cerrada','Cerrada','En seguimiento'])])
        qid += 1
write_csv('calidad.csv', ['id','fecha','linea_id','linea','defecto','severidad','cantidad_afectada','accion','estatus'], quality)

materials = [('MAT001','Resina A',1500,300),('MAT002','Cartón',2200,450),('MAT003','Etiqueta',3500,700),('MAT004','Adhesivo',850,200),('MAT005','Refacción crítica',20,5)]
inventory = []
iid = 1
for d in range(0, days, 3):
    dt = start + timedelta(days=d)
    for code, name, base_qty, reorder in materials:
        qty = max(0, int(random.gauss(base_qty, base_qty*0.18)))
        inventory.append([iid, dt.isoformat(), code, name, qty, reorder, qty < reorder, random.choice(['Almacén MP','Almacén MRO'])])
        iid += 1
write_csv('inventario.csv', ['id','fecha','material_id','material','existencia','punto_reorden','bajo_reorden','ubicacion'], inventory)

energy = []
eid = 1
for d in range(days):
    dt = start + timedelta(days=d)
    for line_id, line_name, _ in lines:
        kwh = round(max(250, random.gauss(620,85)),2)
        energy.append([eid, dt.isoformat(), line_id, line_name, kwh, round(kwh*random.uniform(2.05,2.45),2)])
        eid += 1
write_csv('energia.csv', ['id','fecha','linea_id','linea','kwh','costo_mxn'], energy)

print(f'Datos generados en {RAW}')
