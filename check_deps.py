import sys

REQUIRED = ["keyboard"]

missing = []

for lib in REQUIRED:
    try:
        __import__(lib)
    except ImportError:
        missing.append(lib)

if missing:
    print("Отсутствуют зависимости:", ", ".join(missing))
    sys.exit(1)
else:
    print("Все зависимости установлены.")
    sys.exit(0)
