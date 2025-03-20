import customtkinter as ctk
from tkinter import messagebox, Toplevel
import sqlite3

# Categorías disponibles
CATEGORIAS = ["Bebidas", "Panadería Tradicional", "Hojaldre", "Tortas", "Galletas", "Snacks", "Confitería", "Productos sin gluten"]

# Conectar y asegurar que la tabla existe
def inicializar_bd():
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Alimentos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT,
                Cantidad INTEGER,
                Categoria TEXT,
                Precio REAL
            )
        """)
        conexion.commit()
        
        cursor.execute("SELECT COUNT(*) FROM Alimentos")
        if cursor.fetchone()[0] == 0:
            alimentos = [
                ("Coca-Cola", 20, "Bebidas", 2.500),
                ("Pepsi", 15, "Bebidas", 2.300),
                ("Fanta", 10, "Bebidas", 2.200),
                ("Sprite", 12, "Bebidas", 2.400),
                ("Agua", 25, "Bebidas", 1.000),
                ("Croissant", 10, "Panadería Tradicional", 3.500),
                ("Pan de queso", 15, "Panadería Tradicional", 4.000),
                ("Almojábana", 8, "Panadería Tradicional", 2.800),
                ("Bagel", 7, "Panadería Tradicional", 3.200),
                ("Brioche", 6, "Panadería Tradicional", 3.800),
                ("Pastel de pollo", 10, "Hojaldre", 4.500),
                ("Pastel de carne", 12, "Hojaldre", 4.200),
                ("Pastel de arequipe", 5, "Hojaldre", 3.800),
                ("Empanada", 14, "Hojaldre", 3.600),
                ("Volován", 9, "Hojaldre", 3.900),
                ("Torta de chocolate", 10, "Tortas", 3.500),
                ("Torta de fresa", 8, "Tortas", 3.800),
                ("Torta de vainilla", 6, "Tortas", 3.700),
                ("Cheesecake", 5, "Tortas", 4.500),
                ("Tiramisu", 7, "Tortas", 4.000),
                ("Galletas de chispas", 15, "Galletas", 2.500),
                ("Galletas de avena", 10, "Galletas", 2.700),
                ("Galletas rellenas", 12, "Galletas", 3.200),
                ("Macarons", 5, "Galletas", 4.500),
                ("Galletas de jengibre", 8, "Galletas", 3.000)
            ]
            cursor.executemany("INSERT INTO Alimentos (Nombre, Cantidad, Categoria, Precio) VALUES (?, ?, ?, ?)", alimentos)
            conexion.commit()

inicializar_bd()

def mostrar_mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def mostrar_inventario():
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT Nombre, Categoria, Cantidad, Precio FROM Alimentos")
        productos = cursor.fetchall()
    
    if not productos:
        mostrar_mensaje("Inventario", "No hay productos en el inventario.")
        return
    
    ventana_inventario = Toplevel()
    ventana_inventario.title("Inventario")
    ventana_inventario.geometry("500x400")
    
    frame = ctk.CTkFrame(ventana_inventario)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    ctk.CTkLabel(frame, text="Inventario de Productos", font=("Arial", 16, "bold")).pack(pady=10)
    
    for prod in productos:
        ctk.CTkLabel(frame, text=f"{prod[0]} ({prod[1]}): {prod[2]} unidades a ${prod[3]:.2f}").pack(anchor='w', padx=10)

def agregar_producto_inventario(entrada_producto, categoria_var, entrada_precio, entrada_cantidad):
    try:
        producto, categoria, precio, cantidad = entrada_producto.get(), categoria_var.get(), float(entrada_precio.get()), int(entrada_cantidad.get())
    except ValueError:
        mostrar_mensaje("Error", "Precio o cantidad inválida.")
        return
    
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Alimentos (Nombre, Cantidad, Categoria, Precio) VALUES (?, ?, ?, ?)", (producto, cantidad, categoria, precio))
        conexion.commit()
    
    mostrar_mensaje("Éxito", f"Producto '{producto}' agregado.")

def eliminar_producto(entrada_producto):
    producto_a_eliminar = entrada_producto.get()
    
    with sqlite3.connect("database.db") as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Alimentos WHERE Nombre = ?", (producto_a_eliminar,))
        conexion.commit()
    
    mostrar_mensaje("Éxito", f"Producto '{producto_a_eliminar}' eliminado del inventario.")

def crear_ventana_empleado():
    ctk.set_appearance_mode("dark")
    ventana = ctk.CTk()
    ventana.title("Panel de Empleados")
    ventana.geometry("400x500")
    
    entrada_producto = ctk.CTkEntry(ventana)
    entrada_precio = ctk.CTkEntry(ventana)
    entrada_cantidad = ctk.CTkEntry(ventana)
    categoria_var = ctk.StringVar()
    
    ctk.CTkLabel(ventana, text="Producto:").pack()
    entrada_producto.pack()
    ctk.CTkLabel(ventana, text="Categoría:").pack()
    ctk.CTkComboBox(ventana, variable=categoria_var, values=CATEGORIAS).pack()
    ctk.CTkLabel(ventana, text="Precio:").pack()
    entrada_precio.pack()
    ctk.CTkLabel(ventana, text="Cantidad:").pack()
    entrada_cantidad.pack()
    
    ctk.CTkButton(ventana, text="Añadir Producto", command=lambda: agregar_producto_inventario(entrada_producto, categoria_var, entrada_precio, entrada_cantidad)).pack()
    ctk.CTkButton(ventana, text="Eliminar Producto", command=lambda: eliminar_producto(entrada_producto)).pack()
    ctk.CTkButton(ventana, text="Ver Inventario", command=mostrar_inventario).pack()
    
    ventana.mainloop()

# Crear ventana de empleados directamente para pruebas
crear_ventana_empleado()
