import pymysql


class Db:
    def __init__(self):
        self.connexio = pymysql.connect(
            host="localhost",
            user="usuari",
            password="password",
            db="bank_python"
        )

        self.cursor = self.connexio.cursor()

    # SELECT
    def SelectUser(self, user):
        SQL = "SELECT count(username) FROM user_bank WHERE username = '{}';".format(user)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectLog(self, user, password):
        SQL = "SELECT * FROM user_bank WHERE username = '{}' AND pass = '{}';".format(user, password)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectInfoUser(self, user):
        SQL = "SELECT * FROM user_bank WHERE username = '{}';".format(user)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectUserPass(self, user, password):
        SQL = "SELECT COUNT(*) FROM user_bank WHERE username = '{}' AND pass = '{}';".format(user, password)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectId(self, user):
        SQL = "SELECT id_usuari FROM user_bank WHERE username = '{}';".format(user)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectCompte(self, id_compte):
        SQL = "SELECT * FROM compte_bank WHERE id_usuari = '{}';".format(id_compte)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectCompte2(self, nun_compte):
        SQL = "SELECT id_compte FROM compte_bank WHERE nun_compte = '{}';".format(nun_compte)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectCompte3(self, nun):
        SQL = "SELECT id_compte FROM `compte_bank` WHERE nun_compte = '{}';".format(nun)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectNumCompte(self):
        SQL = "SELECT MAX(`nun_compte`) FROM `compte_bank`;"
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    def SelectMoviment(self, id):
        SQL = "SELECT mc.*, cb.saldo FROM moviment_compte mc LEFT JOIN compte_bank cb ON mc.id_compte = cb.id_compte " \
              "WHERE mc.id_compte = '{}';".format(id)
        self.cursor.execute(SQL)
        return self.cursor.fetchall()

    #INSERT
    def InsertUser(self, element):
        SQL = "INSERT INTO `user_bank`(`nom_usuari`, `cognoms_usuari`, `username`, `pass`, `tlf_usuari`, `email_usuari`) " \
              "VALUES('{}', '{}', '{}', '{}', '{}', '{}');".format(element[0], element[1], element[2], element[3], element[4], element[5])
        self.cursor.execute(SQL)
        self.connexio.commit()

    def InsertCompte(self, nun, id):
        SQL = "INSERT INTO `compte_bank`(`nun_compte`, `id_usuari`) " \
              "VALUES('{}', '{}');".format(nun, id)
        self.cursor.execute(SQL)
        self.connexio.commit()

    def InsertMoviment(self, a, b, c):
        SQL = "INSERT INTO `moviment_compte`(`tipus_moviment`, `import_diners`, `id_compte`) " \
              "VALUES('{}', '{}', '{}');".format(a, b, c)
        self.cursor.execute(SQL)
        self.connexio.commit()

    #UPDATE
    def UpdateUser(self, element, id):
        SQL = "UPDATE user_bank SET `nom_usuari`='{}', `cognoms_usuari`='{}', `username`='{}', " \
              "`pass`='{}', `tlf_usuari`='{}', `email_usuari`='{}' WHERE id_usuari = '{}'".format(element[0], element[1], element[2], element[3], element[4], element[5], id)
        self.cursor.execute(SQL)
        self.connexio.commit()
