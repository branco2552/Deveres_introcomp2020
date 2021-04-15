#Programa de calculo do delta segundo grau

#similar ao "#include<math.h> na linguagem C"
#from math import *
import math;


ValorA= float(input());
ValorB= float(input());
ValorC= float(input());

delta= (math.pow(ValorB, 2) - 4 * ValorA * ValorC;

if delta < 0:
    print("NENHUMA");
        
elif delta == 0:     
	print("UMA");
        
elif delta > 0:
	print("DUAS");
