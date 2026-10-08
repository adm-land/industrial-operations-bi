import csv
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)


def read_csv(name):
    with open(RAW / name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def build_daily_kpis():
    production = read_csv("produccion.csv")
    by_date = defaultdict(lambda: {
        "target": 0, "total": 0, "good": 0, "scrap": 0,
        "scheduled": 0, "planned_stop": 0, "unplanned_stop": 0,
        "run": 0, "ideal_capacity": 0
    })

    for row in production:
        item = by_date[row["fecha"]]
        item["target"] += safe_float(row["objetivo_unidades"])
        item["total"] += safe_float(row["unidades_totales"])
        item["good"] += safe_float(row["unidades_buenas"])
        item["scrap"] += safe_float(row["scrap_unidades"])
        item["scheduled"] += safe_float(row["min_programados"])
        item["planned_stop"] += safe_float(row["paro_planeado_min"])
        item["unplanned_stop"] += safe_float(row["paro_no_planeado_min"])
        item["run"] += safe_float(row["tiempo_operacion_min"])
        item["ideal_capacity"] += safe_float(row["tiempo_operacion_min"]) * safe_float(row["velocidad_ideal_u_min"])

    output = []
    for fecha, x in sorted(by_date.items()):
        planned_time = max(1, x["scheduled"] - x["planned_stop"])
        availability = x["run"] / planned_time
        performance = x["total"] / max(1, x["ideal_capacity"])
        quality = x["good"] / max(1, x["total"])
        oee = availability * performance * quality
        output.append({
            "fecha": fecha,
            "cumplimiento_produccion": round(x["total"] / max(1, x["target"]), 4),
            "scrap_pct": round(x["scrap"] / max(1, x["total"]), 4),
            "disponibilidad": round(availability, 4),
            "rendimiento": round(performance, 4),
            "calidad": round(quality, 4),
            "oee": round(oee, 4),
            "paro_no_planeado_h": round(x["unplanned_stop"] / 60, 2),
        })

    path = OUT / "kpi_diario.csv"
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)
    return path


if __name__ == "__main__":
    print(build_daily_kpis())
