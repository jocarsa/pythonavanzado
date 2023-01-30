CREATE TABLE 
articulos
(
    Identificador INT(255) NOT NULL AUTO_INCREMENT , 
    titulo VARCHAR(255) NOT NULL , 
    contenido TEXT NOT NULL , 
    imagen VARCHAR(255) NOT NULL , 
    fecha VARCHAR(255) NOT NULL , 
    PRIMARY KEY (`Identificador`)
) ENGINE = InnoDB;