"""
Registro de docentes
"""
#Definir la clase docente, 
class Docente:
    def __init__(self,nombre,apellido,edad):
        #Definir las variables que se van a guardar
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
#Definir clase docente personal academico
class DocentePersonalAcademico:
    def __init__(self,rol,departamento,salario):
        #Definir las variables que se van a guardar
        self.rol=rol
        self.departamento=departamento
        self.salario=salario

#Llenamos las variables del Docente mediante teclado    
nombre = str(input("Ingrese su Nombre: "))
apellido = str(input("Ingrese su Apellido: "))
edad = int(input("Ingresa su Edad: "))

#Llenamos las variables del Docente Personal Academico mediante teclado
rol = str(input("Ingrese su Rol en la Institucion: "))
departamento = str(input("Ingrese El Departamento: "))
salario = float(input("Ingrese su Salario: "))

#Imprimimos todos los datos recogidos
print ("====================================================================")
print ("\n\t",nombre,"\n\t",apellido,"\n\t",edad,"\n\t",rol,"\n\t",departamento,"\n\t",salario)
print ("====================================================================")
