import tkinter as tk
from tkinter import messagebox, ttk
import pickle
import os

entries_file = "diary_entries.dat"

# Function to load all saved entries on startup
def load_all_entries():
    if os.path.exists(entries_file):
        try:
            with open(entries_file, 'rb') as file:
                entries = pickle.load(file)
            return entries
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load entries on startup: {e}")
            return {}
    return {}

# Function to save diary entries for a specific date
def save_entries():
    selected_date = date_picker.get()
    if not selected_date:
        messagebox.showwarning("Warning", "Please select a date.")
        return

    entry_content = diary_text.get("1.0", tk.END).strip()
    if not entry_content:
        messagebox.showwarning("Warning", "Diary entry cannot be empty.")
        return

    try:
        entries[selected_date] = entry_content

        with open(entries_file, 'wb') as file:
            pickle.dump(entries, file)

        messagebox.showinfo("Success", f"Diary entry for {selected_date} saved successfully!")
        diary_text.delete("1.0", tk.END)
        refresh_saved_dates()
        refresh_date_picker()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save diary entry: {e}")

# Function to load diary entries for a specific date
def load_entries(event=None):
    selected_date = saved_dates_listbox.get(saved_dates_listbox.curselection())
    if selected_date in entries:
        diary_text.delete("1.0", tk.END)
        diary_text.insert(tk.END, entries[selected_date])
    else:
        messagebox.showinfo("Info", f"No entry found for {selected_date}.")

# Function to refresh the saved dates listbox
def refresh_saved_dates():
    saved_dates_listbox.delete(0, tk.END)
    for date in sorted(entries.keys()):
        saved_dates_listbox.insert(tk.END, date)

# Function to refresh the date picker dropdown
def refresh_date_picker():
    date_picker["values"] = sorted(entries.keys())

# Create the main window
root = tk.Tk()
root.title("Personal Diary")
root.geometry("800x500")

# Load all entries on startup
entries = load_all_entries()

# Create the main frames
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

saved_dates_frame = tk.Frame(main_frame)
saved_dates_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

editor_frame = tk.Frame(main_frame)
editor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Saved dates section
saved_dates_label = tk.Label(saved_dates_frame, text="Saved Dates")
saved_dates_label.pack(anchor=tk.W, padx=5, pady=5)

saved_dates_listbox = tk.Listbox(saved_dates_frame, height=25, width=20)
saved_dates_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
saved_dates_listbox.bind("<Double-1>", load_entries)

refresh_saved_dates()

# Editor section
editor_top_frame = tk.Frame(editor_frame)
editor_top_frame.pack(fill=tk.X, pady=5)

date_label = tk.Label(editor_top_frame, text="Select Date:")
date_label.pack(side=tk.LEFT, padx=5)

date_picker = ttk.Combobox(editor_top_frame)
date_picker.pack(side=tk.LEFT, padx=5)
date_picker['values'] = sorted(entries.keys())
date_picker.set("Select a Date")

save_button = tk.Button(editor_top_frame, text="Save Entry", command=save_entries)
save_button.pack(side=tk.LEFT, padx=5)

# Text editor
scrollbar = tk.Scrollbar(editor_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

diary_text = tk.Text(editor_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
diary_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=diary_text.yview)

# Run the application
root.mainloop()
