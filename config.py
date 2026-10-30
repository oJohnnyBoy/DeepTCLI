import json
import os
from pathlib import Path

from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Stored next to this script, so it works no matter where you run it from
FILE = Path(__file__).parent / 'keys.json'

# Menu number -> service name. Add more APIs here later.
SERVICES = {'1': 'deepl'}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    console.input('\n[dim]Press Enter to continue...[/dim]')


# ---------- storage ----------

def load_keys() -> dict:
    try:
        return json.loads(FILE.read_text(encoding='utf-8'))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        console.print('[red]keys.json is corrupted, starting with an empty list.[/red]')
        return {}


def save_keys(keys: dict) -> None:
    FILE.write_text(json.dumps(keys, indent=2), encoding='utf-8')
    try:
        os.chmod(FILE, 0o600)  # owner-only on Linux/macOS (limited effect on Windows)
    except OSError:
        pass


def get_key(service: str) -> str | None:
    """Used by main.py to fetch a saved key."""
    return load_keys().get(service)


def mask(key: str) -> str:
    if len(key) <= 8:
        return '*' * len(key)
    return key[:4] + '*' * (len(key) - 8) + key[-4:]


# ---------- actions ----------

def pick_service(title: str, subtitle: str) -> str | None:
    options = '\n'.join(f'{n}. {name}' for n, name in SERVICES.items())
    console.print(Panel(f'Which API?\n{options}', title='[bold red]API Manager', subtitle=subtitle))
    return SERVICES.get(console.input('> ').strip())


def handle_import():
    service = pick_service('Import', 'Import Key')
    if not service:
        console.print('[red]Invalid option.[/red]')
        return pause()

    keys = load_keys()
    if service in keys:
        overwrite = console.input(f'[yellow]A {service} key already exists. Overwrite? (y/n)[/yellow] ')
        if overwrite.strip().lower() != 'y':
            return

    # is_password=True hides what you type/paste
    key = prompt(f'Paste your {service} API key: ', is_password=True).strip()
    if not key:
        console.print('[red]Empty key, nothing saved.[/red]')
        return pause()

    keys[service] = key
    save_keys(keys)
    console.print(f'[green]{service} key saved ({mask(key)}).[/green]')
    pause()


def list_keys():
    keys = load_keys()
    if not keys:
        console.print('[yellow]No keys registered yet.[/yellow]')
        return pause()

    table = Table(title='Registered keys')
    table.add_column('Service', style='bold red')
    table.add_column('Key')
    for service, key in keys.items():
        table.add_row(service, mask(key))
    console.print(table)
    pause()


def handle_delete():
    keys = load_keys()
    if not keys:
        console.print('[yellow]No keys to delete.[/yellow]')
        return pause()

    service = pick_service('Delete', 'Delete Key')
    if service not in keys:
        console.print('[red]No key saved for that service.[/red]')
        return pause()

    confirm = console.input(f'[yellow]Delete the {service} key? (y/n)[/yellow] ')
    if confirm.strip().lower() == 'y':
        del keys[service]
        save_keys(keys)
        console.print(f'[green]{service} key deleted.[/green]')
    pause()


# ---------- menu ----------

def options():
    while True:
        clear()
        console.print(Panel(
            '[italic green]What would you want to do?[/italic green]'
            '\n1. Import a key.'
            '\n2. Delete a key.'
            '\n3. Show your registered keys.'
            '\n4. Back.',
            title='[bold red]API Manager'))
        choice = console.input('> ').strip()
        clear()

        match choice:
            case '1':
                handle_import()
            case '2':
                handle_delete()
            case '3':
                list_keys()
            case '4':
                return