import json
import os

new_rounds = [
    {
        "round_number": 1,
        "title": "Pronoun Basics Challenge",
        "questions": [
            {"type": "mcq", "question": "What does a pronoun replace?", "options": ["Verb", "Noun", "Adjective", "Adverb"], "correct_option_index": 1, "explanation": "Pronouns replace nouns."},
            {"type": "mcq", "question": "Which is a pronoun?", "options": ["Apple", "Quickly", "They", "Happy"], "correct_option_index": 2, "explanation": "'They' is a pronoun."},
            {"type": "mcq", "question": "Why do we use pronouns?", "options": ["To make sentences longer", "To avoid repeating nouns", "To show action", "To describe things"], "correct_option_index": 1, "explanation": "Avoids repetition."},
            {"type": "mcq", "question": "Replace 'Mary' in 'Mary runs fast':", "options": ["He", "She", "It", "They"], "correct_option_index": 1, "explanation": "Mary is female."},
            {"type": "mcq", "question": "Replace 'The dog' in 'The dog barks':", "options": ["He", "She", "It", "They"], "correct_option_index": 2, "explanation": "Animals without known gender take 'it'."},
            {"type": "fib", "question": "Instead of 'The cars', we can use the pronoun ___.", "answer": "they", "explanation": "They is used for plural things."},
            {"type": "fib", "question": "I saw John. I waved at ___.", "answer": "him", "explanation": "Him is the object pronoun for a male."},
            {"type": "fib", "question": "My friends are here. ___ brought pizza.", "answer": "They", "explanation": "They replaces 'My friends'."},
            {"type": "fib", "question": "Where is the book? ___ is on the table.", "answer": "It", "explanation": "It replaces book."},
            {"type": "fib", "question": "A ___ is a word that takes the place of a noun.", "answer": "pronoun", "explanation": "Definition of a pronoun."}
        ]
    },
    {
        "round_number": 2,
        "title": "Personal Pronouns Challenge",
        "questions": [
            {"type": "mcq", "question": "Which is a 1st person plural pronoun?", "options": ["I", "We", "They", "You"], "correct_option_index": 1, "explanation": "We includes the speaker."},
            {"type": "mcq", "question": "Which pronoun is 2nd person?", "options": ["He", "She", "You", "It"], "correct_option_index": 2, "explanation": "You is spoken to."},
            {"type": "mcq", "question": "Replace 'My brother and I':", "options": ["They", "We", "You", "Us"], "correct_option_index": 1, "explanation": "We includes the speaker."},
            {"type": "mcq", "question": "Which pronoun is singular?", "options": ["They", "We", "I", "Ours"], "correct_option_index": 2, "explanation": "I is one person."},
            {"type": "mcq", "question": "Find the pronoun: 'She likes to read.'", "options": ["She", "likes", "to", "read"], "correct_option_index": 0, "explanation": "She is a personal pronoun."},
            {"type": "fib", "question": "___ am going to the store.", "answer": "I", "explanation": "'am' goes with I."},
            {"type": "fib", "question": "Where are ___ going? (asking a friend)", "answer": "you", "explanation": "You is 2nd person."},
            {"type": "fib", "question": "Sarah is my sister. ___ is very smart.", "answer": "She", "explanation": "She replaces Sarah."},
            {"type": "fib", "question": "Mark is late. ___ missed the bus.", "answer": "He", "explanation": "He replaces Mark."},
            {"type": "fib", "question": "The students are studying. ___ have a test.", "answer": "They", "explanation": "They replaces students."}
        ]
    },
    {
        "round_number": 3,
        "title": "Subject & Object Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which is a subject pronoun?", "options": ["Me", "Him", "They", "Us"], "correct_option_index": 2, "explanation": "They does the action."},
            {"type": "mcq", "question": "Which is an object pronoun?", "options": ["I", "She", "We", "Them"], "correct_option_index": 3, "explanation": "Them receives the action."},
            {"type": "mcq", "question": "Choose the correct word: 'He gave it to ___.'", "options": ["I", "me", "he", "they"], "correct_option_index": 1, "explanation": "Me is the object of the preposition."},
            {"type": "mcq", "question": "Choose the correct word: '___ love pizza.'", "options": ["Us", "Them", "Me", "We"], "correct_option_index": 3, "explanation": "We is the subject."},
            {"type": "mcq", "question": "Which acts as both subject and object?", "options": ["I", "He", "You", "We"], "correct_option_index": 2, "explanation": "You remains unchanged."},
            {"type": "fib", "question": "My mom called ___. (I/me)", "answer": "me", "explanation": "Me is the object."},
            {"type": "fib", "question": "___ went to the park. (Us/We)", "answer": "We", "explanation": "We is the subject."},
            {"type": "fib", "question": "I saw ___ at the mall. (he/him)", "answer": "him", "explanation": "Him is the object."},
            {"type": "fib", "question": "___ are my best friends. (They/Them)", "answer": "They", "explanation": "They is the subject."},
            {"type": "fib", "question": "Can you help ___? (we/us)", "answer": "us", "explanation": "Us is the object."}
        ]
    },
    {
        "round_number": 4,
        "title": "Possessive Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which is a possessive pronoun?", "options": ["mine", "my", "me", "I"], "correct_option_index": 0, "explanation": "Mine stands alone."},
            {"type": "mcq", "question": "Complete: 'This book is ___.'", "options": ["her", "hers", "she", "it"], "correct_option_index": 1, "explanation": "Hers stands alone."},
            {"type": "mcq", "question": "Complete: 'The victory is ___.'", "options": ["us", "our", "ours", "we"], "correct_option_index": 2, "explanation": "Ours stands alone."},
            {"type": "mcq", "question": "Which pronoun means 'belonging to them'?", "options": ["their", "they", "them", "theirs"], "correct_option_index": 3, "explanation": "Theirs is the possessive pronoun."},
            {"type": "mcq", "question": "Is 'yours' a possessive pronoun?", "options": ["Yes", "No", "Only plural", "Only singular"], "correct_option_index": 0, "explanation": "Yes, it stands alone."},
            {"type": "fib", "question": "That car belongs to me. It is ___.", "answer": "mine", "explanation": "Shows my ownership."},
            {"type": "fib", "question": "Those shoes belong to him. They are ___.", "answer": "his", "explanation": "Shows his ownership."},
            {"type": "fib", "question": "This house belongs to us. It is ___.", "answer": "ours", "explanation": "Shows our ownership."},
            {"type": "fib", "question": "The money belongs to them. It is ___.", "answer": "theirs", "explanation": "Shows their ownership."},
            {"type": "fib", "question": "Is this phone ___? (belonging to you)", "answer": "yours", "explanation": "Shows your ownership."}
        ]
    },
    {
        "round_number": 5,
        "title": "Possessive Adjectives vs Pronouns",
        "questions": [
            {"type": "mcq", "question": "In 'my car', 'my' is a:", "options": ["Possessive Adjective", "Possessive Pronoun", "Noun", "Verb"], "correct_option_index": 0, "explanation": "It precedes a noun."},
            {"type": "mcq", "question": "In 'the car is mine', 'mine' is a:", "options": ["Possessive Adjective", "Possessive Pronoun", "Noun", "Verb"], "correct_option_index": 1, "explanation": "It stands alone."},
            {"type": "mcq", "question": "Which sentence is correct?", "options": ["This is mine book.", "This is my book.", "This book is my.", "This book is me."], "correct_option_index": 1, "explanation": "My is an adjective followed by book."},
            {"type": "mcq", "question": "Which word acts as BOTH adjective and pronoun?", "options": ["my", "his", "her", "our"], "correct_option_index": 1, "explanation": "His book / The book is his."},
            {"type": "mcq", "question": "Choose the correct word: 'I lost ___ keys.'", "options": ["mine", "my", "me", "I"], "correct_option_index": 1, "explanation": "My is followed by keys."},
            {"type": "fib", "question": "That is ___ dog. (my/mine)", "answer": "my", "explanation": "Adjective modifying dog."},
            {"type": "fib", "question": "That dog is ___. (my/mine)", "answer": "mine", "explanation": "Pronoun standing alone."},
            {"type": "fib", "question": "Where is ___ house? (your/yours)", "answer": "your", "explanation": "Adjective modifying house."},
            {"type": "fib", "question": "Is this house ___? (your/yours)", "answer": "yours", "explanation": "Pronoun standing alone."},
            {"type": "fib", "question": "___ team won the game! (Our/Ours)", "answer": "Our", "explanation": "Adjective modifying team."}
        ]
    },
    {
        "round_number": 6,
        "title": "Reflexive Pronouns",
        "questions": [
            {"type": "mcq", "question": "Reflexive pronouns end in:", "options": ["-ly", "-ed", "-self / -selves", "-ing"], "correct_option_index": 2, "explanation": "They reflect back to the subject."},
            {"type": "mcq", "question": "Complete: 'I cut ___.'", "options": ["me", "mine", "myself", "I"], "correct_option_index": 2, "explanation": "Subject and object are the same (I)."},
            {"type": "mcq", "question": "Plural of yourself is:", "options": ["yourselfs", "yourselves", "your", "yours"], "correct_option_index": 1, "explanation": "Change f to v and add es."},
            {"type": "mcq", "question": "Complete: 'They built it ___.'", "options": ["themselfs", "theirselves", "themselves", "them"], "correct_option_index": 2, "explanation": "Themselves is the correct form."},
            {"type": "mcq", "question": "Is 'hisself' a real word?", "options": ["Yes", "No", "Only in British English", "Only in slang"], "correct_option_index": 1, "explanation": "The correct word is 'himself'."},
            {"type": "fib", "question": "She looked at ___ in the mirror.", "answer": "herself", "explanation": "Reflects back to she."},
            {"type": "fib", "question": "We cooked dinner all by ___.", "answer": "ourselves", "explanation": "Reflects back to we."},
            {"type": "fib", "question": "He taught ___ how to code.", "answer": "himself", "explanation": "Reflects back to he."},
            {"type": "fib", "question": "The cat washed ___.", "answer": "itself", "explanation": "Reflects back to cat (it)."},
            {"type": "fib", "question": "Did you make this ___? (talking to one person)", "answer": "yourself", "explanation": "Singular you."}
        ]
    },
    {
        "round_number": 7,
        "title": "Demonstrative Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which points to a singular object near you?", "options": ["This", "That", "These", "Those"], "correct_option_index": 0, "explanation": "This = singular, near."},
            {"type": "mcq", "question": "Which points to plural objects far away?", "options": ["This", "That", "These", "Those"], "correct_option_index": 3, "explanation": "Those = plural, far."},
            {"type": "mcq", "question": "Which pair is plural?", "options": ["This, That", "These, Those", "This, These", "That, Those"], "correct_option_index": 1, "explanation": "These and Those are plural."},
            {"type": "mcq", "question": "Complete: '___ is my favorite song.'", "options": ["This", "These", "Those", "Them"], "correct_option_index": 0, "explanation": "Song is singular."},
            {"type": "mcq", "question": "In 'That is cool', 'That' is a:", "options": ["Demonstrative Adjective", "Demonstrative Pronoun", "Noun", "Verb"], "correct_option_index": 1, "explanation": "It stands alone as a pronoun."},
            {"type": "fib", "question": "___ are my shoes right here.", "answer": "These", "explanation": "Plural and near."},
            {"type": "fib", "question": "Look at ___ stars up in the sky!", "answer": "those", "explanation": "Plural and far."},
            {"type": "fib", "question": "Was ___ your brother who just left?", "answer": "that", "explanation": "Singular and far (left)."},
            {"type": "fib", "question": "Hold ___ for a second. (handing an object)", "answer": "this", "explanation": "Singular and near."},
            {"type": "fib", "question": "___ is the best pizza I've ever had!", "answer": "This", "explanation": "Singular and currently eating it."}
        ]
    },
    {
        "round_number": 8,
        "title": "Interrogative Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which asks about a person doing an action?", "options": ["What", "Which", "Who", "Whose"], "correct_option_index": 2, "explanation": "Who is the subject."},
            {"type": "mcq", "question": "Which asks about ownership?", "options": ["Who", "Whom", "Whose", "What"], "correct_option_index": 2, "explanation": "Whose means 'belonging to who'."},
            {"type": "mcq", "question": "Which is used for making a choice?", "options": ["What", "Which", "Who", "Whom"], "correct_option_index": 1, "explanation": "Which of these two?"},
            {"type": "mcq", "question": "Which asks about a person receiving an action?", "options": ["Who", "Whom", "Whose", "What"], "correct_option_index": 1, "explanation": "Whom is the object."},
            {"type": "mcq", "question": "Identify the interrogative pronoun: 'What is that?'", "options": ["What", "is", "that", "None"], "correct_option_index": 0, "explanation": "What asks the question."},
            {"type": "fib", "question": "___ is at the door?", "answer": "Who", "explanation": "Asking for a person."},
            {"type": "fib", "question": "___ did you call last night?", "answer": "Whom", "explanation": "Object of the calling."},
            {"type": "fib", "question": "___ shoes are these?", "answer": "Whose", "explanation": "Asking ownership."},
            {"type": "fib", "question": "___ is your favorite color?", "answer": "What", "explanation": "Asking for a thing."},
            {"type": "fib", "question": "___ of these two shirts is better?", "answer": "Which", "explanation": "Making a choice."}
        ]
    },
    {
        "round_number": 9,
        "title": "Indefinite Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which is an indefinite pronoun?", "options": ["He", "Someone", "Which", "Myself"], "correct_option_index": 1, "explanation": "Does not specify exactly who."},
            {"type": "mcq", "question": "Are pronouns ending in -body usually singular or plural?", "options": ["Singular", "Plural", "Both", "Neither"], "correct_option_index": 0, "explanation": "Everybody IS here."},
            {"type": "mcq", "question": "Complete: 'Everyone ___ happy.'", "options": ["is", "are", "am", "be"], "correct_option_index": 0, "explanation": "Everyone takes a singular verb."},
            {"type": "mcq", "question": "Which means 'no people'?", "options": ["Nothing", "Nobody", "Nowhere", "None"], "correct_option_index": 1, "explanation": "No + body (person)."},
            {"type": "mcq", "question": "Which means 'no things'?", "options": ["Nothing", "Nobody", "Nowhere", "None"], "correct_option_index": 0, "explanation": "No + thing."},
            {"type": "fib", "question": "I have looked ___ for my phone.", "answer": "everywhere", "explanation": "All places."},
            {"type": "fib", "question": "Does ___ have a pencil?", "answer": "anyone", "explanation": "Any person."},
            {"type": "fib", "question": "I have ___ to wear!", "answer": "nothing", "explanation": "Zero things."},
            {"type": "fib", "question": "___ is perfect.", "answer": "Nobody", "explanation": "Zero people."},
            {"type": "fib", "question": "Is there ___ good on TV?", "answer": "anything", "explanation": "Any thing."}
        ]
    },
    {
        "round_number": 10,
        "title": "Relative Pronouns",
        "questions": [
            {"type": "mcq", "question": "Which relative pronoun is used ONLY for people?", "options": ["Which", "That", "Who", "What"], "correct_option_index": 2, "explanation": "Who refers to people."},
            {"type": "mcq", "question": "Which is used ONLY for things/animals?", "options": ["Who", "Whom", "Which", "Whose"], "correct_option_index": 2, "explanation": "Which refers to things."},
            {"type": "mcq", "question": "Which can be used for BOTH people and things?", "options": ["Who", "Which", "That", "Whom"], "correct_option_index": 2, "explanation": "The man that... The car that..."},
            {"type": "mcq", "question": "Complete: 'The boy ___ dog ran away is sad.'", "options": ["who", "which", "whose", "whom"], "correct_option_index": 2, "explanation": "Whose shows ownership of the dog."},
            {"type": "mcq", "question": "Identify the relative pronoun: 'The book that I read was good.'", "options": ["The", "book", "that", "good"], "correct_option_index": 2, "explanation": "That connects the clauses."},
            {"type": "fib", "question": "The woman ___ won the lottery is rich.", "answer": "who", "explanation": "Refers to the woman."},
            {"type": "fib", "question": "The car ___ I bought is blue.", "answer": "which", "explanation": "Refers to the car."},
            {"type": "fib", "question": "The girl ___ purse was stolen cried.", "answer": "whose", "explanation": "Ownership of the purse."},
            {"type": "fib", "question": "He is the only one ___ can save us.", "answer": "who", "explanation": "Refers to the person."},
            {"type": "fib", "question": "I found the keys ___ I lost yesterday.", "answer": "that", "explanation": "Refers to the keys (things)."}
        ]
    }
]

with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find or create Pronoun topic in challenge rounds
topic = next((t for t in data['topics'] if t['name'] == 'Pronoun'), None)
if not topic:
    topic = {
        "name": "Pronoun",
        "rounds": []
    }
    data['topics'].append(topic)

existing_rounds = [r['round_number'] for r in topic['rounds']]
for nr in new_rounds:
    if nr['round_number'] not in existing_rounds:
        topic['rounds'].append(nr)
        
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added all 10 Pronoun challenge rounds successfully!")
