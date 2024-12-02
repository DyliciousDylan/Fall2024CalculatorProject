import tkinter as tk
from tkinter import messagebox

def clear_values():
    value_entry.delete("1.0", tk.END)

def compute_sample_std_dev():
    try:
        values = list(map(float, value_entry.get("1.0", tk.END).strip().splitlines()))
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
        result = variance ** 0.5
        messagebox.showinfo("Result", f"Sample Standard Deviation: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter one value per line.")

def compute_population_std_dev():
    try:
        values = list(map(float, value_entry.get("1.0", tk.END).strip().splitlines()))
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        result = variance ** 0.5
        messagebox.showinfo("Result", f"Population Standard Deviation: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter one value per line.")

def compute_mean():
    try:
        values = list(map(float, value_entry.get("1.0", tk.END).strip().splitlines()))
        result = sum(values) / len(values)
        messagebox.showinfo("Result", f"Mean: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter one value per line.")

def compute_z_score():
    try:
        value, mean, std_dev = map(float, value_entry.get("1.0", tk.END).strip().split())
        result = (value - mean) / std_dev
        messagebox.showinfo("Result", f"Z-Score: {result}")
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter value, mean, stdDev on one line.")

def compute_single_linear_regression():
    # Placeholder function
    messagebox.showinfo("Feature", "This function is not yet implemented.")

def compute_y_from_linear_regression():
    # Placeholder function
    messagebox.showinfo("Feature", "This function is not yet implemented.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Add UI elements
header_label = tk.Label(root, text="Calculator", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_values)
clear_button.pack()

instruction_label = tk.Label(root, text="Enter values below, then select an operation", bg="peach puff", font=("Arial", 10))
instruction_label.pack(pady=5, fill="x")

value_entry = tk.Text(root, height=10, width=50)
value_entry.pack(pady=5)

# Descriptive Statistics Section
desc_stats_label = tk.Label(root, text="Descriptive Statistics", font=("Arial", 12, "bold"))
desc_stats_label.pack(pady=10)

sample_std_dev_button = tk.Button(root, text="Compute Sample Standard Deviation | one value per line", command=compute_sample_std_dev)
sample_std_dev_button.pack(pady=2)

population_std_dev_button = tk.Button(root, text="Compute Population Standard Deviation | one value per line", command=compute_population_std_dev)
population_std_dev_button.pack(pady=2)

mean_button = tk.Button(root, text="Compute Mean | one value per line", command=compute_mean)
mean_button.pack(pady=2)

z_score_button = tk.Button(root, text="Compute Z Score | value, mean, stdDev on one line", command=compute_z_score)
z_score_button.pack(pady=2)

# Single Linear Regression Section
regression_label = tk.Label(root, text="Single Linear Regression", font=("Arial", 12, "bold"))
regression_label.pack(pady=10)

single_lr_button = tk.Button(root, text="Compute Single Linear Regression Formula | one x,y pair per line", command=compute_single_linear_regression)
single_lr_button.pack(pady=2)

compute_y_button = tk.Button(root, text="Compute Y from Linear Regression Formula | x, m, b on one line", command=compute_y_from_linear_regression)
compute_y_button.pack(pady=2)

# Start the GUI event loop
root.mainloop()
