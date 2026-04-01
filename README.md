**Passgen**

A lightweight, secure password generator built with Python and Tkinter.

##  Features:

- **Cryptographically Secure**: Uses Python's `secrets` module for secure random generation
- **Customizable Length**: Generate passwords of any desired length
- **Character Options**: Toggle symbols and uppercase letters
- **Multiple Passwords**: Generates one primary password plus 5 alternatives
- **Clipboard Integration**: One-click copy to clipboard
- **Simple GUI**: Clean, intuitive ## Features:

## 📋 Requirements

- Python 3.8 or higher
- Tkinter (usually included with Python installations)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Nobuka72/passgen.git
cd passgen
```

2. Ensure Python 3.8+ is installed:
```bash
python3 --version
```

## Usage

Run the application:
```bash
python3 passwordgenerator.py
```

Or make it executable:
```bash
chmod +x passwordgenerator
./passwordgenerator
```

### How to Use

1. **Enter Password Length**: Type the desired length in the input field
2. **Select Options**: 
   - Check "Include symbols?" for special characters (!@#$%^&*, etc.)
   - Check "Include uppercase letters?" for A-Z characters
3. **Generate**: Click the "Generate" button to create passwords
4. **Copy**: Click "Copy to clipboard" to copy the main password


## 📸 Screenshot

![Passgen Screenshot](passgen-screenshot.png)

### Example

- Length: `16`
- Options: Both symbols and uppercase enabled
- Result: `aB3!xR9@mK7#pQ2$` (primary) + 5 alternatives
