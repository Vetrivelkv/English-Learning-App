import json
import os

new_rounds = [
    {
        "round_number": 1,
        "title": "Verbs Basics",
        "questions": [
            {"type": "mcq", "question": "What part of speech shows action or state of being?", "options": ["Noun", "Pronoun", "Verb", "Adjective"], "correct_option_index": 2, "explanation": "Verbs show action/being."},
            {"type": "mcq", "question": "Which is an action verb?", "options": ["is", "am", "run", "were"], "correct_option_index": 2, "explanation": "Run is physical."},
            {"type": "mcq", "question": "Which is a state of being verb?", "options": ["are", "eat", "jump", "sleep"], "correct_option_index": 0, "explanation": "Are shows existence."},
            {"type": "mcq", "question": "Find the verb: 'He writes fast.'", "options": ["He", "writes", "fast", "None"], "correct_option_index": 1, "explanation": "Writes is the action."},
            {"type": "mcq", "question": "Find the verb: 'They were late.'", "options": ["They", "were", "late", "None"], "correct_option_index": 1, "explanation": "Were is the state of being."},
            {"type": "fib", "question": "She ___ a great singer. (is/jump)", "options": ["is", "jump", "she", "singer"], "correct_option_index": 0, "explanation": "'is' describes her state."},
            {"type": "fib", "question": "I ___ to the music. (listen/am)", "options": ["listen", "am", "music", "I"], "correct_option_index": 0, "explanation": "Listen is an action."},
            {"type": "fib", "question": "The dog ___ loudly. (barked/was)", "options": ["barked", "was", "dog", "loudly"], "correct_option_index": 0, "explanation": "Barked is an action."},
            {"type": "fib", "question": "We ___ happy today. (are/play)", "options": ["are", "play", "we", "happy"], "correct_option_index": 0, "explanation": "'are' connects we to happy."},
            {"type": "fib", "question": "The sun ___ brightly. (shines/is)", "options": ["shines", "is", "sun", "brightly"], "correct_option_index": 0, "explanation": "Shines is the action."}
        ]
    },
    {
        "round_number": 2,
        "title": "Action vs Linking",
        "questions": [
            {"type": "mcq", "question": "What does a linking verb do?", "options": ["Shows action", "Connects subject to describing word", "Acts as object", "Ends a sentence"], "correct_option_index": 1, "explanation": "It links subject to a noun/adjective."},
            {"type": "mcq", "question": "In 'The cake tastes good', 'tastes' is:", "options": ["Action", "Linking", "Helping", "None"], "correct_option_index": 1, "explanation": "Cake = good."},
            {"type": "mcq", "question": "In 'I tasted the cake', 'tasted' is:", "options": ["Action", "Linking", "Helping", "None"], "correct_option_index": 0, "explanation": "Physical action done by I."},
            {"type": "mcq", "question": "Which is ALWAYS a linking verb?", "options": ["feel", "smell", "is", "appear"], "correct_option_index": 2, "explanation": "'is' never shows action."},
            {"type": "mcq", "question": "Identify the linking verb: 'She seems tired.'", "options": ["She", "seems", "tired", "None"], "correct_option_index": 1, "explanation": "Seems connects she to tired."},
            {"type": "fib", "question": "The soup ___ delicious. (smells/eats)", "options": ["smells", "eats", "soup", "delicious"], "correct_option_index": 0, "explanation": "Smells is linking here."},
            {"type": "fib", "question": "He ___ the ball. (threw/was)", "options": ["threw", "was", "he", "ball"], "correct_option_index": 0, "explanation": "Threw is an action."},
            {"type": "fib", "question": "I ___ cold. (feel/run)", "options": ["feel", "run", "I", "cold"], "correct_option_index": 0, "explanation": "Feel is linking here."},
            {"type": "fib", "question": "They ___ best friends. (became/walked)", "options": ["became", "walked", "they", "friends"], "correct_option_index": 0, "explanation": "Became is linking."},
            {"type": "fib", "question": "She ___ beautiful today. (looks/sees)", "options": ["looks", "sees", "she", "beautiful"], "correct_option_index": 0, "explanation": "Looks is linking here."}
        ]
    },
    {
        "round_number": 3,
        "title": "Helping Verbs",
        "questions": [
            {"type": "mcq", "question": "What comes BEFORE the main verb to show tense?", "options": ["Noun", "Adjective", "Helping Verb", "Adverb"], "correct_option_index": 2, "explanation": "Helping verbs assist main verbs."},
            {"type": "mcq", "question": "In 'I am eating', what is 'am'?", "options": ["Main Verb", "Helping Verb", "Noun", "Pronoun"], "correct_option_index": 1, "explanation": "It helps eating."},
            {"type": "mcq", "question": "In 'She has left', what is the main verb?", "options": ["She", "has", "left", "None"], "correct_option_index": 2, "explanation": "Left is the main action."},
            {"type": "mcq", "question": "Which is a helping verb in 'He will win'?", "options": ["He", "will", "win", "None"], "correct_option_index": 1, "explanation": "Will helps win."},
            {"type": "mcq", "question": "Can 'is' be a helping verb?", "options": ["Yes", "No", "Only main", "Never"], "correct_option_index": 0, "explanation": "Yes, e.g., 'He is running'."},
            {"type": "fib", "question": "They ___ playing soccer. (are/jump)", "options": ["are", "jump", "they", "playing"], "correct_option_index": 0, "explanation": "Are is the helping verb."},
            {"type": "fib", "question": "I ___ not see him. (did/running)", "options": ["did", "running", "I", "not"], "correct_option_index": 0, "explanation": "Did helps see."},
            {"type": "fib", "question": "We ___ been waiting. (have/are)", "options": ["have", "are", "we", "waiting"], "correct_option_index": 0, "explanation": "Have helps been waiting."},
            {"type": "fib", "question": "She ___ be sleeping. (could/went)", "options": ["could", "went", "she", "sleeping"], "correct_option_index": 0, "explanation": "Could helps be sleeping."},
            {"type": "fib", "question": "The dog ___ barking loudly. (was/barked)", "options": ["was", "barked", "dog", "loudly"], "correct_option_index": 0, "explanation": "Was helps barking."}
        ]
    },
    {
        "round_number": 4,
        "title": "Transitive vs Intransitive",
        "questions": [
            {"type": "mcq", "question": "A transitive verb must have a ___.", "options": ["Subject", "Direct Object", "Adverb", "Adjective"], "correct_option_index": 1, "explanation": "It transfers action to an object."},
            {"type": "mcq", "question": "In 'He read a book', 'read' is:", "options": ["Transitive", "Intransitive", "Linking", "Helping"], "correct_option_index": 0, "explanation": "Read what? A book."},
            {"type": "mcq", "question": "In 'The baby cried', 'cried' is:", "options": ["Transitive", "Intransitive", "Linking", "Helping"], "correct_option_index": 1, "explanation": "No direct object."},
            {"type": "mcq", "question": "Identify the direct object: 'She painted the wall.'", "options": ["She", "painted", "the", "wall"], "correct_option_index": 3, "explanation": "The wall receives the paint."},
            {"type": "mcq", "question": "Which sentence is intransitive?", "options": ["I eat lunch.", "He drove a car.", "They arrived.", "She wrote a poem."], "correct_option_index": 2, "explanation": "Arrived has no object."},
            {"type": "fib", "question": "I bought a car. 'Bought' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "I", "car"], "correct_option_index": 0, "explanation": "Bought what? A car."},
            {"type": "fib", "question": "He laughed loudly. 'Laughed' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "he", "loudly"], "correct_option_index": 1, "explanation": "No object."},
            {"type": "fib", "question": "She baked a cake. 'Baked' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "she", "cake"], "correct_option_index": 0, "explanation": "Baked what? A cake."},
            {"type": "fib", "question": "The sun set. 'Set' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "sun", "set"], "correct_option_index": 1, "explanation": "No object."},
            {"type": "fib", "question": "Transitive verbs answer the question '___?'", "options": ["Why", "Where", "What", "When"], "correct_option_index": 2, "explanation": "What or who."}
        ]
    },
    {
        "round_number": 5,
        "title": "Regular vs Irregular Verbs",
        "questions": [
            {"type": "mcq", "question": "Regular verbs in past tense end in:", "options": ["-ing", "-s", "-ed", "-ly"], "correct_option_index": 2, "explanation": "Standard rule is -ed."},
            {"type": "mcq", "question": "Which is a regular verb?", "options": ["eat", "go", "jump", "see"], "correct_option_index": 2, "explanation": "Jumped."},
            {"type": "mcq", "question": "Which is an irregular verb?", "options": ["walk", "talk", "run", "look"], "correct_option_index": 2, "explanation": "Ran."},
            {"type": "mcq", "question": "Past tense of 'buy':", "options": ["buyed", "bought", "bring", "brought"], "correct_option_index": 1, "explanation": "Bought."},
            {"type": "mcq", "question": "Past tense of 'catch':", "options": ["catched", "caught", "cot", "catch"], "correct_option_index": 1, "explanation": "Caught."},
            {"type": "fib", "question": "Past tense of 'work' is ___. (regular)", "options": ["worked", "worken", "wrought", "working"], "correct_option_index": 0, "explanation": "Worked."},
            {"type": "fib", "question": "Past tense of 'sing' is ___. (irregular)", "options": ["singed", "sang", "sung", "singing"], "correct_option_index": 1, "explanation": "Sang."},
            {"type": "fib", "question": "Past tense of 'go' is ___.", "options": ["goed", "went", "gone", "going"], "correct_option_index": 1, "explanation": "Went."},
            {"type": "fib", "question": "Past tense of 'close' is ___.", "options": ["closed", "cloze", "close", "closing"], "correct_option_index": 0, "explanation": "Closed."},
            {"type": "fib", "question": "Past tense of 'think' is ___.", "options": ["thinked", "thought", "thunk", "think"], "correct_option_index": 1, "explanation": "Thought."}
        ]
    }
]

with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

topic = next((t for t in data['topics'] if t['name'] == 'Verb'), None)
if not topic:
    topic = {
        "name": "Verb",
        "rounds": []
    }
    data['topics'].append(topic)

existing_rounds = [r['round_number'] for r in topic['rounds']]
for nr in new_rounds:
    if nr['round_number'] not in existing_rounds:
        topic['rounds'].append(nr)
        
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added Verb challenge rounds 1 to 5 successfully!")
