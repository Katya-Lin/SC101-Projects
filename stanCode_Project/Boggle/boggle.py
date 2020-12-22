"""
File: boggle.py
Name: Katya Lin
----------------------------------------
TODO: To input random letters into a board and search words
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
d_list = []
board = []
previous_w = [] # To store the words that had already been found
count_lst = []

def main():
	"""
	TODO: To create a board list and check the coordinate around a letter
	"""
	global board
	read_dictionary()
	for i in range(4):
		lst = []
		letters = input(f'{i+1} row of letters: ')
		if letters[1] is not ' ' or letters[3] is not ' ' or letters[5] is not ' ':
			print('Illegal Input')
			break
		for j in range(4):
			lst += letters[(j * 2)]  # To avoid the blank
		board.append(lst)

	for i in range(4):
		for j in range(4):
			word = board[i][j]  # Roll & Column
			coordinate_l = [(i, j)]
			search_word(board, i, j, word, coordinate_l, count_lst)
			coordinate_l.clear()

	print('There are ' + str(sum(count_lst)) + ' words in total.')


def search_word(b, roll, col, word, cod_l, count):

	global previous_w, count_lst

	if word in d_list and word not in previous_w:
		print(f'Found \"{word}\" ')
		previous_w.append(word)
		count_lst.append(1)

	else:
		# if has_prefix(word) is True:
			for i in range(-1, 2):     # To prevent the x coordinate from getting out of the board range
				for j in range(-1, 2):  # To prevent the y coordinate from getting out of the board range
					if 4 > roll + i >= 0 and 4 > col + j >= 0 and (roll+i, col+j) not in previous_w:
						cod_l.append((roll + i, col + j))
						word += b[roll + i][col + j]
						search_word(b, roll + i, col + j, word, cod_l, count)
						cod_l.pop()
						word = word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global d_list
	with open(FILE, 'r') as f:
		for line in f:
			d_list.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	check = False
	for word in d_list:
		if word.startswith(str(sub_s)) is True:
			check = True
			break
	return check


if __name__ == '__main__':
	main()
