""" ADITYA DEOGAONKAR
    ASSIGNMENT :-5 [ AI ]
"""
from nltk.chat.util import Chat

reflections ={
	"i am":'you are',
	'i':'you'
}

pairs = [
	[
		r"hi|hello|hey",
		['Hello!','Hey there!']
	],
	[
		r"(.*) open(.*)",
		['Yes we are open!','No we are closed!']
	],
	[
		r"What is (rate|cost) of (.*)?",
		['%2 is for $1','%2 is for $2.5','%2 is for $10']
	],
	[
		r"quit|stop|bye",
		['Thank you!']
	],
	[
		r"(.*)",
	['I am sorry. I am unable to process']
	]
]

def chat():
	print('Welcome to Durga! How may I help you?')
	chat = Chat(pairs, reflections)
	chat.converse()

if __name__ == '__main__':
	chat()
