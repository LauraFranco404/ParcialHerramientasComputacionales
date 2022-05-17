# **ParcialHerramientasComputacionales**
## **Documentación del Problema**
### Problema
Las cafeterías de la universidad requieren automatizar el cobro de almuerzos brindados a la comunidad estudiantil, por lo que han fijado precios y descuentos a cobrar dependiendo del caso. Se desea saber entonces por cada compra cu´anto debe pagar el usuario en caja. Para ello:

1. Pida por teclado la siguiente información para el cliente: cédula y rol: profesor o estudiante. _Si es estudiante pregunte si es del programa de becas_

2. Registrar el producto a comprar: código producto, cantidad de unidades y precio del producto. _(un solo producto, varias unidades, por ejemplo: producto 076: gaseosa, 3 unidades)_.
Los descuentos están dados de la siguiente forma: 
> - los estudiantes tienen un 30% de descuento,
> si tiene beca será del 50% mientras que los profesores tienen un 20% de descuento

3. Al final el procedimiento por cada cliente deberá imprimir el valor a pagar por sus productos. De la forma: 
> ”El **Rol** con cedula **Numero**, debe pagar **Valor** por el producto **Código**”
___
#### _Ejemplo_ 

"El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076".
>_Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cédula de cada cliente y el código del producto llevado en el mensaje._


### Modelo Computacional
El modelo computacional que se sigue, consiste en responder una serie de puntos; comenzando desde la solicitud de ciertos datos del usuario. _(Cédula, rol)_.
<br>
<br>
Después se muestra el inventario, en donde se pueden visualizar los productos existentes y el código con el cual se encunetran. Esta información estará contenida en un diccionario llamado _**inventario**_. Y al seleccionar el código, se extraerá el producto y su precio de un diccionario llamado _**precios**_.
<br>
<br>
Dependiendo de la cantidad de productos adquiridos y el precio que se asocia a cada producto; se realiza una operación que multiplique ambos valores. Poswteriormente, se le resta el porcentaje de descuento asignado a cada persona según su rol.
<br>
<br>
Finalmente se imprime un recibo que contiene la información del cliente y la factura que contiene tanto el costo de la compra como el código de aquello0 que compró.

### Entrada
Inicialmente, a la función princiupal no se le da ningún parámetro en la entrada, dado a que los datos que se incluyen en la solución del problema están constituidos todos por inputs.
<br>
<br>
Además es importante mencionar que se utuilizan dos variables definidas enteriormente. ambos son diccionarios que contienen la información necesaria para extraer de ellos la información de los productos, dado a que estos son constantes.

### Salida
Como lo mencioné anteriormente, la salida consiste en imprimir un mensaje que contenga el rol, el número de la cédula y la información de la compra de cada persona.

### Cálculo de la solución
Se llevan a cabo diferentes operaciones y se almacenan los nombres de ciertos inputs que se convierten en las variables. Al imprimir, se realiza del proceso especificado anteriormente y se da el resultado.

