from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
import pandas as pd
 
class Circular(object):
    """define una seccion Circular"""

    def __init__(self, D, Dint, color=rand(3)):
        super(Circular, self).__init__()
        self.D = D
        self.Dint = Dint
        self.color = color  #color para la seccion
        
        
        
      
               

    def area(self):
        return pi*(self.D**2 - self.Dint**2)/4

    def peso(self):
        return self.area()*ρ_acero*g_

    def inercia_xx(self):
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):
        return self.inercia_xx()

    def nombre(self):
        return f"O{self.D*1e3:.0f}x{self.Dint*1e3:.0f}"

    def __str__(self):
        return f"Seccion Circular {self.nombre()}"


        
#Mas adelante, no es para P1E1

class SeccionICHA(object):
    """Lee la tabla ICHA y genera una seccion apropiada"""

    def __init__(self, denominacion, base_datos="Perfiles ICHA.xlsx", debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color  #color para la seccion

        s=self.denominacion
        a=s
        l=""
        n=""
        final=0
        c1=0
        c2=0
        c3=0
        c4=0
        c5=0
        for x in a:
            
            if x=="1" or x=="2" or x=="3" or x=="4" or x=="5 " or x=="6" or x=="7" or x=="8" or x=="9" or x=="9":
                c2=c1
                
                break
            else:
                c1+=1
        for y in a[c2:]:
            if y=="x":
                c3=c2+1
                c4=c3
                break
            else:
                c2+=1
        
        for z in a[c3:]:
            if z=="x":
                c5=c4
                c6=c5+1 
                
                if a[(len(a)-2)]==".":
                    number3=float(a[c6:])
                    break
                elif a[(len(a)-1)]==".":
                    
                    final=1
                    number3=int(1)
                else:
                    number3=int(a[c6:])
                    
            else:
                c4+=1
        

        sigla=a[0:c1]
        number1=int(a[c1:c2])
        
        
        number2=int(a[c3:c5])
        
    
        
        if sigla=="H" or sigla=="PH":
            a1=14
            a2=1
            a3=3
            a4=5
            a5=9
            a6=10
            a7=14
            
        if sigla=="HR":
            a1=14
            a2=5
            a3=7
            a4=9
            a5=13
            a6=14
            a7=18
            
        #print(sigla)
        #print(number1)
        #print(number2)
        #print(number3)
        df = pd.read_excel("Perfiles ICHA.xlsx", header=None, skiprows=a1,sheet_name=sigla)
        n=len(df)
        nn=-1
        
        
            
        while nn<=n:
               nn+=1
               aa=df[a2][nn]
               bb=df[a3][nn]
               cc=df[a4][nn]
               
               
               if number1==aa and number2==bb and number3==cc and final==0:
                   area=df[a5][nn]
                   Ix=df[a6][nn]
                   Iy=df[a7][nn]
                   peso=df[a4][nn]
                   print(a,"encontrada =",area,"Ix =",Ix,"Iy =",Iy)
                 
                   print(f"Area:{area}")
                   print(f"Peso:{peso}")
                   print(f"Ixx:{Ix}")
                   print(f"Iyy:{Iy}")
                   break
               else:
                   print("Tipo de seccion",a,"no encontrada en Base de datos ")
                   area="nan"
                   peso="nan"
                   Ix="nan"
                   Iy="nan"
                   print(f"Area:{area}")
                   print(f"Peso:{peso}")
                   print(f"Ixx:{Ix}")
                   print(f"Iyy:{Iy}")
                   break
        
    def area(self):
        return 0

    def peso(self):
        return 0

    def inercia_xx(self):
        return 0

    def inercia_yy(self):
        return 0

    def __str__(self):
        return f"Seccion ICHA {self.denominacion}"
