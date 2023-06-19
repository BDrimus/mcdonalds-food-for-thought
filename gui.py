import customtkinter as ctk
import tkinter as tk


def display_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("500x360")

    root.title("Receipt Reader")

    frame = ctk.CTkFrame(master=root)
    frame.grid(pady=50, padx=65)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    label = ctk.CTkLabel(master=frame, text="McDonald's Food for Thought", font=("Consolas", 20))
    label.grid(row=0, column=0, columnspan=2, pady=12)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Entry Code with Spaces")
    entry1.grid(row=1, column=0, pady=12, padx=12)
    label1 = ctk.CTkLabel(master=frame, text="Eg. AB12 CD34 EF56")
    label1.grid(row=1, column=1, sticky="w", pady=12, padx=12)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Date of Order (DD/MM/YYYY)")
    entry2.grid(row=2, column=0, pady=12, padx=12)
    label2 = ctk.CTkLabel(master=frame, text="Date of Order (DD/MM/YYYY)")
    label2.grid(row=2, column=1, sticky="w", pady=12, padx=12)

    entry3 = ctk.CTkEntry(master=frame, placeholder_text="Time of Order (HH:MM)")
    entry3.grid(row=3, column=0, pady=12, padx=12)
    label3 = ctk.CTkLabel(master=frame, text="Time of Order (HH:MM)")
    label3.grid(row=3, column=1, sticky="w", pady=12, padx=12)

    entry4 = ctk.CTkEntry(master=frame, placeholder_text="Amount Spent")
    entry4.grid(row=4, column=0, pady=12, padx=12)
    label4 = ctk.CTkLabel(master=frame, text="Amount Spent")
    label4.grid(row=4, column=1, sticky="w", pady=12, padx=12)

    root.mainloop()

def get_receipt():

    entry_code = input("Please enter your entry code: ")
    date_of_order = input("Please enter the date of your order (DD/MM/YYYY): ")
    time_of_order = input("Please enter the time of your order (HH:MM): ")
    amount_spent = input("Please enter the amount spent: ")

display_gui()