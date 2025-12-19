import random
words_list = ["account", "act", "addition", "adjustment", "advertisement", "agreement", "air", "amount", "amusement",
"animal", "answer", "apparatus", "approval", "argument", "art"," attack", "attempt", "attention", "attraction",
"authority", "back", "balance", "base", "behaviour", "belief", "birth", "bit", "bite", "blood", "blow", "body", 
"brass", "bread", "breath", "brother", "building", "burn", "burst", "business", "butter", "canvas", 'care', "cause", "chalk", "chance", "change",
"cloth", "coal", "colour", "comfort", "committee", "company", "comparison", "competition", "condition", "connection", "control", "cook"
"copper", "copy", "cork", "cotton", "cough", "country", "cover", "crack", "credit", "crime", "crush", "cry", "current", "curve", "damage", "danger",
"daughter", "day", "death", "debt", "decision", "degree", "design", "desire", "destruction", "detail", 'development', "digestion", "direction",
"discovery", "discussion", "disease", "disgust", "distance", "distribution", "division", "doubt", "drink", "driving", "dust", "earth", "edge",
"education", 'effect', "end", "error", "event", "example", "exchange", 'existence', "expansion", "experience", "expert", "fact", "fall", "family", 
"father", "fear", "feeling", "fiction", "field", "fight", "fire", "flame", "flight", "flower", "fold", "food", "force", "form", "friend", "front", "fruit"
"glass", "gold", "government", "grain", "grass", "grip", "group", "growth", "guide", "harbour", "harmony", "hate", "hearing", "heat", "help", "history", "hole", "hope", "hour", "humour", "ice", "idea",
 "impulse", "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", "invention", "iron", "jelly", "join", "journey", "judge", "jump", "kick", "kiss", "knowledge", "land", 
 "language", "laugh", "law", "lead", "learning", "leather", "letter", "level", "lift", "light", "limit", "linen", "liquid", "list", "look", "loss", "love", "machine", "man", "manager", "mark", "market", 
 "mass", "meal", "measure", "meat", "meeting", "memory", "metal", "middle", "milk", "mind", "mine", "minute", "mist", "money", "month", "morning", "mother", "motion", "mountain", "move", "music", "name",
  "nation", "need", "news", "night", "noise", "note", "number", "observation", "offer", "oil", "operation", "opinion", "order", "organization", "ornament", "owner"]

word = random.choice(words_list)
done = False
word_dict = {}
guesses = 6
answer = ''
loop = True
for letter in word:
    word_dict[letter] = "not guessed"
while not done:
    if len(answer) == 1 and not(answer in word) :
        guesses -= 1
    if len(answer) > 1:
        print("Error: You can't input a word")
    if guesses == 0:
        done = True
    else:
        for letter in word:
            if (letter in answer.lower() and len(answer) == 1 and guesses > 0):
                word_dict[letter] = "guessed"
        if (all(key == "guessed" for key in word_dict.values())):
            pass
        else:
            for letter in word:
                if (word_dict[letter] == "guessed" and guesses > 0):
                    print(letter, end = " ")
                else:
                    print("_", end = " ")
    if (all(key == "guessed" for key in word_dict.values())):
        print(f'Congratulations! You guessed the word {word}')
        done = True
    elif guesses == 0:
        print(f'The word was "{word}"')
        done = True
    else:
        answer = input(f'Guess a letter(guesses left {guesses})')
