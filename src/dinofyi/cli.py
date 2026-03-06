"""Command-line interface for dinofyi."""

from __future__ import annotations

import json

import typer

from dinofyi.api import DinoFYI

app = typer.Typer(help="DinoFYI — Dinosaur paleontology encyclopedia API client.")


@app.command()
def search(query: str) -> None:
    """Search dinofyi.com."""
    with DinoFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))
