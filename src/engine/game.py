from rich.console import Console

from models.arena import Arena

console = Console()

class Game:

    def __init__(self) -> None:
        arena = Arena()

    def start_game(self) -> None:
         
        console.print()
        console.rule("[bold red]THE BLOODBATH[/bold red]")
        console.print()

