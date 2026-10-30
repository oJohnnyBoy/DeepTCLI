# DeepTCLI

DeepTCLI is a lightweight command-line translation tool powered by the [DeepL API](https://www.deepl.com/pro-api). It lets you translate text from your terminal, save API keys locally, and manage them from an interactive menu.

---

## Features

- Translate text using the DeepL API
- Autocomplete language selection with `prompt_toolkit`
- Rich terminal UI with `rich`
- Save and manage API keys locally in `keys.json`
- Cross-platform support for Windows, Linux, and macOS

---

## Requirements

- Python 3.10+
- A valid [DeepL API key](https://www.deepl.com/pro-api)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/oJohnnyBoy/DeepTCLI.git
cd DeepTCLI
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python main.py
```

---

## Usage

When the app starts, you will see a menu like this:

```text
[bold red]Welcome to DeepTCLI
Select what do you want to do:
1. Translate.
2. Manage your API keys.
```

### Translate text

Choose `1` and then type the target language code, such as:

- `PT-BR`
- `EN-US`
- `JA`

Then enter the text you want to translate.

### Manage your API keys

Choose `2` to open the API manager. From there you can:

- import a key
- delete a saved key
- list saved keys

Keys are stored in a local file named `keys.json` in the project directory.

---

## Supported languages

Examples include:

| Code  | Language            |
| ----- | ------------------- |
| PT-BR | Portuguese (Brazil) |
| EN-US | English (US)        |
| JA    | Japanese            |
| ES    | Spanish             |
| FR    | French              |
| DE    | German              |

For the full list, see the [DeepL supported languages documentation](https://developers.deepl.com/docs/resources/supported-languages).

---

## Project structure

```text
DeepTCLI/
├── config.py         # API key storage and menu logic
├── main.py           # Main translation app entry point
├── keys.json         # Saved API keys (created when first imported)
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── .gitignore        # Git ignore rules
```

---

## Contributing

Contributions are welcome. If you want to improve the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## License

This project is open source and available under the MIT license.
