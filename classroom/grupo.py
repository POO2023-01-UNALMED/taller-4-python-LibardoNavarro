from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        if estudiantes == None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes == None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            _lista = []
        else:
            _lista = lista
        _lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + _lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
