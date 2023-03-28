from alumnos import *

def main():

    alumno1 = Alumno("Neithan", 10,[5.0,4.0,3.0])
    print(alumno1.promedio())
    print(alumno1.nota_mayor())
    print(alumno1.nota_menor())

if __name__ == "__main__":
    main()