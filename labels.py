class Label(object):
	def __init__(self, label_color, label_size_x, label_size_y, label_location_x, label_location_y, label_font):
		self.Surface = 	pygame.Surface([label_size_x, label_size_y])	
		self.rectangle = pygame.Rect(label_location_x, label_location_y, label_size_x, label_size_y)
		self.color = label_color
		self.size = label.size
		self.location = label_location
		self.font = location_font
	def draw_label(self):

