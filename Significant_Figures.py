
import sys
#This Program does significant figure math 
#Programmed by Jai Ghanekar

def option():
	if "Exit" in sys.argv:
		sys.exit()
	elif "count" in sys.argv:
		single_count()
	elif "+" in sys.argv:
		addition()
	elif '-' in sys.argv:
		fminus()
	elif 'x' in sys.argv:
		multiplication()
	elif "/" in sys.argv:
		division()
	else:
		print("Enter valid input")
			
def single_count():#if user wants feed back on one number
	number=sys.argv[2]
	count=SigFigCount(number)
	length=count.counter()
	if length==1: #print based on plural case or singular
		print("There is ",length," significant digit." )
	else:
		print("There are ",length," significant digits." )
		
def fminus(): #subtract sigfigs
	number1=sys.argv[1]
	number2=sys.argv[3]
	subtraction=Operations(number1,number2)
	result=subtraction.minus()
	print(number1," - " , number2," = " , result )
	
def addition(): #add sigfigs
	number1=sys.argv[1]
	number2=sys.argv[3]
	summation=Operations(number1,number2)
	result=summation.ssum()
	print(number1," + " , number2," = " , result )

def multiplication():#multiply sigfigs
	number1=sys.argv[1]
	number2=sys.argv[3]
	multi=Operations(number1,number2)
	result=multi.multiply()
	print(number1," * " , number2," = " , result )
	
def division():	#divide sigfigs
	number1=sys.argv[1]
	number2=sys.argv[3]
	div=Operations(number1,number2)
	result=div.divide()
	print(number1," / " , number2," = " , result )
	
	
	
class SigFigCount: #class for sigfig count
	
	use="Sig Fig Operations"
	
	def __init__(self,number): #takes in a sigfig 
		self.number=number  #instance variable for a number
		
		

	#This method counts the number of significant figures 
	def counter(self):
		start="null"
		for digit in range(len(self.number)):   #iterate over every digit
			if self.number[digit]!='0'and self.number[digit]!="." and self.number[digit]!='-':        #ignore starting 0's 
				start=digit               #record first sigfig's index
				break                     #break out of loop
		if "." in self.number[start:]:	       #store number of sigfigs in length
			length=len(self.number[start:])-1	#ignore decimal point 
		elif "." not in self.number[start:]:
			restrict=self.number[start:].count('0')
			length=len(self.number[start:])-restrict	
		else:
			length=len(self.number[start:])
			
		return length	#return length
	
	#def number_display(self,bound):
		

		
		
				
