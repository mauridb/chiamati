from models.buttonsUI.buttons_object import (
	FirstNameButtonUI,
	LastNameButtonUI,
	SubscribeButtonUI,
	UnsubscribeButtonUI,
	LikeButtonUI,
	DislikeButtonUI,
	GiftButtonUI,
	PostButtonUI,
	ShareButtonUI
	)


# ButtonUI FirstName - [ConcreteFactory]
class FirstNameButtonUIFactory(object):

	def get_object(self):
		return FirstNameButtonUI()


# ButtonUI LastName - [ConcreteFactory]
class LastNameButtonUIFactory(object):

	def get_object(self):
		return LastNameButtonUI()


# ButtonUI LastName - [ConcreteFactory]
class SubscribeButtonUIFactory(object):

	def get_object(self):
		return SubscribeButtonUI()


# ButtonUI Unsubscribe - [ConcreteFactory]
class UnsubscribeButtonUIFactory(object):

	def get_object(self):
		return UnsubscribeButtonUI()


# ButtonUI Like - [ConcreteFactory]
class LikeButtonUIFactory(object):

	def get_object(self):
		return LikeButtonUI()


# ButtonUI Dislike - [ConcreteFactory]
class DislikeButtonUIFactory(object):

	def get_object(self):
		return DislikeButtonUI()


# ButtonUI Gift - [ConcreteFactory]
class GiftButtonUIFactory(object):

	def get_object(self):
		return GiftButtonUI()


# ButtonUI Gift - [ConcreteFactory]
class PostButtonUIFactory(object):

	def get_object(self):
		return PostButtonUI()


# ButtonUI Share - [ConcreteFactory]
class ShareButtonUIFactory(object):

	def get_object(self):
		return ShareButtonUI()
