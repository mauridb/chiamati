"""
Title: 
	"Chiamati"

	Created at: 
		23/02/2018

		** by Maurizio Bussi
"""
import random
import uuid


# Telegram System [Abstract]
class TelegramBotSystem(object):
	"""
	Abstract factory
	"""
	
	def __init__(self, factory=None):
		self.factory = factory


	def show_user(self):
		obj = self.factory().get_object()
		obj_id = obj.get_id()
		print("OBJECT: ", obj)
		print("OBJECT_ID: ", obj_id)


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


# Bot user - [ConcreteFactory]
class BotUserFactory(object):
	"""
	Concrete bot user factory
	"""

	def get_object(self):
		return BotUser()


	def get_bio(self):
		return 'Bot factory user bio'


# Militant user - [ConcreteFactory]
class MilitantUserFactory(object):
	"""
	Concrete militant user factory
	"""

	def get_object(self):
		return MilitantUser()


	def get_bio(self):
		return 'Militant factory user bio'


# ButtonUI FirstName - [Object]
class FirstNameButtonUI(object):

	def get_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return 'FirstNameButtonUI'


# ButtonUI LastName - [Object]
class LastNameButtonUI(object):

	def get_id(self):
		return str(uuid.uuid1())

	def __str__(self):
		return 'LastNameButtonUI'


# ButtonUI FirstName - [ConcreteFactory]
class FirstNameButtonUIFactory(object):

	def get_object(self):
		return FirstNameButtonUI()


# ButtonUI LastName - [ConcreteFactory]
class LastNameButtonUIFactory(object):

	def get_object(self):
		return LastNameButtonUI()


def get_factory():
	return random.choice([
		BotUserFactory, 
		MilitantUserFactory,
		FirstNameButtonUIFactory,
		LastNameButtonUIFactory
		])


if __name__ == '__main__':
	for index in range(4):
		my_system_bot = TelegramBotSystem(get_factory())
		my_system_bot.show_user()
