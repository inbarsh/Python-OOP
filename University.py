class Student:

	def __init__(self,name,id,courses):
		self.name = name
		self.id = id
		d = {}
		for course in courses:
			if courses[course][1] < 0 or courses[course][1] > 100:
				raise ValueError('Invalid grade')
			else:
				d[course] = courses[course]
		self.courses = d
		
	def __repr__(self):
		sorted_courses = sorted(self.courses.keys(), key=lambda x:x.lower())
		printable = 'Name: ' + self.name + '\nId: ' + self.id + '\nCourses list: '
		for course in sorted_courses:
			printable = printable + course + ' ' + str(self.courses[course][0]) + ' ' + str(self.courses[course][1]) + ' '
		return printable		
		
	def get_average(self):
		s = 0
		z = 0
		for course in self.courses:
			s += self.courses[course][1]*self.courses[course][0]
			z += self.courses[course][0]
		return s/z
		
		
class GradStudent(Student):

	def __init__(self,name,id,courses,degree):
		Student.__init__(self,name,id,courses)
		self.degree = degree
		
	def __repr__(self):
		result = Student.__repr__(self)
		result += '\nDegree: ' + self.degree
		return result
		
	def get_average(self):
		a = Student.get_average(self)
		if self.degree == 'msc':
			a *= 1.1
		else:
			a *= 1.2
		if a > 100:
			a = 100.0
		return a


class Faculty:

	def __init__(self,name,students):
		self.name = name
		self.students = students
		
	def __repr__(self):
		result = 'Faculty of ' + self.name + '\n'
		d = {}
		for student in self.students:
			for course in student.courses:
				d[course] = d.get(course, 0) + 1
		l = sorted(d.keys(), key = d.get, reverse = True)
		for i in l:
			result = result + str(i) + ' - ' + str(d[i]) + ' students\n'
		return result