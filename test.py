#import numpy as np
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:

    cantidad_vectores_app_1 = None
    cantidad_elementos_vector_app_1 = None

    def app_1_1_siguiente(self, button):
        print("siguiente")

        notebook_app_1 = builder.get_object("notebook_app_1")
        
        combobox_tipo_vector = builder.get_object("combobox_tipo_vector")
        combobox_tipo_vector_value = self.get_combo_value(combobox_tipo_vector)

        combobox_cantidad_vectores = builder.get_object("combobox_cantidad_vectores")
        combobox_cantidad_vectores_value = self.get_combo_value(combobox_cantidad_vectores)

        print(combobox_tipo_vector_value)
        print(combobox_cantidad_vectores_value)

        if combobox_tipo_vector_value is not None and combobox_cantidad_vectores_value is not None:
            self.cantidad_vectores_app_1 = combobox_cantidad_vectores_value
            if combobox_tipo_vector_value == "R":
                self.cantidad_elementos_vector_app_1 = 1
            elif combobox_tipo_vector_value == "R2":
                self.cantidad_elementos_vector_app_1 = 2
            elif combobox_tipo_vector_value == "R3":
                self.cantidad_elementos_vector_app_1 = 3

            for i in range(0, 5):
                vector = builder.get_object("hbox_vector_"+str(i+1))
                vector_visible = i+1 <= self.cantidad_vectores_app_1
                vector.set_visible(vector_visible);
                if vector_visible:
                    for j in range(0, 3):
                        field = builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
                        field_visible = j+1 <= self.cantidad_elementos_vector_app_1
                        field.set_visible(field_visible);

            notebook_app_1.next_page()

    def app_1_2_siguiente(self, button):
        print("siguiente")

        notebook_app_1 = builder.get_object("notebook_app_1")

        matriz_elementos = []

        if self.cantidad_vectores_app_1 is not None and self.cantidad_elementos_vector_app_1 is not None:
            for i in range(0, self.cantidad_vectores_app_1):
                temp_list = []
                for j in range(0, self.cantidad_elementos_vector_app_1):
                    field = builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
                    value_field = int(field.get_text())
                    temp_list.append(value_field)

                matriz_elementos.append(temp_list)

            print(matriz_elementos)
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
