import customtkinter as ctk
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def convert_temperature():
    temp_str = temp_entry.get().strip()
    scale = scale_option.get()
    try:
        temp = float(temp_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    if scale == "Celsius":
        celsius = temp
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
    elif scale == "Fahrenheit":
        celsius = (temp - 32) * 5/9
        fahrenheit = temp
        kelvin = celsius + 273.15
    elif scale == "Kelvin":
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        kelvin = temp
    else:
        messagebox.showerror("Error", "Unknown temperature scale.")
        return

    celsius_value.configure(text=f"{celsius:.2f} °C")
    fahrenheit_value.configure(text=f"{fahrenheit:.2f} °F")
    kelvin_value.configure(text=f"{kelvin:.2f} K")

f = ctk.CTk()
f.title("Temperature Converter")
window_width = 400
window_height = 350
screen_width = f.winfo_screenwidth()
screen_height = f.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
f.geometry(f"{window_width}x{window_height}+{x}+{y}")
f.resizable(False, False)

frame = ctk.CTkFrame(f, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

temp_label = ctk.CTkLabel(frame, text="Temperature:", font=("Helvetica", 12))
temp_label.pack(pady=(10, 5))
temp_entry = ctk.CTkEntry(frame, width=200, font=("Helvetica", 12), placeholder_text="Enter temperature")
temp_entry.pack(pady=(0, 10))

scale_label = ctk.CTkLabel(frame, text="Scale:", font=("Helvetica", 12))
scale_label.pack(pady=(10, 5))
scale_option = ctk.CTkOptionMenu(frame, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Helvetica", 12))
scale_option.set("Celsius")
scale_option.pack(pady=(0, 10))

convert_button = ctk.CTkButton(frame, text="Convert", font=("Helvetica", 12), command=convert_temperature)
convert_button.pack(pady=(10, 10))

result_frame = ctk.CTkFrame(frame, corner_radius=10)
result_frame.pack(pady=(10, 10), fill="both", expand=True)
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)
result_frame.grid_rowconfigure(0, weight=1)
result_frame.grid_rowconfigure(1, weight=1)
result_frame.grid_rowconfigure(2, weight=1)

celsius_label = ctk.CTkLabel(result_frame, text="Celsius:", font=("Helvetica", 12))
celsius_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
celsius_value = ctk.CTkLabel(result_frame, text="", font=("Helvetica", 12))
celsius_value.grid(row=0, column=1, sticky="w", padx=10, pady=5)

fahrenheit_label = ctk.CTkLabel(result_frame, text="Fahrenheit:", font=("Helvetica", 12))
fahrenheit_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
fahrenheit_value = ctk.CTkLabel(result_frame, text="", font=("Helvetica", 12))
fahrenheit_value.grid(row=1, column=1, sticky="w", padx=10, pady=5)

kelvin_label = ctk.CTkLabel(result_frame, text="Kelvin:", font=("Helvetica", 12))
kelvin_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
kelvin_value = ctk.CTkLabel(result_frame, text="", font=("Helvetica", 12))
kelvin_value.grid(row=2, column=1, sticky="w", padx=10, pady=5)

f.mainloop()
