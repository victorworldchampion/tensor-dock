"""
Utilities shared across modules: timers, logging helpers, and data loaders.
"""
from __future__ import annotations
from typing import Any, Callable, Dict, Iterable, List
import json
import time
import contextlib

@contextlib.contextmanager
def timer(name: str):
    t0 = time.perf_counter()
    yield
    dt = time.perf_counter() - t0
    print(f"[TIMER] {name}: {dt:.4f}s")

def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def chunked(iterable: Iterable[Any], size: int) -> Iterable[List[Any]]:
    buf: List[Any] = []
    for x in iterable:
        buf.append(x)
        if len(buf) >= size:
            yield buf
            buf = []
    if buf:
        yield buf
