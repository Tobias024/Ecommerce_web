-- Crear tabla Roles
CREATE TABLE Roles (
    rol_id INT PRIMARY KEY,
    nombre_rol VARCHAR(50)
);

-- Insertar datos en tabla Roles
INSERT INTO Roles (rol_id, nombre_rol) 
VALUES 
    (1, 'manager'),
    (2, 'empleado'),
    (3, 'cliente');

-- Crear tabla Usuarios
CREATE TABLE Usuarios (
    uuid INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    clave CHAR(6), -- Cambiado a CHAR(6)
    direccion VARCHAR(100),
    telefono VARCHAR(15),
    mail AS CONCAT(nombre, apellido, '@uade.com'),
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES Roles(rol_id)
);

-- Insertar datos en tabla Usuarios
-- Asegúrate de que los valores de 'uuid' existen en la tabla 'Usuarios' antes de insertarlos en la tabla 'Pagos'
INSERT INTO Usuarios (uuid, nombre, apellido, clave, direccion, telefono, rol_id) 
VALUES 
    -- Managers
    (2,'Juan', 'Perez', 'abcde', 'Av. Rivadavia 123', '123456789', 1),
    (4,'Maria', 'Gomez', '12345', 'Calle 123', '987654321', 1),
    (6,'Pedro', 'Lopez', 'qwerty', 'Av. Corrientes 456', '456789123', 1),
    -- Empleados
    (8,'Carlos', 'Martinez', 'asdfg', 'Av. Callao 789', '321654987', 2),
    (10,'Laura', 'Rodriguez', 'zxcvb', 'Av. Santa Fe 456', '654987321', 2),
    (12,'Roberto', 'Diaz', '12345', 'Calle 456', '789123654', 2),
    (14,'Ana', 'Sanchez', 'qwerty', 'Av. Cordoba 789', '987321654', 2),
    -- Clientes
    (1,'Jorge', 'Garcia', 'qwerty', 'Av. Libertador 123', '654789123', 3),
    (3,'Valentina', 'Martinez', 'zxcvb', 'Av. 9 de Julio 456', '789123654', 3),
    (5,'Raul', 'Lopez', '12345', 'Av. Corrientes 789', '321654987', 3),
    (7,'Marta', 'Fernandez', 'asdfg', 'Av. Callao 123', '987321654', 3),
    (9,'Lucas', 'Sanchez', 'qwerty', 'Calle 123', '147258369', 3),
    (11,'Camila', 'Gutierrez', 'zxcvb', 'Av. Rivadavia 456', '369147258', 3),
    (13,'Julia', 'Diaz', '12345', 'Av. Cordoba 123', '258369147', 3),
    (15,'Gaston', 'Rodriguez', 'asdfg', 'Av. Santa Fe 789', '654789123', 3),
    (17,'Luis', 'Gomez', 'qwerty', 'Av. Belgrano 456', '789123654', 3),
    (19,'Natalia', 'Perez', 'zxcvb', 'Av. 9 de Julio 789', '321654987', 3);

-- Crear tabla Pagos
CREATE TABLE Pagos (
    pago_id INT PRIMARY KEY,
    monto DECIMAL(10, 2),
    fecha DATE,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(uuid)
);

-- Insertar datos en tabla Pagos
-- Asegúrate de que los valores de 'usuario_id' existen en la tabla 'Usuarios'
INSERT INTO Pagos (pago_id, monto, fecha, usuario_id)
VALUES
    (1, 150.50, '2024-02-15', 1),
    (2, 200.75, '2024-02-16', 3),
    (3, 75.20, '2024-02-17', 5),
    (4, 300.00, '2024-02-18', 7),
    (5, 120.00, '2024-02-19', 9),
    (6, 80.50, '2024-02-20', 11),
    (7, 250.25, '2024-02-21', 13),
    (8, 180.30, '2024-02-22', 15),
    (9, 90.00, '2024-02-23', 17),
    (10, 350.75, '2024-02-24', 19);
