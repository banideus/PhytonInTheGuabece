#clasesObjetos
# class MyClase:
#     pass


class MixinData(object):
    def __init__(
     self,
     user="anonimo",
     password="patito",
     port="1234",
     host="localhost",
     db="sqlite3"):

     self.user = user
     self.password = password
     self.port = property
     self.host = host
     self.db = db

    def get_username(self):
        return self.user

    def get_password(self):
        return self.password

    def get_port(self):
        return self.port

    def get_host(self):
        return self.host

    def get_db(self):
        return self.db

usuario = str(input("Nombre de usuario? :__"))
password = str(input("Password? :__"))

obj =MixinData(password=password, user=usuario)

print(obj.user)
print(obj.password)

print(obj.get_username())
print(obj.get_password())

user=obj.get_username()

print(user*10)
