import abc


class AbstractBaseUser(abc.ABC):

	@abc.abstractmethod
	def subscribe(self):
		pass

	@abc.abstractmethod
	def unsubscribe(self):
		pass

	@abc.abstractmethod
	def like(self):
		pass

	@abc.abstractmethod
	def dislike(self):
		pass

	@abc.abstractmethod
	def publish(self):
		pass

	@abc.abstractmethod
	def share_with(self):
		pass

	@abc.abstractmethod
	def comment(self):
		pass

	@abc.abstractmethod
	def gift(self):
		pass


class BotUser(AbstractBaseUser):

	def __init__(self, *args, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)


	def subscribe(self):
		# TODO subscription
		return 'subscripted'

	def unsubscribe(self):
		# TODO unsubs
		return 'unsubscribed'

	def like(self):
		# TODO  like logic
		return 'clicked a like'

	def dislike(self):
		# TODO  dislike logic
		return 'clicked a dislike'

	def publish(self):
		# TODO publish logic
		return 'publish'

	def share_with(self, other_user):
		# TODO share logic
		return 'shared with other user'

	def comment(self):
		# TODO comment logic
		return 'post a comment'

	def gift(self):
		# TODO implement gift logic
		return 'gift'


class Author(BotUser):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class Militant(Author, BotUser):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

