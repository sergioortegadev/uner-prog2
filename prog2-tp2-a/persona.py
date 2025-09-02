class Persona:
   def __init__(self, name, lastname):
      self.name = name
      self.lastname = lastname


   def establecerNombres(self, name):
      self.name = name

   def establecerApellido(self, lastname):
      self.lastname = lastname

   def establecerGrupoSanguineo(self, grupo):
      self.grupoSanguineo = grupo

   def establecerAltura(self, altura):
      self.altura = altura

   def obtenerNombre(self):
      return self.name
   
   def obtenerApellido(self):
      return self.lastname
   
   def obtenerNombreCompleto(self):
      return f'{self.lastname}, {self.name}'
   
   def obtenerGrupoSanguineo(self):
      return self.grupoSanguineo
   
   def obtenerAltura(self):
      return self.altura
   
   