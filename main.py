import tkinter as tk
from tkinter import messagebox
from temperatura import temperatura
from cpu import cpu

# Declaramos las variables globales para que todas las funciones las reconozcan
ventana = None
entrada_nombre = None
entrada_comp = None
boton_saludar = None

def mostrar_saludo():
    global entrada_comp # Necesitamos avisar que usaremos la global
    
    nombre = entrada_nombre.get()
    
    if nombre:
        messagebox.showinfo("Saludo", f"¡Hola {nombre}, bienvenido a tu app!")
        
        # Si no existe la segunda caja, la creamos
        if entrada_comp is None:
            tk.Label(ventana, text="Elige componente (temperatura / cpu):").pack()
            
            entrada_comp = tk.Entry(ventana, width=30)
            entrada_comp.pack(pady=5)
            
            tk.Button(ventana, text="Buscar", command=buscar_componente, bg="#2ecc71", fg="white").pack(pady=10)
            
            # Desactivamos el botón para que no se repita el proceso
            boton_saludar.config(state="disabled")
    else:
        messagebox.showwarning("Error", "Por favor, escribe tu nombre.")

def buscar_componente():
    usuario = entrada_nombre.get()
    # Leemos lo que puso en la segunda caja
    componente = entrada_comp.get().lower() 
    
    if componente == "temperatura":
        lectura = temperatura()
        messagebox.showinfo("Lectura Temperatura", f"¡Hola {usuario}! La temperatura es: {lectura}")
    elif componente == "cpu":
        resultado = cpu()
        messagebox.showinfo(f"Lectura CPU", f"{resultado}")
    else:
        messagebox.showwarning("Error", "Escribe 'temperatura' o 'cpu'")

def main():
    global ventana, entrada_nombre, boton_saludar
    
    ventana = tk.Tk()
    ventana.title("Mi App en Ubuntu")
    ventana.geometry("400x500")

    tk.Label(ventana, text="Gestor de Datos", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(ventana, text="Introduce tu nombre:").pack()

    entrada_nombre = tk.Entry(ventana, width=30)
    entrada_nombre.pack(pady=5)

    boton_saludar = tk.Button(ventana, text="Saludar y Continuar", command=mostrar_saludo, bg="#3498db", fg="white")
    boton_saludar.pack(pady=20)

    ventana.mainloop()

if __name__ == '__main__':
    main()