import json
import random

data = {1: "Будь собой; все остальные роли уже заняты.", 
        2: "Делай, что можешь, с тем, что у тебя есть, там, где ты находишься.", 
        3: "Жизнь – это то, что с тобой происходит, пока ты строишь планы."}

result = json.dumps(data)

with open('quotes.json', "w", encoding = 'utf-8') as f:
        f.write(result)

with open('quotes.json') as json_file:
        data = json.load(json_file)

print(data[str(random.randrange(1, 4))])