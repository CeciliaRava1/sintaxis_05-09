language_1 = ''
language_2 = ''
languaje_3 = ''
list_language_1 = []
list_language_2 = []
list_language_3 = []
elements_in_L1_and_L2 = []
elements_in_L1_and_NOT_in_L2 = []
elements_in_L2_and_NOT_in_L1 = []
union_L1_L2 = ''
union_L1_L3 = ''
union_L2_L3 = ''
reached = 0

#Type first language
while reached != 1:
	language_1 = input('Type characters for the first language, between "{}" and separates with ","')
	if language_1[0] == "{" and language_1[-1] == "}" and language_1 not in ' ':
		reached = 1

#Type second language
reached = 0
while reached != 1:
	language_2 = input('Type characters for the first language, between "{}" and separates with ","')
	if language_2[0] == "{" and language_2[-1] == "}" and language_2 not in ' ':
		reached = 1

#Type third language
reached = 0
while reached != 1:
	language_3 = input('Type characters for the first language, between "{}" and separates with ","')
	if language_3[0] == "{" and language_3[-1] == "}" and language_3 not in ' ':
		reached = 1

word = ''
init = 0
end = 0
reached = 0
#Save syllabes in list language 1
for i in range(1, len(language_1)-1):
	if language_1[i] != ',' and language_1[i] != "{" and language_1[i] != "}":
		end += 1
		word += language_1[i]
	else:
		list_language_1.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
list_language_1.append(word)

word = ''
#Save syllabes in list language 2
for i in range(1, len(language_2)-1):
	if language_2[i] != ',' and language_2[i] != "{" and language_2[i] != "}":
		end += 1
		word += language_2[i]
	else:
		list_language_2.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
list_language_2.append(word)

word = ''
#Save symbolls in list language 3
for i in range(1, len(language_3)-1):
	if language_3[i] != ',' and language_3[i] != "{" and language_3[i] != "}":
		end += 1
		word += language_3[i]
	else:
		list_language_3.append(word)
		reached = 1
		init = end+1
		end = 0
		word = ''
list_language_3.append(word)

#Elements shared between L1 and L2
#Elements in L1 and not in L2
for i in language_1:
	if i in language_2 and i != ',' and i != '{' and i != '}':
		elements_in_L1_and_L2.append(i)
	if i not in language_2:
		elements_in_L1_and_NOT_in_L2.append(i)

#Elements in L2 and not in L1
for i in language_2:
	if i not in language_1:
		elements_in_L2_and_NOT_in_L1.append(i)

#Can I obtain Lx = Ly + Lz?
union_L1_L2 = list_language_1 + list_language_2
union_L1_L3 = list_language_1 + list_language_3
union_L2_L3 = list_language_2 + list_language_3

#Alphabetical order to compare in the next step
list_language_1.sort()
list_language_2.sort()
list_language_3.sort()
union_L1_L2.sort()
union_L1_L3.sort()
union_L2_L3.sort()

#Print Results
print(f'Elements shared between L1 and L2 {elements_in_L1_and_L2}')
print(f'Elements in L1 and not in L2 {elements_in_L1_and_NOT_in_L2}')
print(f'Elements in L2 and not in L1 {elements_in_L2_and_NOT_in_L1}')

#Compare Lx = Ly + Lz
if list_language_3 == union_L1_L2:
	print("It's possible to obtain L3 = L1 + L2")
else:
	print("It's NOT possible to obtain L3 = L1 + L2")

if list_language_2 == union_L1_L3:
	print("It's possible to obtain L2 = L1 + L3")
else:
	print("It's NOT possible to obtain L2 = L1 + L3")

if list_language_1 == union_L1_L3:
	print("It's possible to obtain L1 = L1 + L3")
else:
	print("It's NOT possible to obtain L1 = L1 + L3")