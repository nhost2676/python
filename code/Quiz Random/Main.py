from random import randrange

question_input = "question.txt"
answer_input = "answer.txt"

question = []
answer = []

question = open(question_input).readlines()	
question = map(lambda s: s.strip(), question)
answer = open(answer_input).readlines() 
answer = map(lambda s: s.strip(), answer)

def quiz():
	q_index = randrange(0,len(question))
	print question[q_index]
	right_asw = answer[q_index]
	asw = raw_input (">>>>> Dap an cua ban la: ")
	
	if asw == right_asw:
		print "You right!!"
	else:
		print "You wrong!!" 
		print "Dap an la: %s" % right_asw  
def add_quiz(qs,aws):
	f = open(question_input,'a')
	f1 = open(answer_input,'a')
	f.write(qs + '\n')
	f1.write(aws + '\n')
	f.close()
	f1.close()


#print question
#print answer

while True:
	print """
	!!!GAME QUIZ!!!
		1. Add question.
		2. Star game.
"""
	choice = raw_input('>>>> ')

	if choice == '1':
		n = int(raw_input('So cau hoi muon them:  '))
		while n > 0:
			print "Your QS:"
			_qs = raw_input('>>> ')
			print "Your AS:"
			_as = raw_input('>>> ')
			add_quiz(_qs, _as)
			n -= 1
	
	if choice == '2':
		m = int(raw_input('So cau hoi muon choi:  '))
		while  m > 0:
			quiz()
			m -= 1
		
	if choice == '3':
		break