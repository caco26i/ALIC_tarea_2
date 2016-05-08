import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

    def home_siguiente(self, tabla):
        print("siguiente " + tabla)

builder = Gtk.Builder()
builder.add_from_file("example.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()
