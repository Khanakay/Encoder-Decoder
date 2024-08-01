from dictionary import *

def decoder(string_to_decode):
	#string_to_decode = input("Enter your encoded paragraph: ")
	string_to_decode = string_to_decode.split(".")
	#print(string_to_decode)
	new_list = []
	for word in string_to_decode:
		for value , item in number_to_phrase_dict.items():
			if word == item:
				new_list.append(value)
				#print(new_list)
	#print(new_list)
	newest_list = []
	for num in new_list:
		for key ,value in encoder_dict.items():
			if num == value:
				newest_list.append(key)
				#print(newest_list)
	#print(newest_list)
	text = ''
	for item in newest_list:
		#print(item,end="")
		text += item
	return text