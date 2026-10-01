# may-the-odds
A Python text-based Hunger Games simulator

## Project structure

```
data/                      Editable game content 
  tributes.json
scripts/     
  build.py                 creates the exe
src/
  engine/                  Game loop, phases, event selection
    game.py
    phases.py
  factories/               Build model objects from the JSON data
    tribute_factory.py
  models/       
    tribute.py
  main.py                  Entry point
tests/                     Mirrors src/ layout

```

## Running

    uv run src/main.py

## Building the exe

    uv run scripts/build.py

## running individual files

    uv run python -m src.factories.tribute_factory