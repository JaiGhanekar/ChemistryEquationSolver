import math 
from Significant_Figures import EasyOp

def main():

	R=8.31446
	T=float(input("What is the temperature? (in C) "))+273.15
	N=int(input("What is the N value? "))
	F=9.64853*(10**4)

	#Get the values for E 
	E_cat=float(input("Ecat? "))
	E_ox=float(input("Eox? "))
	E_O=E_cat-E_ox
	
	#declare a few constants 

	#Get the value of molarities to get Q 

	Mp=float(input("What is the molarity of the products "))
	coeff1=float(input("What is its coeffecient "))
	Mr=float(input("What is the molarity of the the reactant? "))
	coeff2=float(input("What is its coeffecient "))

	Q=(Mp**coeff1)/(Mr**coeff2)

	second_half= ((R*T)/(N*F))*math.log(Q)

	Answer=EasyOp.SUB(str(E_O),str(second_half))

	print(Answer)



if __name__ == '__main__':
	main()