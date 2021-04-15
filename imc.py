#similar ao "#include<math.h> na linguagem C"
#from math import *
import math;


#programa que calcula o IMC de uma pessoa
peso= float(input());
altura= float(input());

#Calculo do IMC sendo aplicado "IMC= Peso/altura²"
imc=  peso/(math.pow(altura, 2));

#printa o resultado do IMC
print("{:.2f}".format(imc));
