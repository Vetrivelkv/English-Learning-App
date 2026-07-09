import json
import os

new_rounds = []

# Round 4: Countable & Uncountable Nouns
new_rounds.append({
    "round_number": 4,
    "title": "Countable vs Uncountable Challenge",
    "questions": [
        {"type": "mcq", "question": "Which of these is an uncountable noun?", "options": ["apple", "water", "car", "dog"], "correct_option_index": 1, "explanation": "Water cannot be counted individually."},
        {"type": "mcq", "question": "Which of these is a countable noun?", "options": ["information", "knowledge", "book", "rice"], "correct_option_index": 2, "explanation": "You can count books (one book, two books)."},
        {"type": "mcq", "question": "Identify the correct usage:", "options": ["two milks", "some milk", "a milk", "many milks"], "correct_option_index": 1, "explanation": "Milk is uncountable, so we say 'some milk'."},
        {"type": "mcq", "question": "Which word takes 'much' instead of 'many'?", "options": ["time", "clocks", "minutes", "hours"], "correct_option_index": 0, "explanation": "'Time' is an uncountable concept."},
        {"type": "mcq", "question": "Which sentence is correct?", "options": ["I have many homeworks.", "I have much homework.", "I have a homework.", "I have two homeworks."], "correct_option_index": 1, "explanation": "Homework is uncountable."},
        {"type": "fib", "question": "He gave me a good piece of ___.", "answer": "advice", "explanation": "Advice is uncountable, so we say 'a piece of advice'."},
        {"type": "fib", "question": "How ___ money do you have?", "answer": "much", "explanation": "Money is uncountable."},
        {"type": "fib", "question": "How ___ dollars do you have?", "answer": "many", "explanation": "Dollars are countable."},
        {"type": "fib", "question": "I bought three ___ of bread.", "answer": "loaves", "explanation": "Bread is uncountable, but 'loaves' are countable units."},
        {"type": "fib", "question": "The ___ is terrible today. (weather / weathers)", "answer": "weather", "explanation": "Weather is uncountable."}
    ]
})

# Round 5: Compound Nouns
new_rounds.append({
    "round_number": 5,
    "title": "Compound Nouns Mastery",
    "questions": [
        {"type": "mcq", "question": "Which is a compound noun?", "options": ["running", "quickly", "sunflower", "beautiful"], "correct_option_index": 2, "explanation": "sun + flower"},
        {"type": "mcq", "question": "Which is a hyphenated compound noun?", "options": ["ice cream", "mother-in-law", "bedroom", "football"], "correct_option_index": 1, "explanation": "It uses hyphens."},
        {"type": "mcq", "question": "What two words make 'breakfast'?", "options": ["break + fast", "brave + fast", "break + first", "bread + fast"], "correct_option_index": 0, "explanation": "Breaking the fast."},
        {"type": "mcq", "question": "Which sentence has a compound noun?", "options": ["The cat is black.", "I lost my toothbrush.", "He is very tall.", "She sings well."], "correct_option_index": 1, "explanation": "tooth + brush"},
        {"type": "mcq", "question": "Plural of 'passer-by' is:", "options": ["passer-bys", "passers-by", "passers-bys", "passer-byes"], "correct_option_index": 1, "explanation": "Pluralize the main word 'passer'."},
        {"type": "fib", "question": "A board with keys is a ___.", "answer": "keyboard", "explanation": "key + board"},
        {"type": "fib", "question": "A room for a bed is a ___.", "answer": "bedroom", "explanation": "bed + room"},
        {"type": "fib", "question": "The print of a foot is a ___.", "answer": "footprint", "explanation": "foot + print"},
        {"type": "fib", "question": "A brush for hair is a ___.", "answer": "hairbrush", "explanation": "hair + brush"},
        {"type": "fib", "question": "The light from the moon is ___.", "answer": "moonlight", "explanation": "moon + light"}
    ]
})

