import elements 
import re
import unit 
from Significant_Figures import EasyOp
from elements import Map_Count
import sys
from Compound import Total


class Equation:
	def __init__(self,reactants,products): #accepts a tuple of reactants and products 
		self.reactants=reactants
		self.products=products
	def create_equation(self):
		equation=""
		for items in range(len(self.reactants)):
			if items==len(reactants)-1:
				equation+=reactants[items]
			else:
				equation+=reactants[items]+"+"	
			
		equation=equation+"--->"
		for items in range(len(self.products)):
			if items==len(products)-1:
				equation+=products[items]
			else:
				equation+=products[items]+"+"	
		return equation		

	def solvefor(self,given,desired):
		if given in reactants or given in products and desired in reactants or desired in products:

			reactant=unit(given) #initialize object
			product=unit(desired)
			if reactant.isgram():
				molreactant=float(reactant.prefix)/Total.returntotal(reactant.element)
				if product.isgram
					gramproduct=molreactant*Total.returntotal(desired)
				return gramproduct
			if reactant.ismole():
				molreactant=	


if __name__ == '__main__':
	reactants=["C6H12O6","6O2"]
	products=["6CO2","6H2O"]

	current=Equation(reactants,products)
	print(current.create_equation())