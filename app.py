import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import tkinter

def on_activate(app):

    # Creamos una ventana
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("Gestión de mi ordenador") # App name
    win.set_default_size(500, 300)

    # Creamos un botón con el texto "Hola Mundo"
    btn = Gtk.Button(label="Hello World")
    btn.set_margin_top(20)
    btn.set_margin_bottom(20)
    
    # Al cerrar la ventana, se termina la app
    win.set_child(btn)
    win.present()

app = Gtk.Application(application_id="com.ejemplo.HolaMundo")
app.connect("activate", on_activate)
app.run(None)