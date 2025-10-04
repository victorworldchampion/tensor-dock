"""
Command-line interface for Image Processing.
"""
from __future__ import annotations
import argparse
from typing import Any
from .algorithm import core_algorithm, pretty_print, validate_input
from .utils import load_json, timer

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Image Processing CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    runp = sub.add_parser("run", help="run the core algorithm")
    runp.add_argument("--example", type=str, default="examples/sample.json")
    runp.add_argument("--seed", type=int, default=42)

    args = p.parse_args(argv)

    if args.cmd == "run":
        data: Any = load_json(args.example)
        validate_input(data)
        with timer("core_algorithm"):
            res = core_algorithm(data, seed=args.seed)
        print(pretty_print(res))
        return 0

    return 1

if __name__ == "__main__":
    raise SystemExit(main())
