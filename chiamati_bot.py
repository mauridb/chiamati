import time
import telepot
from telepot.loop import MessageLoop


bot = telepot.Bot('541628015:AAFMOY4EyaI06fCc4p2HTR6jAoTYpk6fLho')

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print ('Got command: %s' % command)

	if command == '/subscribe':
		bot.sendMessage(chat_id, 'ciao')

	if command == '/unsubscribe':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/publish':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/like':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/dislike':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/share_with':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/comment':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/gift':
		bot.sendMessage(chat_id, random.randint(1,6))
	if command == '/confirmation':
		bot.sendMessage(chat_id, random.randint(1,6))
    

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
