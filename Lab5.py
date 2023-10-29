import collections
string = input("1.1)буквалар: ")
ch_list = list(string)
print(ch_list)
print("1.2)буквалар неше рет кездесет")
san = collections.Counter(string)
print(san)
#san = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '#']
list_vow = []
list_cons = []
list_symb = []
for char in san:
   if char in ['a','e','i','o','u']:
       list_vow.append(char)
   elif char.isalpha():
       list_cons.append(char)
   else:
       list_symb.append(char)
#print("Initial List: ", san)
print("List Vow: ", list_vow)
print("List Cons: ", list_cons)
print("List Symbols: ", list_symb)
print()