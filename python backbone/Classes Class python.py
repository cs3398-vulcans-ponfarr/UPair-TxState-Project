class Classes(object):

	def __init__(self, c_name, c_subject, c_professor, c_time):
		self.c_name = c_name
		self.c_subject = c_subject
		self.c_professor = c_professor
		self.c_time = c_time
		
	def getname(self):
		return self.c_name
		
	def setname(self, name):
		self.c_name = name
	
	def getsubject(self):
		return self.c_subject
		
	def setsubject(self, subject):
		self.c_subject = subject
		
	def getprofessor(self):
		return self.c_professor
		
	def setprofessor(self, professor):
		self.c_professor = professor
		
	def gettime(self):
		return self.c_time
		
	def settime(self, time):
		self.c_time = time
