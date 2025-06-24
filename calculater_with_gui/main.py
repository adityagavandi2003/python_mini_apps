import tkinter as tk
from tkinter import ttk


class CalcultorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CalculatorApp")
        self.root.geometry("400x600")
        self.root.resizable(True, True)

        self.expression = ""
        self.display_text = tk.StringVar()

        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill=tk.BOTH,expand=True)

        display_label = ttk.Label(
            display_frame,
            textvariable=self.display_text,
            font=("Arial",26),
            anchor="e",
            background="White",
            foreground="black",
            padding=6
        )
        display_label.pack(fill=tk.BOTH,expand=True)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH,expand=True)

        self.create_buttons(button_frame)
    
    def create_buttons(self,frame):
        # button_texts = [
        #     ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
        #     ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
        #     ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
        #     ("C",4,0),("0",4,1),("=",4,2),("+",4,3),
        # ]

        button_text = []

        numbers = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"]
        ]
        operators = ["/", "*", "-", "+"]

        # Add number and operator buttons for rows 1-3
        for row, nums in enumerate(numbers, start=1):
            for col, num in enumerate(nums):
                button_text.append((num, row, col))
            button_text.append((operators[row-1], row, 3))
            
        last_row = ["C", "0", "=", "+"]
        for col, text in enumerate(last_row):
            button_text.append((text, 4, col))

        
        for (text,row,col) in button_text:
            button = ttk.Button(frame,text=text,command=lambda t=text: self.on_click_button(t))
            button.grid(row=row,column=col,sticky="nsew",padx=2,pady=2)

        for i in range(5):
            frame.rowconfigure(i,weight=1)
            frame.columnconfigure(i,weight=1)

    def on_click_button(self,button_text):
        if button_text.lower() == "c":
            self.expression = ""
        elif button_text == "=":
            try:
              self.expression = str(eval(self.expression))
            except Exception as e:
              self.expression = "Error"
        else:
            self.expression += button_text
        
        self.display_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalcultorApp(root)
    root.mainloop()