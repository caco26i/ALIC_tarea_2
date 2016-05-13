import gi
import sys
from gi.repository import Gtk
import numpy as np
import warnings
gi.require_version('Gtk', '3.0')



class App4:
    cantidad_vectores_app_1 = None
    # R2, R3, o R1
    cantidad_elementos_vector_app_1 = None
    orden_matriz_app_2 = None

    matriz_elementos_app_1 = None

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

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def boton_app_1_siguiente_1(self, button):
        App_1 = self.builder.get_object("App_1")
        combobox_tipo_vectores = self.builder.get_object("combobox_tipo_vectores")
        combobox_tipo_vectores_value = self.get_combo_value(combobox_tipo_vectores)
        combobox_cant_vectores = self.builder.get_object("combobox_cant_vectores")
        combobox_cant_vectores_value = self.get_combo_value(combobox_cant_vectores)
        print(combobox_tipo_vectores_value)
        print(combobox_cant_vectores_value)
        tipo_operacion = ""
        if combobox_tipo_vectores_value is not None and combobox_cant_vectores_value is not None:
            if combobox_cant_vectores_value != "W ∈ Gen = {U, V}":
                self.cantidad_vectores_app_1 = int(combobox_cant_vectores_value)
                tipo_operacion = "dependencia"
            else:
                self.cantidad_vectores_app_1 = 3
                tipo_operacion = "generado"

            if combobox_tipo_vectores_value == "R":
                self.cantidad_elementos_vector_app_1 = 1
            elif combobox_tipo_vectores_value == "R2":
                self.cantidad_elementos_vector_app_1 = 2
            elif combobox_tipo_vectores_value == "R3":
                self.cantidad_elementos_vector_app_1 = 3
            for i in range(0, 5):
                vector = self.builder.get_object("hbox_vector_"+str(i+1))
                vector_visible = i+1 <= self.cantidad_vectores_app_1
                vector.set_visible(vector_visible)
                if vector_visible:
                    for j in range(0, 3):
                        field_visible = j+1 <= self.cantidad_elementos_vector_app_1

                        if i < 3 and j <= self.cantidad_elementos_vector_app_1: #para ocultar los campos de la ventana de pertence al generado
                            field_pertenece_gen = self.builder.get_object("entry_v_"+str(i)+"_"+str(j))
                            field_pertenece_gen.set_visible(field_visible)

                        field = self.builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
                        field.set_visible(field_visible)
            if tipo_operacion == "generado":
                App_1.set_current_page(2)
            else:
                App_1.set_current_page(1)

    def calcular_dependencia(self, button):
        """
        Con esta funcion se valida la tabla y lo siguiente de la app 1
        :param button:
        """

        App_1 = self.builder.get_object("App_1")
        matriz_elementos = []
        if self.cantidad_vectores_app_1 is not None and self.cantidad_elementos_vector_app_1 is not None:
            print("Entro al if")
            isValid = True
            for i in range(0, self.cantidad_vectores_app_1):
                temp_list = []
                for j in range(0, self.cantidad_elementos_vector_app_1):
                    field = self.builder.get_object("entry_vector_"+str(i+1)+"_"+str(j+1))
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
                    label_result = self.builder.get_object("label_result_app1")
                    label_result.set_text("Es Linealmente Independiente")
                else:
                    label_result = self.builder.get_object("label_result_app1")
                    label_result.set_text("Es Linealmente Dependiente")
                print(resultado_li)
                App_1.next_page()

    def generar_base(self, button):
        App_1 = self.builder.get_object("App_1")

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

        label_result = self.builder.get_object("label_base_app_1")
        print(len(matriz_base) )
        print(self.cantidad_elementos_vector_app_1)
        if len(matriz_base) >= self.cantidad_elementos_vector_app_1:
            label_result.set_text(str(matriz_base))
        else:
            label_result.set_text("No se puede generar una base con los siguientes vectores \n" + str(self.matriz_elementos_app_1))

        App_1.next_page()

    def calcular_pertenece_generado(self, button):
        App_1 = self.builder.get_object("App_1")
        matriz_elementos = []
        if True:
            print("Entro al if")
            isValid = True
            for i in range(0, 3):
                temp_list = []
                for j in range(0, self.cantidad_elementos_vector_app_1):
                    field = self.builder.get_object("entry_v_"+str(i)+"_"+str(j))
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

                print("entro al isValid")
                print(matriz_elementos)
                matrix_u_v = [matriz_elementos[0], matriz_elementos[1]]
                print("matrix_u_v")
                print(matrix_u_v)

                temp_matrix = np.array(matrix_u_v)
                temp_matrix = temp_matrix.T

                print("matrix_u_v T")
                print(temp_matrix)
                print(self.cantidad_elementos_vector_app_1)

                b = np.array(matriz_elementos[2])
                resultado_li = np.linalg.lstsq(temp_matrix, b)

                print("resultado!")
                print(resultado_li)
                # indica si es LI o LD

                is_generado = resultado_li[2] == len(temp_matrix[0])

                label_result = self.builder.get_object("label_base_app_1")
                if is_generado:
                    label_result.set_text("W SÍ ES GENERADO POR GEN(U,V)")
                    print("SI ES GENERADO")

                else:
                    label_result.set_text("W NO ES GENERADO POR GEN(U,V)")
                    print("NO ES GENERADO")

                App_1.set_current_page(4)

    #APP 2
        
    def boton_app_2_llenar_matriz(self, button):
        App_2 = self.builder.get_object("App_2")
        combobox_cant_vectores1 = self.builder.get_object("combobox_cant_vectores1")
        combobox_cant_vectores1_value = self.get_combo_value(combobox_cant_vectores1)
        print(combobox_cant_vectores1_value)
        if combobox_cant_vectores1_value is not None:
            print("Entro al if")
            self.orden_matriz_app_2 = combobox_cant_vectores1_value
            for i in range(0, 5):
                for j in range(0, 5):
                    field = self.builder.get_object("entry_matrix_" + str(i) + "_" + str(j))
                    field_visible = j < self.orden_matriz_app_2 and i < self.orden_matriz_app_2
                    field.set_visible(field_visible)
            App_2.next_page()
    def calcular_LU(self, button):
        isValid = True
        matriz_elementos = []
        for i in range (0, self.orden_matriz_app_2):
            temp_list = []
            for j in range (0, self.orden_matriz_app_2):
                field = self.builder.get_object("entry_matrix_"+str(i)+"_"+str(j))
                if field.get_text().lstrip('-').isdigit():
                    value_field = float(field.get_text())
                    temp_list.append(value_field)
                else:
                    isValid = False
                    break
            if not isValid:
                break
            matriz_elementos.append(temp_list)

        label = self.builder.get_object("label_base_app_2")
        if isValid:            
            try:
                L, U = lu(np.array(matriz_elementos))
                label.set_text(str(L) + "  " + str(U))
            except ValueError:
                label.set_text('No tiene inversa')

    def luEquation(A, b):
        L, U = lu(A)
        #Primero se resuelve Ly = b
        y = np.linalg.solve(L, b)
        #Despues se resuleve Ux = y
        x = np.linalg.solve(U, y)
        return x

    def luInverse(A):
        L, U = lu(A)
        # Primero se resuelve la inversa de L
        LInv = np.linalg.inv(L)

        # Despues se resuelve la invers de U
        UInv = np.linalg.inv(U)

        # Al final se multiplican ambas inversas para resolver A inverso
        AInv = np.dot(LInv, UInv)

        return AInv, LInv, UInv

    def open_first_page(self, button):
        notebook.set_current_page(0)

    #GETTERS AND SETTERS
    def get_combo_value(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter != None:
            model = combo.get_model()
            return model[tree_iter][0]


warnings.filterwarnings('error')


def lu(A):
    n = A.shape[0]     # Orden de la matriz
    L = np.zeros((n,n),dtype='float64')
    U = np.zeros((n,n),dtype='float64')
    U[:] = A
    np.fill_diagonal(L,1) #LLena la diagonal L con 1

    #Si U[j,i]/U[i,i] es division de 0, no tiene factorizacion
    #se ejecuta el except

    try:

        for i in range(n-1):
            for j in range(i+1,n):
                L[j,i] = U[j,i]/U[i,i]
                U[j,i:] = U[j,i:]-L[j,i]*U[i,i:]
                U[j,i] = 0
            # pprint.pprint(L)
            # pprint.pprint(U)

        return (L,U)

    except Warning:

        return "No tiene inversa"

if __name__ == "__main__":
    main = App4()
    Gtk.main()



