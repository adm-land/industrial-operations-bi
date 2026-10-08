-- Modelo simplificado para una solución de analítica industrial.
CREATE TABLE dim_linea (
    linea_id VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE dim_producto (
    producto_id VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL
);

CREATE TABLE fact_produccion (
    id INTEGER PRIMARY KEY,
    fecha DATE NOT NULL,
    linea_id VARCHAR(10) NOT NULL,
    turno VARCHAR(30) NOT NULL,
    producto_id VARCHAR(20) NOT NULL,
    min_programados INTEGER NOT NULL,
    paro_planeado_min INTEGER NOT NULL,
    paro_no_planeado_min INTEGER NOT NULL,
    tiempo_operacion_min INTEGER NOT NULL,
    velocidad_ideal_u_min DECIMAL(10,2) NOT NULL,
    objetivo_unidades INTEGER NOT NULL,
    unidades_totales INTEGER NOT NULL,
    unidades_buenas INTEGER NOT NULL,
    scrap_unidades INTEGER NOT NULL
);

CREATE TABLE fact_paros (
    id INTEGER PRIMARY KEY,
    fecha DATE NOT NULL,
    linea_id VARCHAR(10) NOT NULL,
    turno VARCHAR(30) NOT NULL,
    codigo_causa VARCHAR(20),
    causa VARCHAR(120),
    area_responsable VARCHAR(80),
    duracion_min INTEGER NOT NULL,
    estatus VARCHAR(30),
    accion VARCHAR(200)
);

CREATE TABLE fact_mantenimiento (
    id INTEGER PRIMARY KEY,
    fecha DATE NOT NULL,
    linea_id VARCHAR(10) NOT NULL,
    tipo VARCHAR(40) NOT NULL,
    descripcion VARCHAR(200),
    planeado BOOLEAN NOT NULL,
    duracion_min INTEGER NOT NULL,
    estatus VARCHAR(30),
    tecnico VARCHAR(100),
    costo_mxn DECIMAL(12,2)
);
