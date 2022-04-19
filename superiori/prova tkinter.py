import tkinter as tk

window = tk.Tk()
window.geometry("700x400")
window.title("prova")
window.resizable (False, False)
window.configure (background="white")

def first_print():
    text = "hello world"
    text_output=tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, sticky="W")


def second_print():
    text = "nuovo messaggio"
    text_output=tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=100, sticky="W")

first_button = tk.Button(text="saluta", command=first_print)
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="seconda", command=second_print)
second_button.grid(row=1, column=0, sticky="W")

if __name__ == "__main__":
    window.mainloop()
    
