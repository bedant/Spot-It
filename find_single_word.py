def findSingleWord(words_list,word):
	# words_list = str.split()
	idxList=[]
	for i in range(len(words_list)):
		if word == words_list[i]:
			idxList.append(i)
	return idxList
if __name__ == "__main__":
	string="testing hello world hello _hello "
	word="hello"
	print(findSingleWord(string,word))