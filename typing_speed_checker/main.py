import tkinter as tk
import time
import random

texts = [
    "Python programming is used in every field in today's world.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast requires focus and consistent practice.",
    "Python is a popular programming language for beginners.",
    "Always check your code for syntax errors before running.",
    "Practice daily to improve your typing speed and accuracy."
]

class TypingSpeedChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Checker")
        self.root.geometry("600x400")
        self.sample_text = random.choice(texts)
        self.start_time_val = None

        # Title
        self.label = tk.Label(self.root, text="🧠 Type the following text:", font=("Arial", 15))
        self.label.pack(pady=10)

        # Sample Text
        self.text_label = tk.Label(self.root, text=self.sample_text, font=("Arial", 13), wraplength=550, justify="left")
        self.text_label.pack(pady=10)

        # Entry Box
        self.entry = tk.Entry(self.root, font=("Arial", 14), width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        # Result Label
        self.result_label = tk.Label(self.root, text='', font=("Arial", 13), fg="green")
        self.result_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(self.root, text="🔁 Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event=None):
        if self.start_time_val is None:
            self.start_time_val = time.time()

    def check_result(self, event=None):
        try:
            if self.start_time_val is None:
                self.result_label.config(text="⚠ Please click inside the typing box before starting.")
                return

            typed_text = self.entry.get().strip()
            if not typed_text:
                self.result_label.config(text="⚠ You haven't typed anything!")
                return

            end_time = time.time()
            time_taken = end_time - self.start_time_val
            if time_taken < 1:
                self.result_label.config(text="⚠ You typed too quickly to measure!")
                return

            words = len(typed_text.split())
            minutes = time_taken / 60
            wpm = words / minutes if minutes > 0 else 0

            # Accuracy Calculation
            correct_chars = sum(1 for a, b in zip(typed_text, self.sample_text) if a == b)
            total_chars = len(self.sample_text)
            accuracy = (correct_chars / total_chars) * 100

            # Result Formatting
            feedback = ""
            if accuracy == 100:
                feedback = "🎯 Perfect!"
            elif accuracy < 60:
                feedback = "💡 Try again, you can improve!"
            else:
                feedback = "👍 Good job!"

            self.result_label.config(
                text=f"{feedback}\nWPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nTime: {time_taken:.2f} sec"
            )

        except Exception as e:
            self.result_label.config(text=f"❌ An error occurred: {e}")

    def reset(self):
        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time_val = None
        self.entry.focus_set()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedChecker(root)
    root.mainloop()