class Operations: #class for sigfug operations 
	use="Basic math operations"
	def __init__(self,number1,number2): # translate these to float and keep string format
		self.entry1=number1
		self.entry2=number2
		self.parameter1=float(number1)
		self.parameter2=float(number2)
		
	def ssum(self): #sums two measurements 

		
		position1=self.entry1.find(".")	#find location of decimal in both strings
		position2=self.entry2.find(".")
		
		if len(self.entry1[position1:])<len(self.entry2[position2:]): #compare the sigfigs after the decimal and record rounding bound
			precision=len(self.entry1[position1:])-1 #subtract the decimal point from precision 
		elif len(self.entry1[position1:])>len(self.entry2[position2:]): 
			precision=len(self.entry2[position2:])-1 
		elif len(self.entry1[position1:])==len(self.entry2[position2:]): 
			precision=len(self.entry1[position1:])-1
			
		result=self.parameter1+self.parameter2 #add parameters 
		result=round(result,precision) 
		
		return result
	
	def minus(self): #subtracts two measurements
		position1=self.entry1.find(".")	#find location of decimal in both strings
		position2=self.entry2.find(".")
		
		if len(self.entry1[position1:])<len(self.entry2[position2:]): #compare the sigfigs after the decimal and record rounding bound
			precision=len(self.entry1[position1:])-1 #subtract the decimal point from precision 
		elif len(self.entry1[position1:])>len(self.entry2[position2:]): 
			precision=len(self.entry2[position2:])-1 
		elif len(self.entry1[position1:])==len(self.entry2[position2:]): 
			precision=len(self.entry1[position1:])-1
			
		result=self.parameter1-self.parameter2 #subtract parameters 
		result=round(result,precision) 
		
		return result
	
	def multiply(self): #multiply sigfigs
		size1=SigFigCount(self.entry1)	#declare size1 and size2 objects of type SigFigCount to compute smallest number of sigfigs
		size2=SigFigCount(self.entry2)
		negative=False 
		if size1.counter()<size2.counter(): #test all cases of length and assign smallest to precision
			precision=size1.counter()
		elif size1.counter()>size2.counter():
			precision=size2.counter()
		elif size1.counter()==size2.counter():	
			precision=size1.counter()
		#Test negative case 

		if '-' in str(self.parameter1):
			if '-' not in str(self.parameter2):
				negative=True
		elif '-' in str(self.parameter2):
			if '-' not in str(self.parameter1):
				negative=True		
		result=self.parameter1*self.parameter2 #multiply parameters
		
		subresult=[]
		for digits in str(result):		#convert float to list and ignore the decimal point
			subresult.append(digits)
		fresult=[]	
		dot=str(result)
		dot=dot.index('.')
		for numbers in subresult:
			if numbers != '.' and numbers!='-':	
				fresult.append(int(numbers))
		if fresult[0]==0:
				precision+=1			

		for entries in range(len(fresult)):  #Split floating number into a list to manipulate the digits 
			
			if entries+1==precision:
					
				if fresult[entries+1]>=5 :			#rules for rounding a number 
					fresult[entries]+=1	
				if fresult[entries+1]<5:
					continue	

			elif entries+1>precision: #set reamaining digits to 0 
				fresult[entries]=0	

		if negative: fresult.insert(0,'-')	
		fresult.insert(dot,'.')
		fresult=[str(fresult[strings]) for strings in range(len(fresult)) ]
		display=str()
		result=display.join(fresult)
		if precision+1<dot:
			return result[:dot]
		else:
			return result[:precision+1]
	
	def divide(self): #method divides sigfigs
		size1=SigFigCount(self.entry1)	#declare size1 and size2 objects of type SigFigCount to compute smallest number of sigfigs
		size2=SigFigCount(self.entry2)
		negative=False 
		if size1.counter()<size2.counter(): #test all cases of length and assign smallest to precision
			precision=size1.counter()
		elif size1.counter()>size2.counter():
			precision=size2.counter()
		elif size1.counter()==size2.counter():	
			precision=size1.counter()
		#Test negative case 

		if '-' in str(self.parameter1):
			if '-' not in str(self.parameter2):
				negative=True
		elif '-' in str(self.parameter2):
			if '-' not in str(self.parameter1):
				negative=True		
		result=self.parameter1/self.parameter2 #multiply parameters
		
		subresult=[]
		for digits in str(result):		#convert float to list and ignore the decimal point
			subresult.append(digits)
		fresult=[]	
		dot=str(result)
		dot=dot.index('.')
		for numbers in subresult:
			if numbers != '.' and numbers!='-':	
				fresult.append(int(numbers))
		if fresult[0]==0:
				precision+=1			

		for entries in range(len(fresult)):  #Split floating number into a list to manipulate the digits 
			
			if entries+1==precision:
					
				if fresult[entries+1]>=5 :			#rules for rounding a number 
					fresult[entries]+=1	
				if fresult[entries+1]<5:
					continue	

			elif entries+1>precision: #set reamaining digits to 0 
				fresult[entries]=0	

		if negative: fresult.insert(0,'-')	
		fresult.insert(dot,'.')
		fresult=[str(fresult[strings]) for strings in range(len(fresult)) ]
		display=str()
		result=display.join(fresult)
		if precision+1<dot:
			return result[:dot]
		else:
			return result[:precision+1]
#set values 


class EasyOp: #easily access class operations 
	@staticmethod
	def ADD(num,num2):
		return Operations(num,num2).ssum()
	@staticmethod	
	def SUB(num,num2):
		return Operations(num,num2).minus()
	@staticmethod	
	def MUL(num,num2):
		return Operations(num,num2).multiply()
	@staticmethod	
	def DIV(num,num2):
		return Operations(num,num2).divide()
	@staticmethod	
	def COUNT(num):
		return SigFigCount(num).counter()					
	
	
if __name__=='__main__':
	print(EasyOp.DIV('7171','.277432'))
	


	
	

