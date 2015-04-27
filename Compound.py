#This program will define what a compound is 
#!/usr/local/bin/python
import elements 
import re
import unit 
from Significant_Figures import EasyOp
from elements import Map_Count
import sys



def finalsum(symbol): #final sum of element 
	total=0
	if '.' in symbol:
		times=symbol.count('.') #iterate over all the polyatomic ions 
		for elements in range(times):
			if '.' in symbol:	
				end=symbol.find('.') 
				total+=Total.totalmass(symbol[:end])
				symbol=symbol.replace(symbol[:end+1],"",1)			#get rid of bounds each time 
		

			if '.' not in symbol:
				total+=Total.totalmass(symbol)
		return total
	else:
		return Total.totalmass(symbol)		



def manipulate(string):	#do for each polyatomic 
	times=string.count('(') 
	for count in range(times):				#for every poly atomic ion reiter 
		string=extract_polyatomic(string)
	return string




def extract_polyatomic(string):
	polytup=[]  #empty list for all the polyatomic objects
	try:
		if '(' and ')' in string: #while polyatomics still exists 
			bound=string.find('(')  #find the bounds 
			bound2=string.find(')')
			parse_index=retcharindex(string[bound2+1:]) #repetedly replace the subscripts and store the data in tuple
			realindex=parse_index+len(string[:bound2+1])
			polytup.append(string[bound2+1:realindex])
			string=string.replace(string[bound2+1:realindex],"",1)
			polytup.append(string[bound+1:bound2])
			string=string.replace(string[bound:bound2+1],"",1)
			temppolytup=polytup[0]+polytup[1]	#carry the tupple through the event 
			polytup=[]
			polytup.append(temppolytup)
			string=string+'.'
			for elements in range(len(polytup)):
				string+=polytup[elements]
			del polytup
		return string
	except ValueError:
		string=list(string)
		string=string.replace(')',"",1)

		return string 		

def gettotal(tuples,multiplier):
		subtotal1=0
		subtotal2=0
		subtotal=0 
		
		for elements in tuples: #for every element in tuple 
			current_element=elements
			index=retindex(current_element)
			try:
				subscript=float(current_element[index:]) #get the subscript of each element 
				subtotal1=Map_Count.symbol_to_mass(current_element[:index]) #get around unit converter formatting 
				subtotal+=(subscript*subtotal1)
			except ValueError:		
				
					subtotal2+=Map_Count.symbol_to_mass(elements) #get around unit converter formatting 
			
		total=(subtotal+subtotal2)*multiplier #accumulate amount

		return total		

def dissociate(symbol):

	index=retcharindex(symbol)
	if index!=0:
		subelements=re.findall('[A-Z][^A-Z]*', symbol) #concatinate with capital letter 
		return subelements,float(symbol[:index])
	else:
		subelements=re.findall('[A-Z][^A-Z]*', symbol)
		return subelements,1 #return subelement tuple and its multiplier 

def retindex(symbol):					#find the subscripts 
	index=0
	for chars in symbol:
		
		if chars.isalpha()==False:
			return index
		index+=1
	return False


def retcharindex(symbol): #Find the entire multiplier of the compound  
	index=0
	
	for chars in symbol:
		
		if chars.isalpha()==True or chars=='.' :
			return index	
		index+=1
		if index==len(symbol) or symbol[index]=='(' or symbol[index]==')' :
			return index
	return False #false if not found 
 



class Compounds: #what is a compound 

	def __init__(self,symbol):
		self.subelements,self.multiplier=dissociate(symbol)
		self.mass=0
		
	def total_mass(self):
		
		rtotal=gettotal(self.subelements,self.multiplier)

		return rtotal
class Molar_mass: #get the final mass
	def __init__(self,symbol):
		symbol=manipulate(symbol)
		self.finaltotal=finalsum(symbol)
	def rettotal(self):
		return self.finaltotal

class Total: #find the total mass of a compound 
	@staticmethod
	def totalmass(string):
		return Compounds(string).total_mass()
	@staticmethod
	def returntotal(string):					#use this one for final mass of anything 
		return Molar_mass(string).rettotal()
	@staticmethod
	def coefficent(string):
		return Compounds(string).multiplier		

if __name__ == '__main__':
	
	user_input=str(raw_input("Compound Name "))
	print(str(Total.returntotal(user_input))+" g/mol")
	while(user_input!="q"):
		if user_input!="q":
			user_input=str(raw_input("Compound Name "))
		if user_input=="quit":
			sys.exit(1)
		print(str(Total.returntotal(user_input))+" g/mol")
	
		

