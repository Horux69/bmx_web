class ConsultaAnonima:
    def __init__(self, miDB):
        self.mysql = miDB
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()

    def consulta(self, cedula):
        consulta = f"SELECT num_documento FROM clientes WHERE num_documento = '{cedula}'"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado