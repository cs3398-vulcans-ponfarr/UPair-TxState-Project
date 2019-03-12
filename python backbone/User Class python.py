class User(object):

	def __init__(self, d_name, d_pass, email, in_status):
		self.d_name = d_name
		self.d_pass = d_pass
		self.email = email
		self.inStatus = in_status
		self.classlist = []

	def login(self):
	
		# get username and password
		print('Enter username: ')
		u_name = input()
		print('Enter password: ')
		_pass = input()
		
		# compare with user database
		if u_name == d_name and _pass == d_pass:
			self.inStatus = True
			return True
		
		self.inStatus = False
		return False
		
	def logout(self):
	
		self.inStatus = False
		
	def setname(self, name):
	
		self.d_name = name
		
	def getname(self):
	
		return self.d_name
		
	def setemail(self, email):
		
		self.email = email
	
	def getemail(self):
	
		return self.email
		
	def setpassword(self, _pass):
		
		self.d_pass = _pass
		
	def getpassword(self):
	
		return self.d_pass
		
	def addclasses(self, _class):
		
		self.classlist = []
		self.classlist.append(_class)
		
	def getclasses(self, classlist):
	
		for x in classlist:
			print(x)
