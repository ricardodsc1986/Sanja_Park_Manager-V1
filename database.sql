
CREATE DATABASE estacionamento;

USE estacionamento;

CREATE TABLE registros_veiculos (
    placa VARCHAR(7) PRIMARY KEY,
    entrada DATETIME,
    saida DATETIME
);

INSERT INTO registros_veiculos (placa, entrada) VALUES
('ABC1234', '2025-02-17 08:00:00'),
('XYZ5678', '2025-02-17 09:00:00');

ALTER USER 'root'@'localhost:5000' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
    