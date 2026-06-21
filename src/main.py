import tkinter as tk
from tkinter import messagebox
from temperature import get_temperature
import subprocess
import os

# Base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function variables (Tkinter references)
window = None
name_entry = None
comp_entry = None
greet_button = None

def show_greeting():
    global comp_entry # Declare comp_entry as global to modify it
    
    name = name_entry.get()
    
    if name:
        messagebox.showinfo("Greeting", f"Hello {name}, welcome to your app!")
        
        # If the second input field does not exist, create it
        if comp_entry is None:
            tk.Label(window, text="Choose component (temperature / cpu):").pack()
            
            comp_entry = tk.Entry(window, width=30)
            comp_entry.pack(pady=5)
            
            tk.Button(window, text="Search", command=search_component, bg="#2ecc71", fg="white").pack(pady=10)
            
            # Disable the greeting button to prevent duplication
            greet_button.config(state="disabled")
    else:
        messagebox.showwarning("Error", "Please enter your name.")

def search_component():
    user = name_entry.get()
    # Read what the user typed in the second input field
    component = comp_entry.get().lower() 
    
    if component == "temperatura" or component == "temp" or component == "temperature":
        reading = get_temperature()
        messagebox.showinfo("Temperature Reading", f"Hello {user}! The temperature is: {reading}")
    elif component == "cpu":
        result = get_cpu_usage()
        messagebox.showinfo("CPU Reading", f"{result}")
    else:
        messagebox.showwarning("Error", "Please enter 'temperature' or 'cpu'")

def get_cpu_usage():
    try:
        motor_path = os.path.join(BASE_DIR, "cpu_motor")
        # text=True automatically decodes the output as a string
        result = subprocess.check_output([motor_path], text=True)
        return result.strip()
    except FileNotFoundError:
        return f"Error: 'cpu_motor' not found in {BASE_DIR}. Did you compile it?"
    except subprocess.CalledProcessError as e:
        return f"The C program failed (Exit Code {e.returncode})"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    global window, name_entry, greet_button
    
    window = tk.Tk()
    window.title("System Status")
    window.geometry("400x500")

    try:
        logo_path = os.path.join(BASE_DIR, "assets", "logo.png")
        logo_photo = tk.PhotoImage(file=logo_path)
        window.iconphoto(False, logo_photo)
        window.logo_reference = logo_photo 
    except Exception as e:
        print(f"Error loading logo from {logo_path}: {e}")

    tk.Label(window, text="Data Manager", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(window, text="Enter your name:").pack()

    name_entry = tk.Entry(window, width=30)
    name_entry.pack(pady=5)

    greet_button = tk.Button(window, text="Greet and Continue", command=show_greeting, bg="#3498db", fg="white")
    greet_button.pack(pady=20)

    window.mainloop()

if __name__ == '__main__':
    main()