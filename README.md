# DeepTCLI

DeepTCLI is a lightweight command-line translation tool powered by the [DeepL API](https://www.deepl.com/pro-api). It lets you translate text from your terminal, save API keys securely, and manage them from an interactive menu.

---

## Features

- Translate text using the DeepL API
- Autocomplete language selection with `prompt_toolkit`
- Rich terminal UI with `rich`
- Save and manage API keys securely in the OS config directory
- API keys are masked when displayed and stored with restricted permissions
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

### 3. Install the package

```bash
pip install -e .
```

> **Note:** This installs all dependencies automatically from `pyproject.toml`. You can also install dependencies manually with `pip install -r requirements.txt`.

### 4. Run the app

```bash
deeptcli
```

> On Windows the alias `DeepTCLI` also works.

---

## Usage

When the app starts, you will see a menu like this:

```
Welcome to DeepTCLI
Select what do you want to do:
1. Translate.
2. Manage your API keys.
```

### Translate text

Choose `1`. An autocomplete prompt will appear — start typing a language code such as:

| Code  | Language            |
| ----- | ------------------- |
| PT-BR | Portuguese (Brazil) |
| EN-US | English (US)        |
| JA    | Japanese            |
| ES    | Spanish             |
| FR    | French              |
| DE    | German              |

Then enter the text you want to translate and the result will be displayed in the terminal.

For the full list of supported languages, see the [DeepL supported languages documentation](https://developers.deepl.com/docs/resources/supported-languages).

### Manage your API keys

Choose `2` to open the API Manager. From there you can:

1. **Import a key** — paste your DeepL API key (input is hidden while typing)
2. **Delete a key** — remove a saved key after confirmation
3. **Show your registered keys** — display all saved keys (masked for security)
4. **Back** — return to the main menu

Keys are stored in the OS config directory:

| OS      | Location                              |
| ------- | ------------------------------------- |
| Windows | `%APPDATA%\deeptcli\keys.json`        |
| Linux   | `$XDG_CONFIG_HOME/deeptcli/keys.json` (defaults to `~/.config/deeptcli/keys.json`) |
| macOS   | `~/.config/deeptcli/keys.json`        |

---

## Project Structure

```text
DeepTCLI/
├── deeptcli/
│   ├── __init__.py       # Package init
│   ├── __main__.py       # Allows running as `python -m deeptcli`
│   ├── main.py           # Main translation app entry point
│   ├── config.py         # API key storage and menu logic
│   └── keys.json         # Legacy key file (keys now stored in OS config dir)
├── pyproject.toml        # Package metadata and build config
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
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
