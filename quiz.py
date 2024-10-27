username = input('Enter your name: ')
print()
print('----------START----------')
print()

def new_test():

	nums_of_correct_answer = 0
	user_answers = []
	actual_answers = []

	question_id = 0
	for question, answer in questions.items():
		print(question)
		for option in options[question_id]:
			print(option)
		user_answer = check_answer_validation(input('Enter your answer: ').upper())
		user_answers.append(user_answer)
		actual_answers.append(answer)
		nums_of_correct_answer += check_answer(user_answer, answer)
		question_id += 1
		print()

	display_answer = ''
	for actual_answer in actual_answers:
		display_answer += actual_answer + ' '
	print(f"Test's answers: {display_answer}")

	display_user_answer = ''
	for user_answer in user_answers:
		display_user_answer += user_answer + ' '
	print(f"Your answers: {display_user_answer}")

	print(f"Your score: {nums_of_correct_answer*20}/100")


def check_answer_validation(answer):
	if answer in ['A', 'B', 'C', 'D']:
		return answer
	else:
		next_answer = answer
		while not next_answer in ['A', 'B', 'C', 'D']:
			print('Please enter A B C D only!')
			next_answer = input('Enter your answer: ').upper()
		return next_answer


def check_answer(user_answer, actual_answer):
	if user_answer == actual_answer:
		print(f'{username} answer is correct')
		return 1
	else:
		print(f'{username} answer is incorrect')
		return 0

def test_again():
	print()
	result = input('Do you wanna test again? Please say yes or no: ').lower()
	if result == 'yes':
		return True
	else:
		return False

questions = {'what is 2 + 2 equal?':'A',
			'what is 2 x 5 equal?':'C',
			'what is 7891 x 0':'B',
			'what the root of 9?':'A',
			'Where does the Sun rise?': 'D'
			}

options = [["A. 4","B. 1","C. 2","D. 7"],
["A. 11","B. 3","C. 10","D. 7"],
["A. 1","B. 0","C. 7891","D. None are correct"],
["A. 3","B. 9","C. 18","D. 11"],
["A. West","B. North","C. South","D. East"]]

new_test()

while test_again():
	new_test()

print()
print(f'Bye Bye, {username}')