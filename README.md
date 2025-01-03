# Personal Diary App

A simple Python-based Personal Diary app built using Tkinter, allowing users to write and store their personal diary entries. The application supports saving, viewing, and managing entries by date. Data is stored using the `pickle` module to persist diary entries between app sessions.

## Features:
- Save and load diary entries for specific dates
- View and edit entries from a list of saved dates
- Select a date from a dropdown to add new entries
- Automatically saves entries to a file for future use
- Intuitive GUI with date picker, text editor, and saved dates list

## Requirements:
- Python 3.10
- Tkinter (comes pre-installed with Python)
- `pickle` module (comes pre-installed with Python)

## How to Use:
1. Run the Python script to start the application.
2. Select a date from the "Select Date" dropdown or double-click an existing date in the "Saved Dates" list to view the entry.
3. Add or modify your diary entry in the text editor.
4. Click the "Save Entry" button to save your entry for the selected date.
5. Your entries will be saved in the `diary_entries.dat` file and automatically loaded the next time you open the app.

## Installation:
1. Clone this repository:
    ```bash
    git clone https://github.com/Vikramjangid/Personal-Diary-App.git
    ```
2. Navigate to the project folder:
    ```bash
    cd Personal-Diary-App
    ```
3. Run the `diary_app.py` script:
    ```bash
    python diary_app.py
    ```

## Contributing:
Feel free to fork this repository, create pull requests, and contribute to enhancing the functionality of this app!

## Author:
[Vikram Jangid](https://github.com/Vikramjangid)

