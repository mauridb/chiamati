import uuid



# Bot user object [Object]
class BotUser(object):
	"""
	BotUser object
	"""
	
	def get_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return "BotUser" 


# Militant user object - [Object]
class MilitantUser(object):
	"""
	Militant user object
	"""
	
	def get_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return "MilitantUser"
