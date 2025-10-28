class Cliente:

    def __init__(self, numero_id, nombres, apellidos, mail):
      self.__numero_id = numero_id
      self.__nombres = nombres
      self.__apellidos = apellidos
      self.__email = mail

    def establecerNumeroId(self, numero_id):
       self.__numero_id = numero_id

    def establecerNombres(self, nombres):
       self.__nombres = nombres

    def establecerApellidos(self, apellidos):
       self.__apellidos = apellidos

    def establecerEmail(self, mail):
       self.__email = mail

    def obtenerNumeroId(self):
       return self.__numero_id
    
    def obtenerNombres(self):
       return self.__nombres
    
    def obtenerApellidos(self):
       return self.__apellidos
    
    def obtenerEmail(self):
       return self.__email

    def __eq__(self, value):
       if isinstance(value, Cliente):
          return self.__numero_id == value.obtenerNumeroId()
       else: NotImplemented
    
    def __str__(self):
       return f'Cliente Id: {self.__numero_id} -Apellido y Nombres: {self.__apellidos}, {self.__nombres} - Email: {self.__email}\n'