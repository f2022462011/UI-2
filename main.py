import tkinter as tk
from tkinter import ttk

def perform_action():
    selected_option = prompt_var.get()
    text = text_entry.get()
    if selected_option == "Sentimental Analysis":
        # Perform sentiment analysis
        print("Performing sentiment analysis on:", text)
    elif selected_option == "Named Entity Recognition":
        # Perform named entity recognition
        print("Performing named entity recognition on:", text)
    elif selected_option == "Summarization":
        # Perform text summarization
        print("Performing summarization on:", text)
    elif selected_option == "Translation into English":
        # Perform translation into English
        print("Performing translation into English on:", text)

# Create main window
root = tk.Tk()
root.title("NLP Tool")

# Create text entry box
text_label = tk.Label(root, text="Text:")
text_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
text_entry = tk.Entry(root, width=50)
text_entry.grid(row=0, column=1, padx=10, pady=5)

# Create prompt entry box
prompt_label = tk.Label(root, text="Prompt:")
prompt_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
prompt_entry = ttk.Combobox(root, values=["Sentimental Analysis", "Named Entity Recognition", "Summarization", "Translation into English"])
prompt_entry.grid(row=1, column=1, padx=10, pady=5)
prompt_entry.current(0)  # Set default option

# Create button to perform action
perform_button = tk.Button(root, text="Perform Action", command=perform_action)
perform_button.grid(row=2, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
