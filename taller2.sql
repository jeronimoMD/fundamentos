SELECT * FROM cliente nombre
SELECT *FROM pedidos nombre_cliente
SELECT * FROM detalles_pedido 

INSERT INTO detalles_pedido ( "producto_comprado", "cantidad_comprada", "subtotal")
VALUES ("mango","1", "4500")
INSERT INTO cliente ("nombre", "correo", "telefono")
VALUES ("javier","javier@gmail.com","12345678")
INSERT INTO cliente ("nombre", "correo", "telefono")
VALUES ("evaluna","evaluna@gmail.com","87654321")
INSERT INTO pedidos ("nombre_cliente", "fecha", "total_compra")
VALUES ("javier","25 de marzo","4500")
INSERT INTO productos ("nombre_producto", "precio", "stock")
VALUES ("zapote","2000","20")
INSERT INTO productos ("nombre_producto", "precio", "stock")
VALUES ("maracuya","2500","10")
INSERT INTO productos ("nombre_producto", "precio", "stock")
VALUES ("mango","4500","8")
--recuerda que las tablas me pusiste a hacerlas desde la parte de interfaz grafica debido a cierto error

