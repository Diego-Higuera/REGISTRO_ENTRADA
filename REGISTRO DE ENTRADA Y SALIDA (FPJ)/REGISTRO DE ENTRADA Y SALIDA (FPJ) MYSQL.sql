#RRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEE        GGGGGGGGGGGGGIIIIIIIIII   SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTTRRRRRRRRRRRRRRRRR        OOOOOOOOO     
#R::::::::::::::::R  E::::::::::::::::::::E     GGG::::::::::::GI::::::::I SS:::::::::::::::ST:::::::::::::::::::::TR::::::::::::::::R     OO:::::::::OO   
#R::::::RRRRRR:::::R E::::::::::::::::::::E   GG:::::::::::::::GI::::::::IS:::::SSSSSS::::::ST:::::::::::::::::::::TR::::::RRRRRR:::::R  OO:::::::::::::OO 
#RR:::::R     R:::::REE::::::EEEEEEEEE::::E  G:::::GGGGGGGG::::GII::::::IIS:::::S     SSSSSSST:::::TT:::::::TT:::::TRR:::::R     R:::::RO:::::::OOO:::::::O
  #R::::R     R:::::R  E:::::E       EEEEEE G:::::G       GGGGGG  I::::I  S:::::S            TTTTTT  T:::::T  TTTTTT  R::::R     R:::::RO::::::O   O::::::O
  #R::::R     R:::::R  E:::::E             G:::::G                I::::I  S:::::S                    T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::RRRRRR:::::R   E::::::EEEEEEEEEE   G:::::G                I::::I   S::::SSSS                 T:::::T          R::::RRRRRR:::::R O:::::O     O:::::O
  #R:::::::::::::RR    E:::::::::::::::E   G:::::G    GGGGGGGGGG  I::::I    SS::::::SSSSS            T:::::T          R:::::::::::::RR  O:::::O     O:::::O
  #R::::RRRRRR:::::R   E:::::::::::::::E   G:::::G    G::::::::G  I::::I      SSS::::::::SS          T:::::T          R::::RRRRRR:::::R O:::::O     O:::::O
  #R::::R     R:::::R  E::::::EEEEEEEEEE   G:::::G    GGGGG::::G  I::::I         SSSSSS::::S         T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::R     R:::::R  E:::::E             G:::::G        G::::G  I::::I              S:::::S        T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::R     R:::::R  E:::::E       EEEEEE G:::::G       G::::G  I::::I              S:::::S        T:::::T          R::::R     R:::::RO::::::O   O::::::O
#RR:::::R     R:::::REE::::::EEEEEEEE:::::E  G:::::GGGGGGGG::::GII::::::IISSSSSSS     S:::::S      TT:::::::TT      RR:::::R     R:::::RO:::::::OOO:::::::O
#R::::::R     R:::::RE::::::::::::::::::::E   GG:::::::::::::::GI::::::::IS::::::SSSSSS:::::S      T:::::::::T      R::::::R     R:::::R OO:::::::::::::OO 
#R::::::R     R:::::RE::::::::::::::::::::E     GGG::::::GGG:::GI::::::::IS:::::::::::::::SS       T:::::::::T      R::::::R     R:::::R   OO:::::::::OO   
#RRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEE        GGGGGG   GGGGIIIIIIIIII SSSSSSSSSSSSSSS         TTTTTTTTTTT      RRRRRRRR     RRRRRRR     OOOOOOOOO     



#          ╔╦╗╔═╗  ╔═╗╔╗╔╔╦╗╦═╗╔═╗╔╦╗╔═╗  ╦ ╦  ╔═╗╔═╗╦  ╦╔╦╗╔═╗
#           ║║║╣   ║╣ ║║║ ║ ╠╦╝╠═╣ ║║╠═╣  ╚╦╝  ╚═╗╠═╣║  ║ ║║╠═╣
#          ═╩╝╚═╝  ╚═╝╝╚╝ ╩ ╩╚═╩ ╩═╩╝╩ ╩   ╩   ╚═╝╩ ╩╩═╝╩═╩╝╩ ╩
    
 







-------------------------------------------------------------------------------------------------------------------------------------------

DROP DATABASE IF EXISTS FPJ;
CREATE DATABASE FPJ;
USE FPJ;

-------------------------------------------------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS USUARIOS;
DROP TABLE IF EXISTS MOTIVOS;
DROP TABLE IF EXISTS REGISTROS;

-------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------ TABLA DE USUARIOS ------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE IF NOT EXISTS USUARIOS (
    DNI VARCHAR(15) PRIMARY KEY,
    NOMBRE_USUARIO VARCHAR(50) NOT NULL UNIQUE,
    CONTRASENA VARCHAR(100) NOT NULL
);


-------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------ TABLA DE MOTIVOS ------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE IF NOT EXISTS MOTIVOS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DESCRIPCION VARCHAR(50) NOT NULL
);


-------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------ TABLA DE REGISTROS -----------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE IF NOT EXISTS REGISTROS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE_USUARIO VARCHAR(50) NOT NULL,
    FICHAJE ENUM('ENTRADA', 'SALIDA') NOT NULL,
    MOTIVO_ID INT NOT NULL,
    FECHA_HORA DATETIME NOT NULL,
    FOREIGN KEY (NOMBRE_USUARIO) REFERENCES USUARIOS(NOMBRE_USUARIO),
    FOREIGN KEY (MOTIVO_ID) REFERENCES MOTIVOS(ID)
);





-------------------------------------------------------------------------------------------------------------------------------------------

   
SELECT * FROM USUARIOS;
SELECT * FROM MOTIVOS;
SELECT * FROM REGISTROS;

   
   


-------------------------------------------------------------------------------------------------------------------------------------------


 SELECT r.ID AS REGISTRO_ID,
               u.NOMBRE_USUARIO AS NOMBRE_USUARIO,
               r.FICHAJE AS TIPO_FICHAJE,
               m.DESCRIPCION AS MOTIVO,
              r.FECHA_HORA AS FECHA_HORA
        FROM REGISTROS r
	    JOIN USUARIOS u ON r.NOMBRE_USUARIO = u.NOMBRE_USUARIO
        JOIN MOTIVOS m ON r.MOTIVO_ID = m.ID;


-------------------------------------------------------------------------------------------------------------------------------------------










 