# Round 6: Noun Genders
new_rounds.append({
    "round_number": 6,
    "title": "Noun Genders Challenge",
    "questions": [
        {"type": "mcq", "question": "Which is a feminine noun?", "options": ["actor", "actress", "doctor", "king"], "correct_option_index": 1, "explanation": "Female form of actor."},
        {"type": "mcq", "question": "Which is a masculine noun?", "options": ["aunt", "queen", "uncle", "niece"], "correct_option_index": 2, "explanation": "Male relative."},
        {"type": "mcq", "question": "Which is a common gender noun?", "options": ["lion", "lioness", "cub", "teacher"], "correct_option_index": 3, "explanation": "Teacher can be male or female."},
        {"type": "mcq", "question": "Which is a neuter noun?", "options": ["table", "brother", "sister", "baby"], "correct_option_index": 0, "explanation": "Table is an inanimate object."},
        {"type": "mcq", "question": "Feminine of 'hero' is:", "options": ["heros", "heroine", "shero", "heron"], "correct_option_index": 1, "explanation": "Heroine is the female hero."},
        {"type": "fib", "question": "The male version of queen is ___.", "answer": "king", "explanation": "King is masculine."},
        {"type": "fib", "question": "The female version of brother is ___.", "answer": "sister", "explanation": "Sister is feminine."},
        {"type": "fib", "question": "The male version of wife is ___.", "answer": "husband", "explanation": "Husband is masculine."},
        {"type": "fib", "question": "The female version of nephew is ___.", "answer": "niece", "explanation": "Niece is feminine."},
        {"type": "fib", "question": "A non-living thing like a car has a ___ gender.", "answer": "neuter", "explanation": "Neuter means neither male nor female."}
    ]
})

# Round 7: Noun Cases
new_rounds.append({
    "round_number": 7,
    "title": "Subjective & Objective Cases",
    "questions": [
        {"type": "mcq", "question": "In 'The dog bit the man', 'dog' is:", "options": ["Subjective", "Objective", "Possessive", "None"], "correct_option_index": 0, "explanation": "Dog is doing the action."},
        {"type": "mcq", "question": "In 'The dog bit the man', 'man' is:", "options": ["Subjective", "Objective", "Possessive", "None"], "correct_option_index": 1, "explanation": "Man is receiving the action."},
        {"type": "mcq", "question": "In 'John's car is fast', 'John's' is:", "options": ["Subjective", "Objective", "Possessive", "None"], "correct_option_index": 2, "explanation": "Shows ownership."},
        {"type": "mcq", "question": "Subjective case is also called:", "options": ["Nominative", "Accusative", "Genitive", "Dative"], "correct_option_index": 0, "explanation": "Nominative means subject."},
        {"type": "mcq", "question": "Which sentence has an objective noun?", "options": ["I sleep.", "She cries.", "He kicked the ball.", "They laugh."], "correct_option_index": 2, "explanation": "The ball receives the kick."},
        {"type": "fib", "question": "A noun that DOES the action is in the ___ case.", "answer": "subjective", "explanation": "Subject does the action."},
        {"type": "fib", "question": "A noun that RECEIVES the action is in the ___ case.", "answer": "objective", "explanation": "Object receives the action."},
        {"type": "fib", "question": "A noun showing OWNERSHIP is in the ___ case.", "answer": "possessive", "explanation": "Possessive means ownership."},
        {"type": "fib", "question": "In 'She likes cats', 'cats' is in the ___ case.", "answer": "objective", "explanation": "Cats receive the liking."},
        {"type": "fib", "question": "In 'Birds fly', 'Birds' is in the ___ case.", "answer": "subjective", "explanation": "Birds do the flying."}
    ]
})

# Round 8: Appositive Nouns
new_rounds.append({
    "round_number": 8,
    "title": "Appositives Mastery",
    "questions": [
        {"type": "mcq", "question": "What is an appositive?", "options": ["A verb", "A noun renaming another noun", "An adjective", "A pronoun"], "correct_option_index": 1, "explanation": "Appositives rename nouns."},
        {"type": "mcq", "question": "Find the appositive: 'My friend, Tom, is here.'", "options": ["My", "friend", "Tom", "here"], "correct_option_index": 2, "explanation": "Tom renames friend."},
        {"type": "mcq", "question": "Find the appositive: 'We visited Paris, the capital of France.'", "options": ["We", "visited", "Paris", "the capital of France"], "correct_option_index": 3, "explanation": "Renames Paris."},
        {"type": "mcq", "question": "Appositives are often separated by:", "options": ["Periods", "Commas", "Hyphens", "Question marks"], "correct_option_index": 1, "explanation": "Commas surround non-essential appositives."},
        {"type": "mcq", "question": "Does this sentence have an appositive? 'The car is red.'", "options": ["Yes", "No", "Maybe", "Only in British English"], "correct_option_index": 1, "explanation": "No noun renaming another noun."},
        {"type": "fib", "question": "An appositive ___ another noun right next to it.", "answer": "renames", "explanation": "It provides a second name/description."},
        {"type": "fib", "question": "In 'The insect, a bee, stung me', the appositive is 'a ___'.", "answer": "bee", "explanation": "Bee renames insect."},
        {"type": "fib", "question": "In 'My brother Jack is tall', the appositive is ___.", "answer": "Jack", "explanation": "Jack renames brother."},
        {"type": "fib", "question": "Appositives add extra ___ about the noun.", "answer": "information", "explanation": "Provides clarity or description."},
        {"type": "fib", "question": "In 'Our planet, Earth, is round', the appositive is ___.", "answer": "Earth", "explanation": "Earth renames our planet."}
    ]
})

