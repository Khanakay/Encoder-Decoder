from dictionary import *
from random_magic import *

#print(random_phrase)
def encoder(string_to_encode):
	#string_to_encode = input("Enter your password: ")
	#string_to_encode = 'khan'
	string_to_encode = list(string_to_encode)
	#print(string_to_encode)
	new_list = []
	for word in string_to_encode:
		for item ,value in decoder_dict.items():
			if word == value:
				new_list.append(item)
	#print(new_list)

	newest_list = []
	for num in new_list:
		for key ,value in number_to_phrase_dict.items():
			if num == key:
				newest_list.append(value)
				newest_list.append(get_random_phrase())
	#print(newest_list)
	text = ''
	for item in newest_list:
		text+=item + '.'
		#print(item,end =".")
	#print(text)
	return text