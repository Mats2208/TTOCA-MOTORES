from mi_queue import Queue

class Turno:
    def __init__(self, name=""):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"Nombre: {self.name}"

class ColaTurnos:
    def __init__(self):
        self.cola = Queue()

    def agregar_turno(self, turno):
        self.cola.push(turno)
        print("Turno agregado:", turno)

    def atender_turno(self):
        success, turno = self.cola.pop()
        if success:
            print("Atendiendo:", turno)
        else:
            print("No hay turnos por atender.")

    def ver_turno(self):
        success, turno = self.cola.peek()
        if success:
            print("Turno actual:", turno)
        else:
            print("No hay turnos esperando.")

    def mostrar(self):
        print("Cola actual:")
        self.cola.print()

    def esta_vacia(self):
        return self.cola.is_empty()

    def cantidad_turnos(self):
        return self.cola.get_size()
