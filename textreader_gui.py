# Note --v
# 
# This is the GUI code attempt. 
# This is not needed for functionality of the project due to full functionality via terminal commands. 
# This is left in file for learning purposes.


# import tkinter as tk
# from textreader import count_words, count_characters, count_lines, find_word_count
# from tkinter import filedialog  # Add this line for filedialog functionality
# from tkinter import messagebox


# def update_labels(text_content):
#     """Updates the result labels with the analyzed text content."""
#     if text_content:
#         word_count = count_words(text_content)
#         char_count = count_characters(text_content)
#         line_count = count_lines(text_content)
#         specific_word_count = find_word_count(text_content, search_word_entry.get())

#         word_count_label.config(text="Word Count: " + str(word_count))
#         char_count_label.config(text="Character Count: " + str(char_count))
#         line_count_label.config(text="Line Count: " + str(line_count))
#         specific_word_count_label.config(text="Specific Word Count ('" + search_word_entry.get() + "'): " + str(specific_word_count))
#     else:
#          # Handle case where no text content is available
#         messagebox.showerror("Error", "No text content available. Please open a file.")

# # Function to open file
# def open_file():
#     """Opens a file selection dialog and reads the chosen text file content."""
#     filename = tk.filedialog.askopenfilename(title="Select a File",
#                                        filetypes=[("Text Files", "*.txt"), ("Python Scripts", "*.py"), ("All Files", "*.*")])

#     if filename:
#         with open(filename, "r") as file:
#             text_content = file.read()
#         print("File content:", text_content[:20])  # Print first 20 characters for preview
#     else:
#         # Handle case where no file was selected (optional)
#         pass

# # Function to analyze text
# def analyze_text():
#     """Analyzes the text content and updates result labels."""
#     if text_content:  # Check if text content is available (file opened)
#         word_count = count_words(text_content)
#         char_count = count_characters(text_content)
#         line_count = count_lines(text_content)
#         specific_word_count = find_word_count(text_content, search_word_entry.get())  # Get search word from entry field

#         word_count_label.config(text="Word Count: " + str(word_count))
#         char_count_label.config(text="Character Count: " + str(char_count))
#         line_count_label.config(text="Line Count: " + str(line_count))
#         specific_word_count_label.config(text="Specific Word Count ('" + search_word_entry.get() + "'): " + str(specific_word_count))

#         print("Word count:", word_count)
#         print("Character count:", char_count)
#         print("Line count:", line_count)
#         print("Specific word count:", specific_word_count)

#         # Call update_labels function to update GUI
#         update_labels(text_content)
#     else:
#         # Handle case where no text content is available
#         messagebox.showerror("Error", "No text content available. Please open a file.")

        
# # Main program flow
# root = tk.Tk()
# root.title("Text File Analyzer")
# root.geometry("500x300")  # Set window size

# # Text entry field for search word
# search_word_entry = tk.Entry(root, width=50)
# search_word_entry.pack(pady=10)  # Add padding for spacing
# search_word_entry.insert(0, "Enter the word to search for")  # Set default text

# # Open file button
# open_file_button = tk.Button(root, text="Open File", command=open_file)
# open_file_button.pack(pady=10)  # Add padding for spacing

# # Analyze text button
# analyze_button = tk.Button(root, text="Analyze Text", command=analyze_text)
# analyze_button.pack(pady=10)  # Add padding for spacing

# # Labels for results (replace placeholders with actual variable names)
# word_count_label = tk.Label(root, text="Word Count:")
# word_count_label.pack()

# char_count_label = tk.Label(root, text="Character Count:")
# char_count_label.pack()

# line_count_label = tk.Label(root, text="Line Count:")
# line_count_label.pack()

# specific_word_count_label = tk.Label(root, text="Specific Word Count:")
# specific_word_count_label.pack()

# # Initialize text content variable (assuming it's empty initially)
# text_content = ""

# # Keep the window running
# root.mainloop()

