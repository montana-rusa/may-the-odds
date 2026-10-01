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
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(
            f"Could not find {path}. Run tribute_factory.py first to generate it."
        )


def display_player_tribute(tribute: dict, console: Console) -> None:
    table = Table(show_header=False, box=None, pad_edge=False)
    table.add_column("Field", style="bold cyan", justify="right")
    table.add_column("Value", style="white")

    for field, value in tribute.items():
        if field == "name":
            continue
        label = field.replace("_", " ").title()
        table.add_row(label, str(value))

    name = tribute.get("name", "Unknown Tribute")
    console.print(
        Panel(
            table,
            title=f"[bold yellow]{name}[/bold yellow]",
            subtitle="[italic]Your Tribute[/italic]",
            border_style="red",
            expand=False,
        )
    )


def main() -> None:
    console = Console()
    tributes = load_tributes()

    if not tributes:
        sys.exit("tributes.json is empty — nothing to assign.")

    player_tribute = random.choice(tributes)

    console.print()
    console.rule("[bold red]THE REAPING[/bold red]")
    console.print()
    display_player_tribute(player_tribute, console)
    console.print()


if __name__ == "__main__":
    main()