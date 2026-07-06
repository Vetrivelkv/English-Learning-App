import json
import os

new_subtopics = [
    {
        "id": "pronoun_sub_1",
        "title": "Introduction to Pronouns",
        "image": "assets/pronoun_intro.jpg",
        "content": "### What is a Pronoun?\n\nA **Pronoun** is a word that takes the place of a noun. We use pronouns so we don't have to repeat the same noun over and over again.\n- *Without Pronoun:* John said that John lost John's keys.\n- *With Pronoun:* John said that **he** lost **his** keys.\n\nPronouns make our sentences smoother and less repetitive.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**பிரதிபெயர்ச்சொல் (Pronoun) என்றால் என்ன?**\n\nபெயர்ச்சொல்லுக்கு (Noun) பதிலாகப் பயன்படுத்தப்படும் சொல் பிரதிபெயர்ச்சொல் ஆகும். ஒரே பெயரைத் திரும்பத் திரும்பச் சொல்வதைத் தவிர்க்க இது உதவுகிறது.\n- *எ.கா:* ராமன் நல்ல பையன். **அவன்** தினமும் பள்ளிக்குச் செல்வான். (இங்கு 'அவன்' என்பது Pronoun).",
        "questions": [
            {"type": "mcq", "question": "What is the main purpose of a pronoun?", "options": ["To describe a noun", "To replace a noun", "To show action", "To connect sentences"], "correct": 1, "explanation": "Pronouns take the place of nouns."},
            {"type": "mcq", "question": "Identify the pronoun: 'She is my best friend.'", "options": ["She", "is", "my", "friend"], "correct": 0, "explanation": "'She' replaces a female's name."},
            {"type": "mcq", "question": "Which of the following is NOT a pronoun?", "options": ["He", "It", "They", "Apple"], "correct": 3, "explanation": "'Apple' is a noun."},
            {"type": "fill", "question": "Instead of saying 'The dog barked because the dog was hungry', we can say 'The dog barked because ___ was hungry.'", "options": ["it", "she", "he", "they"], "correct": 0, "explanation": "'it' is usually used for animals unless gender is known."},
            {"type": "fill", "question": "A ___ replaces a noun to avoid repetition.", "options": ["verb", "pronoun", "adjective", "adverb"], "correct": 1, "explanation": "That is the definition of a pronoun."},
            {"type": "mcq", "question": "Identify the pronoun: 'We are going to the park.'", "options": ["We", "going", "to", "park"], "correct": 0, "explanation": "'We' replaces a group of people including the speaker."},
            {"type": "mcq", "question": "Which sentence uses a pronoun?", "options": ["The cat sleeps.", "He is sleeping.", "Mary eats pizza.", "Cars run fast."], "correct": 1, "explanation": "'He' is a pronoun."},
            {"type": "mcq", "question": "Identify the pronoun: 'Did you see the movie?'", "options": ["Did", "you", "see", "movie"], "correct": 1, "explanation": "'you' is the pronoun."},
            {"type": "fill", "question": "Instead of 'Mary and John', you can use the pronoun ___.", "options": ["he", "she", "they", "we"], "correct": 2, "explanation": "'they' replaces multiple people."},
            {"type": "fill", "question": "Instead of 'My family and I', you can use the pronoun ___.", "options": ["they", "we", "us", "them"], "correct": 1, "explanation": "'we' includes the speaker."},
            {"type": "mcq", "question": "Which of these words is a pronoun?", "options": ["happy", "running", "them", "quickly"], "correct": 2, "explanation": "'them' is a pronoun."},
            {"type": "mcq", "question": "Find the pronoun: 'Give it to me.'", "options": ["Give", "it", "to", "None"], "correct": 1, "explanation": "'it' and 'me' are both pronouns. 'it' is an option."},
            {"type": "mcq", "question": "True or false: A pronoun must agree in number with the noun it replaces.", "options": ["True", "False", "Only for animals", "Only for things"], "correct": 0, "explanation": "If replacing 'boys' (plural), use 'they', not 'he'."},
            {"type": "fill", "question": "Words like I, you, he, she, it, we, and they are called ___.", "options": ["nouns", "verbs", "pronouns", "adjectives"], "correct": 2, "explanation": "They replace nouns."},
            {"type": "mcq", "question": "Which sentence correctly replaces 'The box' with a pronoun?", "options": ["He is heavy.", "She is heavy.", "It is heavy.", "They is heavy."], "correct": 2, "explanation": "'It' is used for a singular thing."}
        ]
    },
    {
        "id": "pronoun_sub_2",
        "title": "Personal Pronouns",
        "image": "assets/pronoun_personal.jpg",
        "content": "### Talking about specific people or things\n\n**Personal Pronouns** represent specific people or things. They change form depending on person, number, and gender.\n\n- **1st Person (Speaker):** I (singular), We (plural)\n- **2nd Person (Spoken to):** You (singular/plural)\n- **3rd Person (Spoken about):** He (male), She (female), It (thing/animal), They (plural)\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**தனிநபர் பிரதிபெயர்ச்சொற்கள் (Personal Pronouns):**\nஇவை குறிப்பிட்ட நபர்களையோ அல்லது பொருட்களையோ குறிக்கப் பயன்படுகின்றன.\n\n- **தன்மை (1st Person):** I (நான்), We (நாங்கள்/நாம்)\n- **முன்னிலை (2nd Person):** You (நீ/நீங்கள்)\n- **படர்க்கை (3rd Person):** He (அவன்), She (அவள்), It (அது), They (அவர்கள்/அவைகள்).",
        "questions": [
            {"type": "mcq", "question": "Which is a 1st person singular pronoun?", "options": ["I", "You", "He", "They"], "correct": 0, "explanation": "'I' refers to the speaker."},
            {"type": "mcq", "question": "Which is a 3rd person plural pronoun?", "options": ["We", "You", "They", "It"], "correct": 2, "explanation": "'They' refers to multiple people/things being spoken about."},
            {"type": "mcq", "question": "What pronoun replaces 'Samantha'?", "options": ["He", "She", "It", "They"], "correct": 1, "explanation": "Samantha is traditionally a female name."},
            {"type": "fill", "question": "My friends and I are going out. ___ are going to the cinema.", "options": ["They", "We", "You", "I"], "correct": 1, "explanation": "'We' includes the speaker and others."},
            {"type": "fill", "question": "Look at that car! ___ is so fast.", "options": ["He", "She", "It", "They"], "correct": 2, "explanation": "'It' is used for a singular object."},
            {"type": "mcq", "question": "Which pronoun is used for the person you are directly talking to?", "options": ["I", "You", "He", "She"], "correct": 1, "explanation": "'You' is the 2nd person pronoun."},
            {"type": "mcq", "question": "Identify the personal pronoun: 'They are playing outside.'", "options": ["They", "are", "playing", "outside"], "correct": 0, "explanation": "'They' is a 3rd person plural personal pronoun."},
            {"type": "mcq", "question": "What pronoun replaces 'The students'?", "options": ["He", "She", "It", "They"], "correct": 3, "explanation": "Students is plural, so we use 'They'."},
            {"type": "fill", "question": "___ am very tired today.", "options": ["I", "You", "He", "She"], "correct": 0, "explanation": "'am' is only used with 'I'."},
            {"type": "fill", "question": "Where is Mark? ___ is in the kitchen.", "options": ["He", "She", "It", "They"], "correct": 0, "explanation": "Mark is a male, so use 'He'."},
            {"type": "mcq", "question": "Which pronoun can be singular AND plural?", "options": ["I", "He", "You", "It"], "correct": 2, "explanation": "'You' can mean one person or a group of people."},
            {"type": "mcq", "question": "Find the personal pronoun: 'She is a great singer.'", "options": ["She", "is", "great", "singer"], "correct": 0, "explanation": "'She' is the personal pronoun."},
            {"type": "mcq", "question": "Which of these is NOT a personal pronoun?", "options": ["I", "We", "Book", "They"], "correct": 2, "explanation": "Book is a noun."},
            {"type": "fill", "question": "The dog is barking because ___ is hungry.", "options": ["he", "she", "it", "they"], "correct": 2, "explanation": "Use 'it' for animals when gender isn't specified."},
            {"type": "mcq", "question": "Which pronoun replaces 'The books'?", "options": ["He", "It", "They", "We"], "correct": 2, "explanation": "'They' is used for plural objects as well as plural people."}
        ]
    },
    {
        "id": "pronoun_sub_3",
        "title": "Subject vs. Object Pronouns",
        "image": "assets/pronoun_subject_object.jpg",
        "content": "### Doer vs. Receiver\n\nPersonal pronouns change their form depending on whether they are doing the action or receiving the action.\n\n- **Subject Pronouns** (Do the action): I, you, he, she, it, we, they.\n  - *Example:* **She** called John.\n- **Object Pronouns** (Receive the action): me, you, him, her, it, us, them.\n  - *Example:* John called **her**.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**Subject vs. Object Pronouns:**\n\n- **Subject Pronouns (எழுவாய்):** வாக்கியத்தில் செயலைச் செய்பவரைக் குறிக்கும்.\n  *(எ.கா: **I** like apples - நான் ஆப்பிள்களை விரும்புகிறேன்).* \n- **Object Pronouns (செயப்படுபொருள்):** செயலை ஏற்பவரைக் குறிக்கும்.\n  *(எ.கா: John gave **me** an apple - ஜான் **எனக்கு** ஒரு ஆப்பிள் கொடுத்தான்).* \n\n*Subject -> Object*\nI -> me\nWe -> us\nHe -> him\nShe -> her\nThey -> them",
        "questions": [
            {"type": "mcq", "question": "Which is a subject pronoun?", "options": ["Me", "Him", "They", "Us"], "correct": 2, "explanation": "'They' does the action (e.g., They run)."},
            {"type": "mcq", "question": "Which is an object pronoun?", "options": ["I", "She", "We", "Them"], "correct": 3, "explanation": "'Them' receives the action (e.g., Call them)."},
            {"type": "mcq", "question": "Choose the correct pronoun: '___ went to the store.'", "options": ["Me", "Him", "Us", "She"], "correct": 3, "explanation": "'She' is a subject pronoun doing the action."},
            {"type": "fill", "question": "Please give the book to ___.", "options": ["I", "me", "he", "she"], "correct": 1, "explanation": "'me' is the object receiving the book."},
            {"type": "fill", "question": "___ are happy today.", "options": ["Us", "Them", "We", "Me"], "correct": 2, "explanation": "'We' is the subject pronoun."},
            {"type": "mcq", "question": "Identify the object pronoun in: 'The teacher praised him.'", "options": ["The", "teacher", "praised", "him"], "correct": 3, "explanation": "'him' receives the praise."},
            {"type": "mcq", "question": "Identify the subject pronoun in: 'They saw us.'", "options": ["They", "saw", "us", "none"], "correct": 0, "explanation": "'They' is the one doing the seeing."},
            {"type": "mcq", "question": "Which pronoun acts as BOTH subject and object without changing form?", "options": ["I", "He", "You", "We"], "correct": 2, "explanation": "'You' stays the same (You saw him / He saw you)."},
            {"type": "fill", "question": "My mom loves ___ very much.", "options": ["I", "me", "he", "she"], "correct": 1, "explanation": "'me' is the object receiving the love."},
            {"type": "fill", "question": "John and ___ went to the mall.", "options": ["me", "I", "him", "her"], "correct": 1, "explanation": "John and 'I' are the subjects doing the action."},
            {"type": "mcq", "question": "Which is correct?", "options": ["Her is running.", "She is running.", "Him is running.", "Them is running."], "correct": 1, "explanation": "'She' is the proper subject pronoun."},
            {"type": "mcq", "question": "Choose the correct pronoun: 'Can you help ___?'", "options": ["we", "us", "they", "she"], "correct": 1, "explanation": "'us' is the object pronoun."},
            {"type": "mcq", "question": "What is the object form of 'He'?", "options": ["His", "Himself", "Him", "He's"], "correct": 2, "explanation": "'Him' is the object pronoun."},
            {"type": "fill", "question": "The dog followed ___ home.", "options": ["they", "them", "we", "he"], "correct": 1, "explanation": "'them' receives the action of being followed."},
            {"type": "mcq", "question": "Which sentence is correct?", "options": ["Me and him went out.", "I and he went out.", "He and I went out.", "Him and me went out."], "correct": 2, "explanation": "Both must be subject pronouns (He, I) and it's polite to put 'I' last."}
        ]
    }
]

with open('data/curriculum.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find if Pronoun topic exists
pronoun_topic = next((t for t in data['topics'] if t['name'] == 'Pronoun'), None)

if not pronoun_topic:
    pronoun_topic = {
        "name": "Pronoun",
        "subtopics": []
    }
    data['topics'].append(pronoun_topic)

# Append new subtopics (avoiding duplicates based on ID)
existing_ids = [s['id'] for s in pronoun_topic['subtopics']]
for sub in new_subtopics:
    if sub['id'] not in existing_ids:
        pronoun_topic['subtopics'].append(sub)

with open('data/curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("curriculum.json updated with Pronoun topics 1, 2, 3!")
