# macOS Clipboard Manager

This project is a clipboard manager application for macOS that allows users to manage their clipboard history efficiently. The application runs in the taskbar, providing easy access to clipboard operations.

simple clipboard manager written in python

## Features

- Copy and paste functionality
- Clipboard history management
- Accessible from the macOS taskbar

## Project Structure

```
macos-clipboard-manager
├── src
│   ├── main.py          # Entry point of the application
│   ├── ui
│   │   └── taskbar.py   # Manages the taskbar icon and interactions
│   ├── clipboard
│   │   └── manager.py   # Handles clipboard operations
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd macos-clipboard-manager
   ```

2. Install the required dependencies & add to startup:
   ```
   python3 startup.py   
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Once the application is running, you can access it from the taskbar. 
