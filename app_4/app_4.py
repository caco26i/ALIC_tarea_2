import gi
import sys
from gi.repository import Gtk
import numpy as np
gi.require_version('Gtk', '3.0')


class App4:
    def __init__(self):
        self.glade_file = "view_app_4.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("main_window")

        self.window.show_all()

    def on_window_destroy(self, object, data=None):
        print("quit with cancel")
        Gtk.main_quit()
        sys.exit(0)

    def next_button_1(self, button):
        notebook_app = self.builder.get_object("notebook1")
        combobox_orden = self.builder.get_object("combobox1")
        orden_value = button.get_combo_value(combobox_orden)
        print(orden_value)

if __name__ == "__main__":
    main = App4()
    Gtk.main()



