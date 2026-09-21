import gi
import sys

gi.request_version("Gtk", "4.0")
from gi.repository import Glib, Gkt

def create_window(app):
    window = Gtk.ApplicationWindow(application=app, title="Hello, World!")
    return window

def on_activate(app):
    window = create_window(app)
    window.present()

def main():
    Glib.set_application_name("My Gtk application")

    app = Gtk.application(application_id="com.example.MyGtkApplication")

    app.connect("activate", on_activate)

    return app.run(sys.argv)

if __name__ == "__main__":
    main()
