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
        notebook_app_1 = builder.get_object("notebook_app_1")
        
        combobox_tipo_vector = builder.get_object("combobox_tipo_vector")
        combobox_tipo_vector_value = self.get_combo_value(combobox_tipo_vector)

        combobox_cantidad_vectores = builder.get_object("combobox_cantidad_vectores")
        combobox_cantidad_vectores_value = self.get_combo_value(combobox_cantidad_vectores)

        print(combobox_tipo_vector_value)
        print(combobox_cantidad_vectores_value)

        notebook_app_1.next_page()

    ##############################
    #    GETTERS AND SETTERS
    ##############################
    def get_combo_value(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            return model[tree_iter][0]

        
builder = Gtk.Builder()
builder.add_from_file("example.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()
