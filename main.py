# age = 10
# if age > 15:
#   print("Okok")
# else:
#   print("Nop")

# import statistics
# import random

# note_list = []
# for i in range(10):
#   note_list.append(random.randint(0, 20))
# print(note_list)
# print(statistics.mean(note_list))

# list_notes = [
#   [16, 6, 4, 9, 19, 0, 20, 7, 13, 18], 
#   [7, 4, 8, 2, 0, 20, 1, 16, 1, 17]
# ]
# print("la taille du tableau 1 est de", len(list_notes[0]), "et la moyenne est de : ", statistics.mean(list_notes[0]), "et la taille du tableau 2 est de", len(list_notes[1]), "et la moyenne est de : ", statistics.mean(list_notes[1]))
from ollama import chat, ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': 'well, im not sure because its 16:18 in france for the moment and its 3:18 in NZ" ',
  },
])

print(response['message']['content'])
