class ArtDisplay:

	def __init__(self, name, date, art_type, preserving_date, worth):
		if worth <= 0:
			raise ValueError("Invalid worth value")
		self.name = name
		self.date = date
		self.art_type = art_type
		self.preserving_date = preserving_date
		self.worth = worth

	def __repr__(self):
		return self.name + " is a " + self.art_type + " that was created in " + self.date + " and needs to be preserved in " + self.preserving_date

	def __gt__(self,other):
		return self.worth > other.worth

	def change_preserving_date(self,new_date):
		self.date = new_date

	def get_worth(self):
		return self.worth


class MuseumSubscriber:

	def __init__(self, name, ticket_type, favorites):
		self.name = name
		self.favorites = favorites
		if ticket_type == '1' or ticket_type == '5': 
			self.entries_left = int(ticket_type)
		else:
			self.entries_left = ticket_type

	def __repr__(self):
		if isinstance(self.entries_left , int):
			return self.name + " has " + str(self.entries_left) + " entries left"
		else:	
			return self.name + " has a subscription until the " + self.entries_left			

	def set_entry(self):
		if isinstance(self.entries_left , int):
			if self.entries_left == 0:
				print ("Please renew your subscription")
			else:
				self.entries_left = self.entries_left-1
				print ("Welcome!", self.entries_left, "entries left")
		else:	
			print ("Welcome subscriber!")

	def get_favorites(self):
		return self.favorites


class Museum:

	def __init__(self,art_displays):
		self.art_displays = art_displays[:]
		self.subscribers = []

	def __repr__(self):
		art_displays_copy = self.art_displays
		sorted_art_displays = sorted(art_displays_copy, key = lambda x : x.get_worth())
		printable = "This museum contains the following displays:\n"
		for art_display in sorted_art_displays:
			printable = printable + str(art_display) + '\n'
		printable + '\n'
		return printable

	def get_art_displays(self):
		return self.art_displays

	def get_art_display(self,name):
		for i in self.art_displays:
			if i.name == name:
				return i

	def add_art_display(self,artDisplay):
		self.art_displays.append(artDisplay)

	def add_subscriber(self, subscriber):
		self.subscribers.append(subscriber)

	def change_preserving_date(self, name , new_date):
		for i in self.art_displays:
			if i.name == name:
				i.change_preserving_date(new_date)
		return None	

	def get_total_worth(self):
		total = 0
		for i in self.art_displays:
			total = total + i.get_worth()
		return total

	def subscriber_entry(self,name):
		for i in self.subscribers:
			if i.name == name:
				i.set_entry()

	def find_loved_disp(self):
		loved = []
		d = {}
		for i in self.subscribers:
			favorites = i.get_favorites()
			for f in favorites:
				d[f] = d.get(f, 0) + 1
		l = sorted(d.keys(), key = d.get, reverse = True)
		loved.append(l[0])
		for i in range(1,len(l)):
			if d[l[i]] == d[l[0]]:
				loved.append(l[i])
			else:
				break
		return loved


def create_museum(filename):
	f = None
	try:
		f = open(filename, 'r')
		l = f.readlines()
		museum = Museum([])
		for i in range(len(l)):
			tokens = l[i].rstrip().split(',')
			if tokens[0] == 'artDisplay':
				name = tokens[1]
				date = tokens[2]
				art_type = tokens[3]
				preserving_date = tokens[4]
				worth = int(tokens[5])
				art_display = ArtDisplay(name,date,art_type, preserving_date, worth)
				museum.add_art_display(art_display)
			else:
				break

		for j in range(i,len(l)):
			tokens = l[j].rstrip().split(',')
			name = tokens[1]
			ticket_type = tokens[2]
			favorites = []
			favorites.append(l[int(tokens[3])-1].rstrip().split(',')[1])
			favorites.append(l[int(tokens[4])-1].rstrip().split(',')[1])
			favorites.append(l[int(tokens[5])-1].rstrip().split(',')[1])
			subscriber = MuseumSubscriber(name,ticket_type,favorites)
			museum.add_subscriber(subscriber)
		print ("This museum's worth is", museum.get_total_worth())
	except IOError:
		print("Unable to load",filename,"due to an IO Error ")
	finally:
		if f != None:
			f.close()
	return museum






















