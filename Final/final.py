import gi
import sys
from gi.repository import Gtk
import numpy as np
gi.require_version('Gtk', '3.0')


class App4:
    def __init__(self):
        self.glade_file = "view.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.glade_file)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("main_window")
        self.window.show_all()

    def on_window_destroy(self, object, data=None):
        print("quit with cancel")
        Gtk.main_quit()
        sys.exit(0)


if __name__ == "__main__":
    main = App4()
    Gtk.main()



