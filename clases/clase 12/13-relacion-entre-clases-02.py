# Define la clase Sueldo
class Sueldo:

    # Método constructor de la clase Sueldo
    def __init__(self, sueldo):
        self.sueldo = sueldo  # Inicializa el atributo sueldo

    # Método para representación en string de la clase Sueldo
    def __str__(self):
        return f"\nSUELDO: {self.sueldo}"  # Devuelve una cadena representando el objeto Sueldo

    # Define la clase anidada Empleado dentro de la clase Sueldo
    class Empleado:

        # Método constructor de la clase Empleado
        def __init__(self, nombre, puesto):
            self.nombre = nombre  # Inicializa el atributo nombre
            self.puesto = puesto  # Inicializa el atributo puesto
            self.sueldo = Sueldo(1200)  # Inicializa el atributo sueldo con un objeto Sueldo de valor 1200

        # Método para representación en string de la clase Empleado
        def __str__(self):
            return f"NOMBRE: {self.nombre}\nPUESTO: {self.puesto}\n" + self.sueldo.__str__()
            # Devuelve una cadena representando el objeto Empleado, incluyendo su nombre, puesto y sueldo

# Crea una instancia de la clase Sueldo con un sueldo de 200
s1 = Sueldo(200)

# Crea una instancia de la clase Empleado (dentro de Sueldo) con nombre "Nico" y puesto "Profe"
emp1 = Sueldo.Empleado("Nico", "Profe")

# Imprime el resultado de la representación en string del objeto s1 de la clase Sueldo
print("RESULTADO 1:" + s1.__str__())

# Imprime el resultado de la representación en string del objeto emp1 de la clase Empleado
print("RESULTADO 2:" + emp1.__str__())

#otra alternativa
# print(f"RESULTADO 1:  {s1}\n")
# print(f"RESULTADO 2:  {emp1}")


# RESULTADO 1:
# SUELDO: 200

# RESULTADO 2:  NOMBRE: Nico
# PUESTO: Profe

# SUELDO: 1200