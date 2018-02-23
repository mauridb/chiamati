"""
Title: 
	"Chiamati"

	Created at: 
		23/02/2018

		** by Maurizio Bussi
"""
from models.buttonsUI.buttons_concrete_factory import (
	FirstNameButtonUIFactory, 
	LastNameButtonUIFactory, 
	SubscribeButtonUIFactory, 
	UnsubscribeButtonUIFactory,
	LikeButtonUIFactory,
	DislikeButtonUIFactory,
	GiftButtonUIFactory,
	PostButtonUIFactory,
	ShareButtonUIFactory
	)
from models.users.users_concrete_factory import BotUserFactory, MilitantUserFactory

import random

# Telegram System [Abstract]
class TelegramBotSystem(object):
	"""
	Abstract factory
	"""
	
	def __init__(self, factory=None):
		self.factory = factory


	def show_user(self):
		obj = self.factory().get_object() # TODO isinstance() check
		obj_id = obj.get_id()
		print("OBJECT: ", obj)
		print("OBJECT_ID: ", obj_id)


def get_factory():
	return random.choice([
		BotUserFactory, 
		MilitantUserFactory,
		FirstNameButtonUIFactory,
		LastNameButtonUIFactory,
		LikeButtonUIFactory,
		DislikeButtonUIFactory,
		SubscribeButtonUIFactory,
		UnsubscribeButtonUIFactory,
		GiftButtonUIFactory,
		PostButtonUIFactory,
		ShareButtonUIFactory
		])

