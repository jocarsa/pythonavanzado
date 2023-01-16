CREATE TABLE 
curso.productos 
(
    Identificador INT(255) NOT NULL AUTO_INCREMENT , 
    titulo VARCHAR(100) NOT NULL , 
    descripcion VARCHAR(255) NOT NULL , 
    precio DECIMAL(5,2) NOT NULL , 
    imagen VARCHAR(100) NOT NULL ,
    stock INT(10) NOT NULL , 
    PRIMARY KEY (`Identificador`)
) ENGINE = InnoDB;