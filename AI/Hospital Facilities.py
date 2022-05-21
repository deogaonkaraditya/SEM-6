""" ADITYA DEOGAONKAR
    ASSIGNMENT :-6 [ AI ]
"""
questions = [
	'Do you have cough?',
	'Do you have fever?',
	'Do you have stuffy nose?',
	'Do you have a headache?',
	'Are you able to smell perfume?'
]

threshold = {
	'Mild':30,
	'Severe':50,
	'Extreme':75
}

def expertSystem(questions, threshold):
	score = 0
	for question in questions:
		print(question+"(Y/N):")
		ans = input("> ")
		if ans.lower() == 'y':
			print('Rate how bad it is: (1-10):')
			ip = input("> ")
			while((not ip.isnumeric()) or int(ip)<1 or int(ip)>10):
				print("Enter a valid input!")
				ip = input("> ")
			score+=int(ip)
	print()
	print()
	print()

	if score >= threshold['Extreme']:
		print("YEAH")
	else:
		print("NAH")

print("Ecper system")
expertSystem(questions,threshold)
