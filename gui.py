# === gui.py ===
import tkinter as tk
from tkinter import messagebox
from collector import main as collect_all_evidence

def run_collector():
    try:
        collect_all_evidence()
        messagebox.showinfo("Success", "Evidence collected and report generated.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

def main():
    root = tk.Tk()
    root.title("Cybercrime Evidence Collector")
    root.geometry("400x200")

    label = tk.Label(root, text="Click to collect live forensic evidence", font=("Arial", 12))
    label.pack(pady=20)

    collect_button = tk.Button(root, text="Collect Evidence", command=run_collector,
                                font=("Arial", 12), bg="green", fg="white", height=2, width=20)
    collect_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()