from alumnos import *

def main():

    alumno1 = Alumno("Neithan", 10,[5.0,4.0,3.0,3.2])
    alumno2 = Alumno("Esteban", 13,[5.0,4.0,4.0,4.0])
    alumno3 = Alumno("Phol", 12, [4.0,5.0,5.0,2.0])
    alumno4 = Alumno("Bobolon", 12, [1.0,3.0,2.0,2.0])

    print("Promedio de notas de alumno: ", alumno1.promedio())
    print("Nota mayor del alumno", alumno1.nota_mayor())
    print("Nota menor del alumno", alumno1.nota_menor())
    
    alumnos = [alumno1, alumno2, alumno3, alumno4]

    print("Los mejores 3 estudiantes son: ", mejores_alumnos(alumnos))

if __name__ == "__main__":
    main()