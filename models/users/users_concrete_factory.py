from models.users.users_object import BotUser, MilitantUser


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
