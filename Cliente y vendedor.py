class Cliente:
    def __init__(self, codigo=None, nombre=None, telefono=None, direccion=None,
                 email=None, ocupacion=None, preferencia=None, estado_civil=None,
                 cedula=None, presupuesto=None):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.ocupacion = ocupacion
        self.preferencia = preferencia
        self.estado_civil = estado_civil
        self.cedula = cedula
        self.presupuesto = presupuesto

    def __str__(self):
        return f"Cliente: {self.nombre} (Código: {self.codigo})"

    # Uso de @property para getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor


class Vendedor:
    def __init__(self, codigo=None, nombre=None, direccion=None, horario=None,
                 email=None, experiencia=None, telefono=None, cargo=None,
                 departamento=None, fecha_ingreso=None):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        self.email = email
        self.experiencia = experiencia
        self.telefono = telefono
        self.cargo = cargo
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso

    def __str__(self):
        return f"Vendedor: {self.nombre} (Código: {self.codigo})"

    # Uso de @property para getters y setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente(
        codigo="C001",
        nombre="William velez",
        telefono="555-1234",
        direccion="Calle Principal 123",
        email="William@example.com",
        ocupacion="Ingeniero",
        preferencia="Tecnología",
        estado_civil="Casado",
        cedula="1234567890",
        presupuesto=5000
    )

    # Crear un vendedor
    vendedor1 = Vendedor(
        codigo="V001",
        nombre="Liam Payne",
        direccion="Av. Comercial 456",
        horario="9:00 - 18:00",
        email="Liam@company.com",
        experiencia="5 años",
        telefono="555-5678",
        cargo="Supervisor de Ventas",
        departamento="Electrónica",
        fecha_ingreso="2020-01-15"
    )

    print(cliente1)
    print(vendedor1)