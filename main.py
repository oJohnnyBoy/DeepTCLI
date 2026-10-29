import deepl
import os
from rich import print
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter as WC
from pathlib import Path



languages = ['PT-BR', 'EN-US', 'JA']

completer = WC(languages, ignore_case=True)



client = deepl.DeepLClient('')#your deepL API key


def translate():
   print('[italic red]_________SELECT LANGUAGE_________')
   lang1 = prompt(
    "Language (PT-BR, EN-US, JA...): \n",
    completer=completer,
).strip().upper()
   clear()

   print(f'You choose {lang1}')
   txt = input('What do you want to translate? \n')
   clear()

   result = client.translate_text(txt, target_lang=lang1) 
   
   print(f'Your text: "{txt}" \nHas been sucessfully translated to: {lang1}\nHere is your translation: \n{result.text}')

def import_api():
    return

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class main():
    clear()
    print('[italic bold red]__________________________\n \n---------WELCOME!---------\n__________________________\n')
    c1 = input('Select what do you want to do: \n1. Translate. \n2. Import a API KEY.\n')
    match c1:
        case '1':
            clear()
            translate()
        case '2':
            clear()
            import_api()

if __name__ == "__main__":
    main()