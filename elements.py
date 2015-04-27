import sys



class Element:	#defines basic properties of any element 

	def __init__(self, symbol, name, number, mass):
		self.symbol=symbol
		self.number = number
		self.name = name
		self.mass = mass
	def __repr__(self):
		return "{} {} {} {}".format(self.symbol, self.name, self.number,self.mass)
		
	

def makereference():

	key_file=open("element_name.txt",'r') #open file containing information 
	
	count=0 #count the lines aka the atomic number 
	atomic_number={}	#create hashtable of elements 
	atomic_name={} #map the name from the symbol
	for lines in key_file:
		#atomic number mapped from symbol
		count+=1
		split_line = lines.strip().replace('\t',' ').split(" ")
		name = split_line[0]
		symbol = split_line[1]
		mass=split_line[-1]
		key = symbol
		current_element = Element(symbol, name, count, mass)
		atomic_number[count] = current_element
		atomic_name[key] = current_element
	key_file.close() #close the file 
	return atomic_number, atomic_name


atomic_number, atomic_name = makereference()

class Map_Count: #class directly returns desired values 
	@staticmethod
	def number_to_element(num):
		return atomic_number.get(num)
	@staticmethod
	def symbol_to_name(string):
		return atomic_name.get(string)
	@staticmethod
	def symbol_to_mass(string):
		return float(atomic_name.get(string).mass)

