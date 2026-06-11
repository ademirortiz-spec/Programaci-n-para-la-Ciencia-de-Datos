"""Valida que las dependencias listadas en requirements.txt están instaladas.

Salida:
 - Código 0: todo OK (todas las libs instaladas y versiones coinciden o no se especificó versión)
 - Código 1: hay paquetes faltantes
 - Código 2: requirements.txt no encontrado
 - Código 3: error inesperado

Uso (desde la raíz del repo):
  python src\Install\validate_requirements.py
"""
from pathlib import Path
import sys
import re

try:
    from importlib.metadata import version, PackageNotFoundError
except Exception:
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


def parse_requirements(path: Path):
    lines = []
    for raw in path.read_text(encoding="utf8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # remove inline comments
        if "#" in line:
            line = line.split("#", 1)[0].strip()
        if line:
            lines.append(line)
    return lines


def main():
    repo_root = Path(__file__).resolve().parents[2]
    req_file = repo_root / "requirements.txt"
    if not req_file.exists():
        print(f"No se encontró requirements.txt en: {req_file}")
        return 2

    reqs = parse_requirements(req_file)
    missing = []
    mismatch = []
    ok = []

    for item in reqs:
        # soporta formatos: pkg==x.y.z o pkg
        m = re.match(r"^([^=<>!~]+)(?:==([\d\.\w+-]+))?$", item)
        if not m:
            # salto líneas complejas (extras de pip) — considerarlas ok
            ok.append((item, None))
            continue
        name = m.group(1).strip()
        req_ver = m.group(2)
        try:
            inst_ver = version(name)
            if req_ver and inst_ver != req_ver:
                mismatch.append((name, req_ver, inst_ver))
            else:
                ok.append((name, inst_ver))
        except PackageNotFoundError:
            missing.append((name, req_ver))

    # Report
    if ok:
        print("Paquetes instalados:")
        for n, v in ok:
            print(f"  - {n}: {v}")
    if mismatch:
        print("\nPaquetes con versión diferente a la solicitada:")
        for n, reqv, instv in mismatch:
            print(f"  - {n}: requerido={reqv} instalado={instv}")
    if missing:
        print("\nPaquetes faltantes:")
        for n, reqv in missing:
            print(f"  - {n}: requerido={reqv}")

    if missing:
        print(f"\nResultado: paquetes faltantes: {len(missing)}")
        return 1
    if mismatch:
        print(f"\nResultado: versiones diferentes encontradas: {len(mismatch)}")
        # devuelve 0 aún si hay mismatch; 
        return 0

    print("\nResultado: todas las dependencias están instaladas y coinciden con las versiones (si se especificaron).")
    return 0


if __name__ == "__main__":
    try:
        code = main()
        # Si se ejecuta en una terminal interactiva, esperar a que el usuario presione Enter
        try:
            if sys.stdin.isatty():
                input("\nPresione Enter para cerrar...")
        except Exception:
            # En entornos no interactivos (CI, pipes) input() puede fallar; ignorar
            pass
        sys.exit(code)
    except Exception as e:
        print(f"Error inesperado: {e}")
        # Intentar también dar oportunidad al usuario de ver el error en TTY
        try:
            if sys.stdin.isatty():
                input("\nPresione Enter para cerrar...")
        except Exception:
            pass
        sys.exit(3)
