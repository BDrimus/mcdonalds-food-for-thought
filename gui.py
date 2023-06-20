import customtkinter as ctk
import tkinter as tk


def display_gui():
    
    def get_receipt():
        entry_code.set(entry1.get())
        amount_spent.set(entry2.get())
        root.destroy()
        return entry_code, amount_spent

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("500x300")

    root.title("Receipt Reader")

    entry_code = tk.StringVar()
    amount_spent = tk.StringVar()

    frame = ctk.CTkFrame(master=root)
    frame.grid(pady=40, padx=66)

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    label = ctk.CTkLabel(master=frame, text="McDonald's Food for Thought", font=("Consolas", 20))
    label.grid(row=0, column=0, columnspan=2, pady=12, padx=20)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Entry Code separated by hyphens")
    entry1.grid(row=1, column=0, pady=12, padx=12)
    label1 = ctk.CTkLabel(master=frame, text="eg. AB12-CD34-EF56", text_color="gray")
    label1.grid(row=1, column=1, sticky="w", pady=12, padx=12)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Amount Spent")
    entry2.grid(row=4, column=0, pady=12, padx=12)
    label2 = ctk.CTkLabel(master=frame, text="eg. 12.38", text_color="gray")
    label2.grid(row=4, column=1, sticky="w", pady=12, padx=12)

    button = ctk.CTkButton(master=frame, text="Submit", command=get_receipt)
    button.grid(row=5, column=0, columnspan=2, pady=12, padx=12)

    root.mainloop()

    return (entry_code.get()).upper(), amount_spent.get()