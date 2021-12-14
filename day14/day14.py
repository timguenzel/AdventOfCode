with open("input.txt") as f:
	input = list(map(lambda x: x.replace("\n",""), f.readlines()))

def solution(input, steps):
	string = list(input[0])
	pairs = {}

	for line in input:
		if line != '' and line != ''.join(string):
			pairs[line.split(" -> ")[0]] = line.split(" -> ")[1]

	for i in range(steps):
		char = 0
		while True:
			string.insert(char+1, pairs[string[char]+string[char+1]])
			char += 2
			if char == len(string)-1: break
	
	amount = {}
	for char in string:
		if char not in amount:
			amount[char] = 0
		else:
			amount[char] += 1

	maxChar = max(amount.values())
	minChar = min(amount.values())
	return maxChar - minChar

def replace(dict, rules):
	new_dict = dict.copy()
	for pair in dict:
		for start, end in rules:
			if pair == start:
				occ = dict[pair]
				new_dict[pair] -= occ
				if pair[0] + end not in new_dict:
					new_dict[pair[0] + end] = occ
				else:
					new_dict[pair[0]+end] += occ
				if end + pair[1] not in new_dict:
					new_dict[end+pair[1]] = occ
				else:
					new_dict[end+pair[1]] += occ
				break
	return new_dict


def solution2(input,steps):
	occurences = {}
	rules = []
	for line in input:
		if line != '' and line != input[0]:
			rules.append(line.split(" -> "))

	for char in range(len(input[0])-1):
		if input[0][char]+input[0][char+1] not in occurences:
			occurences[input[0][char]+input[0][char+1]] = 1
		else:
			occurences[input[0][char]+input[0][char+1]] += 1

	for i in range(steps):
		occurences = replace(occurences, rules)

	count = {}
	for pair in occurences:
		if pair[0] not in count:
			count[pair[0]] = occurences[pair]
		else:
			count[pair[0]] += occurences[pair]
		if pair[1] not in count:
			count[pair[1]] = occurences[pair]
		else:
			count[pair[1]] += occurences[pair]

	count[input[0][0]] += 1
	count[input[0][-1]] += 1

	count_vals = [c[1] // 2 for c in count.items()]
	
	return max(count_vals) - min(count_vals)

print(solution2(input,40))
