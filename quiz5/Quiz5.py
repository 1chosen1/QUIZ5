import doctest
import unittest
import csv


def agregar():
    nombre = input("Ingrese Nombre: ")
    edad = int(input("Ingrese su Edad: "))
    guardar(nombre, edad)

def guardar(nombre, edad):
    f=open("Datos.csv", "a+", newline='')
    c= csv.writer(f)
    c.writerow([nombre, edad])
    f.close()
    return True

#agregar()

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(guardar("nome", 2))
		
if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    doctest.testmod()
