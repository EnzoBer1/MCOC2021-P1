# MCOC2021-P1
Optimización estructural de un puente reticular

INTRODUCCIÓN

El siguente informe relatará e informará los avances en la confección, diseño y optimización de un puente reticular, el cual cruza un canal de 117 metros de largo, teniendo en cuenta 4 metros de ancho y 2 puntos de apoyo. Se considerará tanto crga viva como carga muerta, distintas combinaciones de carga según el método LRFD y se analizará su estabilidad estructural (si es viable o no), sus deformaciones y desempeño frente a cada combinación de carga y los factores de utilización de cada elemento, se tratará de conseguir que los FU de cada elementos estén lo más cercano a 1 posible, de tal manera de aprovechar toda la capacidad de las secciones.

Todas los tipos de secciones fueron extraidos de la Tabla de Perfiles ICHA.

RESULTADOS, DISCUSIONES Y ARREGLOS

Luego de diseñar el puente, se llegó al siguente tipo:

![image](https://user-images.githubusercontent.com/89056734/135767962-cff4c772-ba36-4b70-87dd-2fb08860a2eb.png)

Como puede apreciarse, el punete consta de "cajones" unidos entre si. La base inferior posee 2 diagonales que actuan como un arriostramiento, las pareddes laterales cuentan con una diagonal la cual une intercaladamente los 2 nodos opuestos. Luego, la cara superior posee una sola diagonal que une nodos opuestos.

Inicialmente, las barras que unen por ejemplo los nodos 44 y 104 en la imagen anterior no estaban, pero esto generó una inestabilidad estructural, o una matriz singular a nivel de código, lo cual generó la necesidad de unir estos nodos.

Las secciones incialmente fueron para las barras de la cara inferior los tipo H800x400x197.5, y para las barras de la cara superior los tipo H500x250x84.4. Los elementos adicionales (diagonales) fueron completados con el perfil tipo H500X250X84.4. 

Esta combinación arrojó los siguentes factores de utilización:

![image](https://user-images.githubusercontent.com/89056734/135768246-dbb9f53c-3d16-4298-97ba-9780bc0a8d5a.png)

Inicialmente el peso fue de 667 456, 26 kilogramos.

Tal como puedes verse, las barras de la cara inferior están al 80% de capacidad y las superiores tan solo al 10%. Por otro lado, el diseño del puente mostro que tanto las barras verticales, arriostramientos superiores y inferiores prácticamente no reciben y/o transmieen carga, por lo que se llegó a la conclusión de usar las secciones más pequeñas posibles para los elementos de factor de utilización cercano a cero para optimizar el peso de la estructura.