# Round 9: Gerunds
new_rounds.append({
    "round_number": 9,
    "title": "Gerunds (Verbal Nouns)",
    "questions": [
        {"type": "mcq", "question": "What is a gerund?", "options": ["A noun ending in -ed", "A verb ending in -ing acting as a noun", "An adjective", "An adverb"], "correct_option_index": 1, "explanation": "Verbal noun."},
        {"type": "mcq", "question": "Find the gerund: 'Running is fun.'", "options": ["Running", "is", "fun", "None"], "correct_option_index": 0, "explanation": "Running acts as the subject noun."},
        {"type": "mcq", "question": "Is there a gerund here? 'She is running.'", "options": ["Yes, She", "Yes, running", "Yes, is", "No"], "correct_option_index": 3, "explanation": "Running is just a verb here, not a noun."},
        {"type": "mcq", "question": "Find the gerund: 'I love painting.'", "options": ["I", "love", "painting", "None"], "correct_option_index": 2, "explanation": "Painting is the object noun."},
        {"type": "mcq", "question": "Gerunds always end in:", "options": ["-ed", "-s", "-ly", "-ing"], "correct_option_index": 3, "explanation": "Always -ing."},
        {"type": "fib", "question": "Because they come from verbs, gerunds are called ___ nouns.", "answer": "verbal", "explanation": "Verbal nouns."},
        {"type": "fib", "question": "In 'Swimming is great', the gerund is ___.", "answer": "Swimming", "explanation": "Swimming is the subject."},
        {"type": "fib", "question": "In 'He enjoys reading', the gerund is ___.", "answer": "reading", "explanation": "Reading is the object."},
        {"type": "fib", "question": "Gerunds function exactly like ___ in a sentence.", "answer": "nouns", "explanation": "They can be subjects or objects."},
        {"type": "fib", "question": "In 'Smoking is bad', the gerund is ___.", "answer": "Smoking", "explanation": "Smoking acts as a noun."}
    ]
})

# Round 10: Ultimate Noun Boss Battle
new_rounds.append({
    "round_number": 10,
    "title": "Ultimate Nouns Boss Battle",
    "questions": [
        {"type": "mcq", "question": "Identify the proper noun:", "options": ["city", "London", "town", "village"], "correct_option_index": 1, "explanation": "Capitalized specific place."},
        {"type": "mcq", "question": "Identify the collective noun:", "options": ["team", "players", "game", "stadium"], "correct_option_index": 0, "explanation": "Group of individuals."},
        {"type": "mcq", "question": "Identify the abstract noun:", "options": ["apple", "table", "happiness", "car"], "correct_option_index": 2, "explanation": "Cannot be touched/seen."},
        {"type": "mcq", "question": "Plural of 'mouse':", "options": ["mouses", "mice", "meese", "mouse"], "correct_option_index": 1, "explanation": "Irregular plural."},
        {"type": "mcq", "question": "Identify the compound noun:", "options": ["sunlight", "quickly", "running", "happily"], "correct_option_index": 0, "explanation": "sun + light"},
        {"type": "fib", "question": "A noun that renames another is an ___.", "answer": "appositive", "explanation": "Appositive renames."},
        {"type": "fib", "question": "Water is a/an ___ noun. (countable / uncountable)", "answer": "uncountable", "explanation": "Cannot be counted."},
        {"type": "fib", "question": "The case showing ownership is ___.", "answer": "possessive", "explanation": "Possessive shows ownership."},
        {"type": "fib", "question": "A verb ending in -ing acting as a noun is a ___.", "answer": "gerund", "explanation": "Definition of gerund."},
        {"type": "fib", "question": "A ___ noun always starts with a capital letter.", "answer": "proper", "explanation": "Proper nouns are capitalized."}
    ]
})

with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Noun topic
topic = next((t for t in data['topics'] if t['name'] == 'Noun'), None)
if topic:
    existing_rounds = [r['round_number'] for r in topic['rounds']]
    for nr in new_rounds:
        if nr['round_number'] not in existing_rounds:
            topic['rounds'].append(nr)
            
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added Noun challenge rounds 4 to 10 successfully!")
