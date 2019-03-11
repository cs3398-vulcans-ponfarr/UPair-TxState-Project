class Group(object):

	def __init__(self, g_creator, g_id):
		self.g_creator = g_creator
		self.memberList = []
		self.memberList.append(g_creator)
		self.limiter = "null"
		self.accept = "null"
		self.g_id = g_id
		
	def setcreator(self, creator):
		self.g_creator = creator
		
	def getcreator(self):
		return self.g_creator
		
	def addmember(self, member):
		self.memberList.append(member)
		
	def getmemberlist(self):
		for x in memberList:
			print(x)
			
	def setlimiter(self, limiter):
		self.limiter = limiter
		
	def getlimiter(self):
		return self.limiter
		
	def setacceptexception(self, a_exception):
		self.accept = a_exception
		
	def getacceptexception(self):
		return self.accept
		
	def setid(self, id):
		self.g_id = id
		
	def getid(self):
		return self.g_id
