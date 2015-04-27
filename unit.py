import sys 
from Significant_Figures import EasyOp
from elements import Map_Count

#This Program converts units used in chemisty 
#Programmed by Jai Ghanekar 

#Create a class of objects that have units 

def prefix(string):
		position=string.split() #Finding scalar value of the unit 
		string=position[0]
		#string=float(string)
		return string

def suffix(string):	#Find the unit dimmention 
	position=string.split()
	string=position[1]
	string=string.lstrip()
	return string

def keyelement(string):#element answer is given in 
	position=string.split()
	sting=posion[2]
	return string


class units:
	use="This is a unit converter"

	def __init__(self,entry):
		self.scalar=entry
		self.prefix=prefix(entry)
		self.suffix=suffix(entry)
		self.element=keyelement(entry)

	def isgram(self):			#Defines what is a gram
		if 'g' or 'gram' in self.suffix:
			return True 

		else:
			return False
	def ismole(self): #Define a mol 
		if 'mol' or 'moles' in self.suffix:
			return True 

		else:
			return False			
	
	def gram_mole(self,key):
		if self.isgram():

			substring= str(EasyOp.DIV(self.prefix,Map_Count.symbol_to_name(key).mass))+' mol'
			return substring
	def mole_gram(self,key):
		if self.ismole():

			substring= str(EasyOp.MUL(self.prefix,Map_Count.symbol_to_name(key).mass))+' g'
			return substring
if __name__=='__main__':
	unit=units("3.24 mole C")
	print(unit.mole_gram('C'))