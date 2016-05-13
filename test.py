from gi.repository import Gtk
import numpy as np
import gi
gi.require_version('Gtk', '3.0')

class Handler:
    cantidad_vectores_app_1 = None
    # R2, R3, o R1
    cantidad_elementos_vector_app_1 = None
    orden_matriz_app_2 = None

    matriz_elementos_app_1 = None

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def app_1_1_siguiente(self, button):
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
                vector.set_visible(vector_visible)
                if vector_visible:
                    for j in range(0, 3):
                        field = builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
                        field_visible = j+1 <= self.cantidad_elementos_vector_app_1
                        field.set_visible(field_visible)
            notebook_app_1.next_page()

    def app_1_2_siguiente(self, button):
        """
        Con esta funcion se valida la tabla y lo siguiente de la app 1
        :param button:
        """

        notebook_app_1 = builder.get_object("notebook_app_1")
        matriz_elementos = []
        if self.cantidad_vectores_app_1 is not None and self.cantidad_elementos_vector_app_1 is not None:
            print("Entro al if")
            isValid = True
            for i in range(0, self.cantidad_vectores_app_1):
                temp_list = []
                for j in range(0, self.cantidad_elementos_vector_app_1):
                    field = builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
                    if field.get_text().lstrip('-').isdigit():
                        value_field = float(field.get_text())
                        temp_list.append(value_field)
                    else:
                        isValid = False
                        break
                if not isValid:
                    break
                matriz_elementos.append(temp_list)
            if isValid:
                self.matriz_elementos_app_1 = matriz_elementos

                print("entro al isValid")
                print(matriz_elementos)
                temp_matrix = np.array(matriz_elementos)
                temp_matrix = temp_matrix.T
                print(self.cantidad_elementos_vector_app_1)

                b = np.array([0] * self.cantidad_elementos_vector_app_1)
                resultado_li = np.linalg.lstsq(temp_matrix, b)

                print("resultado!")
                print(resultado_li)
                # indica si es LI o LD
                isLinear = True
                if resultado_li[2] != len(temp_matrix[0]):
                    isLinear = False
                else:
                    isLinear = True
                for i in range(len(resultado_li[0])):
                    if resultado_li[0][i] != 0:
                        isLinear = False
                        break
                if isLinear:
                    label_result = builder.get_object("label_result_app1")
                    label_result.set_text("Es Linealmente Independiente")
                else:
                    label_result = builder.get_object("label_result_app1")
                    label_result.set_text("Es Linealmente Dependiente")
                print(resultado_li)
                notebook_app_1.next_page()

    def app_1_3_generar_base(self, button):
        notebook_app_1 = builder.get_object("notebook_app_1")

        matriz_base = []

        b = np.array([0] * self.cantidad_elementos_vector_app_1)

        for i in range(0, self.cantidad_vectores_app_1):
            matriz_base = [self.matriz_elementos_app_1[i]]
            for j in range(0, self.cantidad_vectores_app_1):
                if i != j:
                    temp_matrix = matriz_base + [self.matriz_elementos_app_1[j]]
                    print (temp_matrix)
                    temp_matrix = np.array(temp_matrix)
                    temp_matrix = temp_matrix.T

                    resultado_li = np.linalg.lstsq(temp_matrix, b)

                    # indica si es LI o LD
                    isLI = True
                    if resultado_li[2] != len(temp_matrix[0]):
                        isLI = False
                    else:
                        isLI = True
                    for i in range(len(resultado_li[0])):
                        if resultado_li[0][i] != 0:
                            isLI = False
                            break

                    print(len(matriz_base) )
                    print(self.cantidad_elementos_vector_app_1)
                    if isLI:
                        print("isLI")
                        matriz_base = matriz_base + [self.matriz_elementos_app_1[j]]

                    if len(matriz_base) >= self.cantidad_elementos_vector_app_1:
                        print("len(matriz_base) >= self.cantidad_elementos_vector_app_1:")
                        break
            print("salio del for 2")
            if len(matriz_base) >= self.cantidad_elementos_vector_app_1:
                print("for 1 len(matriz_base) >= self.cantidad_elementos_vector_app_1:")
                if isLI:
                    print("for 1 isLI")
                    break

        label_result = builder.get_object("label_base_app_1")
        print(len(matriz_base) )
        print(self.cantidad_elementos_vector_app_1)
        if len(matriz_base) >= self.cantidad_elementos_vector_app_1:
            label_result.set_text(str(matriz_base))
        else:
            label_result.set_text("No se puede generar una base con los siguientes vectores \n" + str(self.matriz_elementos_app_1))

        notebook_app_1.next_page()

    def open_first_page(self, notebook):
        notebook.set_current_page(0)

    def app_2_1_llenar_matriz(self, button):
        notebook_app_2 = builder.get_object("notebook_app_2")
        combobox_orden_matriz = builder.get_object("combobox_orden_matriz")
        combobox_orden_matriz_value = self.get_combo_value(combobox_orden_matriz)
        print(combobox_orden_matriz_value)
        if combobox_orden_matriz_value is not None:
            print("Entro al if")
            self.orden_matriz_app_2 = combobox_orden_matriz_value
            for i in range(0, 5):
                for j in range(0, 5):
                    field = builder.get_object("entry_matrix_" + str(i) + "_" + str(j))
                    field_visible = j < self.orden_matriz_app_2 and i < self.orden_matriz_app_2
                    field.set_visible(field_visible)
            notebook_app_2.next_page()

    #GETTERS AND SETTERS
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
