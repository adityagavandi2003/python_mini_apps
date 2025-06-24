import tkinter as tk
from tkinter import ttk

class UnitConverter:
    def __init__(self,root):
        self.root = root
        self.root.title("Unit Converter ")
        self.root.geometry("400x600")
        self.root.resizable(True, True)

        header = tk.Label(self.root, text="Unit Converter", font=("Arial", 20, "bold"))
        header.pack(pady=20)

        # drop down for length category
        category_label = tk.Label(self.root,text="Select category",font=("Arial", 8, "bold"))
        category_label.pack(pady=10)
        self.combo_category = ttk.Combobox(self.root,values=["length"],state="readonly")
        self.combo_category.current(0)
        self.combo_category.pack(pady=6)
        
        # drop down for unit converter (from)
        from_label = tk.Label(self.root,text="Select Converter",font=("Arial", 8, "bold"))
        from_label.pack(pady=10)
        self.combo_from = ttk.Combobox(self.root,values=["meter","kilometer","inches","feet"],state="readonly")
        self.combo_from.current(0)
        self.combo_from.pack(pady=6)
        
        # drop down for unit converter (to)
        to_label = tk.Label(self.root,text="Convert to",font=("Arial", 8, "bold"))
        to_label.pack(pady=10)
        self.combo_to = ttk.Combobox(self.root,values=["meter","kilometer","inches","feet"],state="readonly")
        self.combo_to.current(0)
        self.combo_to.pack(pady=6)

        # value input
        entry_label = tk.Label(self.root,text="Enter a value that want to convert")
        entry_label.pack(pady=10)
        self.entry_value = ttk.Entry(self.root)
        self.entry_value.pack(pady=5)
        
        # button to perform conversions
        button_convert = tk.Button(self.root,text="Convert",command=self.convert_units)
        button_convert.pack(pady=11)

        # result
        self.label_result = tk.Label(self.root,text="Result")
        self.label_result.pack(pady=6)

    def length_conversion(self, value, from_unit, to_unit):
        conversion_factor = {
            "meter": 1,
            "kilometer": 0.001,
            "inches": 39.3701,
            "feet": 3.28084
        }
        # Convert value to meters first, then to target unit
        value_in_meters = float(value) / conversion_factor[from_unit]
        return value_in_meters * conversion_factor[to_unit]
    
    def convert_units(self):
        try:
            value = float(self.entry_value.get())
            from_unit = self.combo_from.get()
            to_unit = self.combo_to.get()
            category = self.combo_category.get()

            if category.lower() == "length":
                result = self.length_conversion(value, from_unit, to_unit)
            else:
                self.label_result.config(text="Unsupported category")
                return
            self.label_result.config(text=f"Result: {result:.2f} {to_unit}")
        except Exception:
            self.label_result.config(text="Enter a valid number")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()