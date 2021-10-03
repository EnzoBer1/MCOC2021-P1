# MCOC2021-P1
Optimización estructural de un puente reticular

INTRODUCCIÓN

El siguente informe relatará e informará los avances en la confección, diseño y optimización de un puente reticular, el cual cruza un canal de 117 metros de largo, teniendo en cuenta 4 metros de ancho y 2 puntos de apoyo. Se considerará tanto crga viva como carga muerta, distintas combinaciones de carga según el método LRFD y se analizará su estabilidad estructural (si es viable o no), sus deformaciones y desempeño frente a cada combinación de carga y los factores de utilización de cada elemento, se tratará de conseguir que los FU de cada elementos estén lo más cercano a 1 posible, de tal manera de aprovechar toda la capacidad de las secciones. El puente estará situado en el siguente canal:

![image](https://user-images.githubusercontent.com/89056734/135768901-00220b38-52b9-4d1f-8a31-ddc4234bf6dc.png)

La carga viva sobre el tablero del puente serña de 400 kg/m y para la combincación de carga se usará 1,2D + 1,6L.

La carga viva sobre el tablero del puente serña de 400 kg/m y para la combincación de carga se usará 1,2D + 1,6L.

Para obtener la fuerza en cada nodo, se dividio el largo total del puente en 28, para luego conseguir la fuerza resultante en cada tablero, la que correspode a F1=400*4*
(117.48/28)*9.81. Luego, esta fuerza se dividio en 4, ya que cada tablero cuenta con 4 nodos, por lo que para llegar a la fuerza total por cada nodo, F1 se multiplicó por 2 para la fuerza de los nodos de cada tablero, ya que 2/4 de la fuerza llega a todo un tablero.

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

Para optimizar el puente y lograr la estructura más liviana y viable posible, se crearon secciones de distintos tamaños y formas (perfiles H y cajón) los cuales se implementaron según los factores de utilización anteriormente mencionados. Las secciones fueron las siguientes:

![Captura de Pantalla 2021-10-03 a la(s) 17 09 34](https://user-images.githubusercontent.com/89056734/135769912-f2b40e9e-2d33-4831-acb7-3063b986d83b.png)

Con estas modificaciones, el peso total del puente bajó significativamente a los 

Al correr el código con estas secciones, los resultados fueron:

![image](https://user-images.githubusercontent.com/89056734/135768809-46d08f3f-0bd7-4c09-a649-2e760eca9179.png)

El nuevo peso de todo el puente fue de:

![Captura de Pantalla 2021-10-03 a la(s) 17 09 12](https://user-images.githubusercontent.com/89056734/135769901-d05f5e43-1f2f-4519-b834-09c3ecda8ef5.png)

CONCLUSIONES

Luego de los procesos y cambios en el diseño del puente reticular se puede concluir que el proceso computacional es de suma importancia al momento de diseñar este tipo de elementos reticulados, debido a que muestran como se comporta la estructura, ademas de mostrar el comportamiento interno, el cual ayuda a visualizar de mejor manera la estructura, y en el caso de necesitar reformas, estas se puedan automatizar y así entregar un proyecto mas optimizado y eficiente.

Existen elementos dentro de reticulados que no juegan rol estructural pero de igual manera son de suma importancia para que el sistema se comporte como la teoría y los softwares de diseño estructural quieren que se comporte.




