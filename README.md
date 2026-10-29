# DeepTCLI

A lightweight, open-source command-line translation tool powered by the [DeepL API](https://www.deepl.com/pro-api). Quickly translate text between languages directly from your terminal with an intuitive, autocomplete-enabled interface.

---

## ✨ Features

- 🌐 Translate text to multiple languages (Portuguese, English, Japanese, and more)
- ⌨️ Autocomplete language selection via `prompt_toolkit`
- 🎨 Colorful terminal output with `rich`
- 🔑 DeepL API integration for high-quality machine translation
- 🖥️ Cross-platform support (Windows & Linux/macOS)

---

## 📋 Requirements

- Python 3.10+
- A valid [DeepL API key](https://www.deepl.com/pro-api) (Free tier available)

---

## 🚀 Getting Started

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

### 4. Set your DeepL API key

Open `main.py` and replace the placeholder with your own API key:

```python
client = deepl.DeepLClient('YOUR_DEEPL_API_KEY_HERE')
```

---

## ▶️ Usage

```bash
python main.py
```

You will be presented with a menu:

```
__________________________

---------WELCOME!---------
__________________________

Select what do you want to do:
1. Translate.
2. Import a API KEY.
```

Choose option **1** to start translating. Type your target language (with autocomplete support) and enter the text you want to translate.

### Supported Languages (examples)

| Code  | Language            |
| ----- | ------------------- |
| PT-BR | Portuguese (Brazil) |
| EN-US | English (US)        |
| JA    | Japanese            |
| ES    | Spanish             |
| FR    | French              |
| DE    | German              |

> For the full list of supported language codes, refer to the [DeepL API docs](https://developers.deepl.com/docs/resources/supported-languages).

---

## 📁 Project Structure

```
DeepTCLI/
├── main.py           # Main entry point
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── venv/             # Virtual environment (not committed)
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
