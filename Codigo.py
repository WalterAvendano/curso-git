import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root', password='Walugeso01+',
                                               host='127.0.0.1', database= 'clientesdb',
                                               port='3306')
            print("Conexion realizada")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectarse a la Base de Datos original {}".format(error))
            return conexion
    ConexionBaseDeDatos()