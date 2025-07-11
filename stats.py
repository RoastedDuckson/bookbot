def get_num_words(str_text):
	wrd_cnt = len(str_text.split())
	return wrd_cnt

def get_char_word_type(text):
	char_dic = {}
	lower_text = text.lower()
	char_list = list(lower_text)
	for char in char_list:
		char_dic[char] = char_dic.get(char,0) + 1
	return char_dic

def sort_char_num(char_dic):
	return dict(sorted(char_dic.items(), key=lambda x: x[1], reverse=True))






