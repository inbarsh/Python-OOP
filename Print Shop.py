class Order:

	def __init__(self,client_name,copies):
		if copies < 1 or len(client_name) < 1:
			raise ValueError('Invalid input')
		self.client_name = client_name
		self.copies = copies
		
	def __repr__(self):
		return 'Client name: ' + self.client_name + ', Copies: ' + str(self.copies)
		
class PosterOrder(Order):
	
	def __init__(self,client_name,copies,size):
		if len(size) != 2 or size[0] < 1 or size[1] < 1:
			raise ValueError('Invalid poster size')
		Order.__init__(self,client_name,copies)
		self.size = size
		
	def __repr__(self):
		result = 'Poster order: ' + Order.__repr__(self)
		return result + ', Size: '+ str(self.size)
		
	def calc_cost(self):
		return int(30*self.copies*self.size[0]*self.size[1])


class LetterOrder(Order):
	
	def __init__(self,client_name,copies,paper_type,paper_prices):
		if paper_type not in paper_prices:
			raise ValueError('Invalid paper type')
		Order.__init__(self,client_name,copies)
		self.paper_type = paper_type
		self.paper_prices = paper_prices
		
	def __repr__(self):
		result = 'Letter order: ' + Order.__repr__(self)
		return result + ', Paper type: '+ self.paper_type
		
	def calc_cost(self):
		return int(self.copies*self.paper_prices[self.paper_type])
		
		
class PrintShop:
	
	def __init__(self):
		self.orders = []
		self.revenues = 0
		
	def add_order(self,order):
		self.orders.append(order)
		
	def print_next_order(self):
		order = self.orders.pop(0)
		self.revenues += order.calc_cost()
		
	def __repr__(self):
		d = {}
		result = 'Print shop orders: \n' 
		for order in self.orders:
			d[order.client_name] = d.get(order.client_name, 0) + 1
		for i in d:
			result = result + i + ': ' + str(d[i]) + ' orders\n'
		result = result + 'Revenues: ' + str(self.revenues) + '\n'
		return result
