"""main.py

Loads tributes.json, randomly assigns one tribute to the player, and
displays that tribute's stats in the terminal using the `rich` library.

Usage:
    python main.py
"""

import json
import random
import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

TRIBUTES_FILE = "data\\tributes.json"

def load_tributes(path: str = TRIBUTES_FILE) -> list[dict]:
    '''Load tributes from a JSON file.'''
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        sys.exit(
            f"Could not find {path}. Run tribute_factory.py first to generate it."
        )


def build_tribute_panel(tribute: dict) -> Panel:
    '''Build a rich Panel for a tribute.'''
    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column("Field", style="bold cyan", justify="right")
    table.add_column("Value", style="white")

    for field, value in tribute.items():
        if field in ["weapon", "position", "alive", "id", "name"]:
            continue
        label = field.replace("_", " ").title()
        table.add_row(label, str(value))

    name = tribute.get("name", "Unknown Tribute")
    return Panel(
        table,
        title=f"[bold yellow]{name}[/bold yellow]",
        border_style="red",
        expand=True,
    )

def display_tributes(tributes: list[dict], console: Console, per_row: int = 4) -> None:
    '''Display tributes in a grid layout using rich.'''
    panels = [build_tribute_panel(t) for t in sorted(tributes, key=lambda t: t["id"])]

    grid = Table.grid(expand=True, padding=(0, 1))
    for _ in range(per_row):
        grid.add_column(ratio=1)

    for i in range(0, len(panels), per_row):
        row = panels[i : i + per_row]
        row += [""] * (per_row - len(row))  # pad the last row so columns stay aligned
        grid.add_row(*row)

    console.print(grid)

def main() -> None:
    console = Console()
    tributes = load_tributes()

    if not tributes:
        sys.exit("tributes.json is empty — nothing to assign.")

    player_tribute = random.choice(tributes)

    console.print()
    console.rule("[bold red]THE REAPING[/bold red]")
    console.print()

    display_tributes(tributes, console)

    console.print()
    console.print(
        f"[bold]You are [yellow]{player_tribute.get('name', 'Unknown Tribute')}[/yellow], from [yellow]District {player_tribute.get('district', 'unkown')}[/yellow][/bold]"
    )
    console.print()


if __name__ == "__main__":
    main()