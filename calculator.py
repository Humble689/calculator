import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        self.equation = ""
        
        # Entry widget to display the equation
        self.entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief="ridge")
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)
        ]
        
        for btn in buttons:
            text, row, col = btn[:3]
            colspan = btn[3] if len(btn) == 4 else 1
            action = lambda x=text: self.on_button_click(x)
            tk.Button(root, text=text, font=("Arial", 18), command=action, width=5, height=2).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.equation = ""
        elif char == "=":
            try:
                self.equation = str(eval(self.equation))  # Calculate result
            except Exception:
                self.equation = "Error"
        else:
            self.equation += char
        
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
