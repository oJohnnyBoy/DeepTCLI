import deepl
import os
from rich import print
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter as WC
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from . import config



languages = ['PT-BR', 'EN-US', 'JA']

completer = WC(languages, ignore_case=True)

console = Console()

def get_client():
    """Build the DeepL client from the saved key (None if there isn't one)."""
    key = config.get_key('deepl')
    if not key:
        console.print(Panel('[red]No DeepL key found.[/red] Go to "Manage your API keys" and import one first.', title='[bold red]Translate'))
        console.input('\nPress Enter to continue...')
        return None
    return deepl.DeepLClient(key)


def translate():
    client = get_client()
    if client is None:
        return

    console.print(Panel('Select the language you want to translate to',title='[bold red]Translate', subtitle='Select Language'))
    #subtitle1 = 'Select Language'
    lang1 = prompt(
    "Language (PT-BR, EN-US, JA...): \n",
    completer=completer,
    ).strip().upper()
    clear()

    console.print(Panel(f'[red]You choose:[/red] {lang1}', title='[bold red]Translate'))
    txt = console.input('What do you want to translate? \n')
    clear()
    try:
        result = client.translate_text(txt, target_lang=lang1)
    except deepl.AuthorizationException:
        console.print('[red]DeepL rejected your key. Re-import it in "Manage your API keys".[/red]')
        return
    except deepl.DeepLException as e:
        console.print(f'[red]DeepL error:[/red] {e}')
        return
   
    console.print(Panel(f'Your text: [green]"{txt}"[/green] \nHas been sucessfully translated to: [bold red]{lang1}[/bold red]\nHere is your translation: \n{result.text}', title='[bold red]Translate'))

def import_api():
    #call config, it will handle everything about the API's
    config.options()
    return

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    console.print(Panel('[red]Select what do you want to do:[/red] \n1. Translate. \n2. Manage your API keys.', title='[bold red]Welcome to DeepTCLI'))
    c1 = console.input('> ')
    match c1:
        case '1':
            clear()
            translate()
        case '2':
            clear()
            import_api()

if __name__ == "__main__":
    main()