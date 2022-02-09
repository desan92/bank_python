CREATE DATABASE bank_python;

USE bank_python;

CREATE TABLE user_bank (
	id_usuari INT(11) AUTO_INCREMENT PRIMARY KEY,
	nom_usuari VARCHAR(30) NOT NULL,
	cognoms_usuari VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL UNIQUE,
	pass VARCHAR(30) NOT NULL,
	tlf_usuari VARCHAR(30) NOT NULL,
	email_usuari VARCHAR(30) NOT NULL,
    creat TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE compte_bank (
    id_compte INT(11) AUTO_INCREMENT PRIMARY KEY,
    nun_compte VARCHAR(30) NOT NULL,
    saldo DECIMAL(20, 2) NOT NULL,
	id_usuari INT(11),
    FOREIGN KEY (id_usuari) REFERENCES user_bank(id_usuari)
);

CREATE TABLE moviment_compte (
    id_moviment INT(11) AUTO_INCREMENT PRIMARY KEY,
    tipus_moviment VARCHAR(30) NOT NULL,
    import_diners DECIMAL(20, 2) NOT NULL,
    realitzacio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_compte INT(11),
    FOREIGN KEY (id_compte) REFERENCES compte_bank(id_compte)
);

CREATE TRIGGER t_movimentcompte_ai_001 AFTER INSERT ON moviment_compte FOR EACH ROW

BEGIN

	DECLARE saldo TYPE OF compte_bank.saldo;
	DECLARE import TYPE OF moviment_compte.import_diners;

	SET import = NEW.import_diners;

	SELECT saldo INTO saldo
	FROM compte_bank
	WHERE compte_bank.id_compte = NEW.id_compte;

	UPDATE compte_bank
	SET saldo = saldo + import
	WHERE compte_bank.id_compte = NEW.id_compte;

END

CREATE TRIGGER t_movimentcompte_bi_001 BEFORE INSERT ON moviment_compte FOR EACH ROW

BEGIN

	DECLARE saldo TYPE OF compte_bank.saldo;
	DECLARE import TYPE OF moviment_compte.import_diners;

	SET import = NEW.import_diners;

	SELECT saldo INTO saldo
	FROM compte_bank
	WHERE compte_bank.id_compte = NEW.id_compte;

	IF saldo < 0 THEN
	    SIGNAL SQLSTATE 'HY000'
		SET MESSAGE_TEXT = 'ERROR, EL SALDO NO POT SER INFERIOR A 0';

	ELSEIF import = 0 THEN
		SIGNAL SQLSTATE 'HY000'
		SET MESSAGE_TEXT = 'ERROR, IMPORT NO POT SER IGUAL A 0';

   END IF;

END

INSERT INTO `user_bank`(`nom_usuari`, `cognoms_usuari`, `username`, `pass`, `tlf_usuari`, `email_usuari`)
VALUES ("Jordi","de San Antonio Planas","DeSan","23011992","789678567","jordi.jordi@gmail.com")

INSERT INTO `compte_bank`(`nun_compte`, `saldo`, `id_usuari`)
VALUES ("ES23 1233 3213 23 0200051332",0,1)

INSERT INTO `moviment_compte`(`tipus_moviment`, `import_diners`, `id_compte`)
VALUES ("Pagament",-50,1)