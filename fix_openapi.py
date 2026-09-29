#!/usr/bin/env python3
"""Apply deterministic compatibility fixes to the Veeam ONE v2.3 OpenAPI document.

This follows the workaround used by Cenvora's Veeam BR client: schemas referenced
through allOf cannot themselves retain oneOf/discriminator constructs that
openapi-python-client cannot flatten.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def fix(data: dict) -> list[str]:
    schemas = data.get("components", {}).get("schemas", {})
    used: set[str] = set()

    def walk(value):
        if isinstance(value, dict):
            if "allOf" in value and isinstance(value["allOf"], list):
                for item in value["allOf"]:
                    if isinstance(item, dict):
                        ref = item.get("$ref")
                        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
                            used.add(ref.rsplit("/", 1)[-1])
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(schemas)
    fixed: list[str] = []
    for name in sorted(used):
        schema = schemas.get(name)
        if not isinstance(schema, dict):
            continue
        removed = [key for key in ("oneOf", "discriminator") if key in schema]
        for key in removed:
            del schema[key]
        if removed:
            fixed.append(name)
    return fixed


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python fix_openapi.py <input.json> <output.json>")
        return 2
    source, target = map(Path, sys.argv[1:])
    data = json.loads(source.read_text(encoding="utf-8"))
    fixed = fix(data)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {target}; fixed {len(fixed)} schema(s)")
    for name in fixed:
        print(f" - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
