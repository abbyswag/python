# This is library of State Machine created by Abhishek Singh

class SM(object):
	"""This is main class, 
	it takes the input and current state and strems output and next state."""
	def start(self):
		"""Start the state machine"""
		self.state = self.startState
	def step(self,inp):
		"""Takes one input and gives next state and ouput"""
		(s,o) = self.getNextValues(self.state,inp)
		self.state = s
		return o
	def transduce(self,inputs,verbose = False):
		"""Takes stream of input and gives stream of output and next states"""
		self.start()
		result = []
		for inp in inputs:
			out = self.step(inp)
			result.append(out)
			if verbose:
				print('In: '+ str(inp) + ' Out: ' +str(out)+ ' Next Sate: ' +str(self.state))
		return result
	def run(self,n = 10):
		"""Takes list of none as input stream"""
		return self.transduce([None]*n)

# Some useful state machine

class Accumulater(SM):
	def __init__(self,initialValue):
		self.startState = initialValue
	def getNextValues(self,state,inp):
		return (state+inp,state+inp)

class Delay(SM):
	def __init__(self,initialValue):
		self.startState = initialValue
	def getNextValues(self,state,inp):
		return (inp,state)	

# Combination classes

class Cascade(SM):
	def __init__(self,sm1,sm2):
		self.sm1 = sm1
		self.sm2 = sm2
		self.startState = (sm1.startState,sm2.startState)
	def getNextValues(self,state,inp):
		(s1,s2) = state
		(news1,o1) = self.sm1.getNextValues(s1,inp)
		(news2,o2) = self.sm2.getNextValues(s2,o1)
		return ((news1,news2),o2)

class Parallel(SM):
	def __init__(self,sm1,sm2):
		self.sm1 = sm1
		self.sm2 = sm2
		self.startState = (sm1.startState,sm2.startState)
	def getNextValues(self,state,inp):
		(s1,s2) = state
		(news1,o1) = self.sm1.getNextValues(s1,inp)
		(news2,o2) = self.sm2.getNextValues(s2,inp)
		return ((news1,news2),(o1,o2))

class Parallel2(SM):
	def __init__(self,sm1,sm2):
		self.sm1 = sm1
		self.sm2 = sm2
		self.startState = (sm1.startState,sm2.startState)
	def getNextValues(self,state,inp):
		(s1,s2) = state
		(i1,i2) = splitValue(inp)
		(news1,o1) = self.sm1.getNextValues(s1,inp)
		(news2,o2) = self.sm2.getNextValues(s2,o1)
		return ((news1,news2),(o1,o2))

	def splitValue(v):
		if v == 'undefined':
			return ('undefined','undefined')
		else:
			return v

class ParallelAdd(Parallel):
	def getNextValues(self,state,inp):
		(s1,s2) = state
		(news1,o1) = self.sm1.getNextValues(s1,inp)
		(news2,o2) = self.sm2.getNextValues(s2,inp)
		return ((news1,news2),o1+o2)

class Feedback(SM):
	def __init__(self,sm1):
		self.sm1 = sm1
		self.startState = sm1.startState
	def getNextValues(self,state,inp):
		(ignore,o) = self.sm1.getNextValues(state,'undefined')
		(newS,ignore) = self.sm1.getNextValues(state,o)
		return (newS,o)