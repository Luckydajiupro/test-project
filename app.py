"""Minimal route table.

The orchestrator's first instruction against this repo adds a health route;
everything here exists so that instruction has somewhere to land.
"""

from __future__ import annotations

from typing import Callable, Dict, List, Optional

ROUTES: Dict[str, Callable[[], object]] = {}


def route(path: str, handler: Callable[[], object]) -> None:
    ROUTES[path] = handler


def dispatch(path: str) -> Optional[object]:
    handler = ROUTES.get(path)
    return handler() if handler is not None else None


def paths() -> List[str]:
    return sorted(ROUTES)
