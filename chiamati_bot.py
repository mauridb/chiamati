import time
import telepot

from telepot.loop import MessageLoop
from models.abstract_factory import TelegramBotSystem, get_factory

# bot = telepot.Bot('541628015:AAFMOY4EyaI06fCc4p2HTR6jAoTYpk6fLho')

if __name__ == '__main__':
	for index in range(1):
		my_system_bot = TelegramBotSystem(get_factory())
		my_system_bot.show_user()
