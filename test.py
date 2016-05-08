import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

    def app_1_1_siguiente(self, button):
        print("siguiente ")
        builder.get_object(name)

builder = Gtk.Builder()
builder.add_from_file("example.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()
