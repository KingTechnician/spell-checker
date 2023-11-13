import difflib

def load_data():
    return open("wordlist.txt","r").read().split("\n")

programOver = False

def analyze_differences(word_list,word):
  copied_list = word_list
  copied_list.append(word)
  copied_list = sorted(copied_list)
  index = copied_list.index(word)
  print(f"{word} at index {index}")
  print(copied_list)
  if(index==0):
    return copied_list[0:2]
  elif(index==len(copied_list)-1):
    return copied_list[index-2:]
  else:
    return [copied_list[index-1],copied_list[index+2]]

word_list = load_data()

while (not programOver):
  response = input("Enter the word for spell checking, 111 to lose.")
  if(response=="111"):
    programOver = True
  closest_match = difflib.get_close_matches(response,word_list,cutoff=0.15)[0]
  if(abs(len(closest_match)-len(response))<=1):
    print(f"The suggested spelling is: {closest_match}")
    