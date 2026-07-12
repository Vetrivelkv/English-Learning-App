import json
import os

new_subtopics = [
    {
        "id": "pronoun_sub_4",
        "title": "Possessive Pronouns",
        "image": "assets/pronoun_possessive.jpg",
        "content": "### Showing Ownership\n\n**Possessive Pronouns** show that something belongs to someone. They stand ALONE and do NOT need a noun after them.\n\n- **Mine** (belongs to me) -> *The book is mine.*\n- **Yours** (belongs to you) -> *Is this yours?*\n- **His** (belongs to him) -> *The car is his.*\n- **Hers** (belongs to her) -> *The house is hers.*\n- **Ours** (belongs to us) -> *The victory is ours.*\n- **Theirs** (belongs to them) -> *The money is theirs.*\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**உரிமையைக் குறிக்கும் பிரதிபெயர்ச்சொற்கள் (Possessive Pronouns):**\nஒரு பொருள் யாருக்குச் சொந்தமானது என்பதைக் குறிக்க இவை பயன்படுகின்றன. இவற்றுக்குப் பிறகு பெயர்ச்சொல் (noun) வராது. இவை தனித்து நிற்கும்.\n\n- **Mine** - என்னுடையது\n- **Yours** - உன்னுடையது / உங்களுடையது\n- **His** - அவனுடையது\n- **Hers** - அவளுடையது\n- **Ours** - எங்களுடையது / நம்முடையது\n- **Theirs** - அவர்களுடையது / அவைகளுடையது",
        "questions": [
            {"type": "mcq", "question": "Which word is a possessive pronoun?", "options": ["mine", "me", "my", "I"], "correct_option_index": 0, "explanation": "'mine' stands alone to show ownership."},
            {"type": "mcq", "question": "Complete the sentence: 'This jacket is ___.'", "options": ["hers", "her", "she", "me"], "correct_option_index": 0, "explanation": "'hers' is the possessive pronoun."},
            {"type": "mcq", "question": "Which of these stands ALONE without a noun?", "options": ["my", "your", "theirs", "our"], "correct_option_index": 2, "explanation": "Possessive pronouns like 'theirs' don't need a noun after them."},
            {"type": "fill", "question": "I bought this car. It is ___.", "answer": "mine", "explanation": "Belongs to me."},
            {"type": "fill", "question": "We bought this house. It is ___.", "answer": "ours", "explanation": "Belongs to us."},
            {"type": "fill", "question": "They bought those shoes. They are ___.", "answer": "theirs", "explanation": "Belongs to them."},
            {"type": "mcq", "question": "Choose the correct pronoun: 'Is this book ___?'", "options": ["you", "your", "yours", "yourself"], "correct_option_index": 2, "explanation": "yours stands alone."},
            {"type": "mcq", "question": "Identify the possessive pronoun: 'The fault is entirely his.'", "options": ["The", "fault", "entirely", "his"], "correct_option_index": 3, "explanation": "his shows ownership."},
            {"type": "mcq", "question": "Which is NOT a possessive pronoun?", "options": ["ours", "hers", "mine", "them"], "correct_option_index": 3, "explanation": "Them is an object pronoun."},
            {"type": "fill", "question": "She owns that laptop. The laptop is ___.", "answer": "hers", "explanation": "Belongs to her."},
            {"type": "mcq", "question": "Complete: 'That problem is not mine, it's ___.'", "options": ["your", "yours", "you", "yourself"], "correct_option_index": 1, "explanation": "yours stands alone."},
            {"type": "mcq", "question": "Is 'its' a possessive pronoun?", "options": ["Yes", "No", "Only for animals", "Only in plural"], "correct_option_index": 0, "explanation": "Yes, e.g., 'The cat licked its paw' (though usually used as an adjective, 'its' can act as a pronoun)."},
            {"type": "fill", "question": "He forgot his lunch, so I gave him ___.", "answer": "mine", "explanation": "Meaning 'my lunch'."},
            {"type": "fill", "question": "Those seats belong to them. They are ___.", "answer": "theirs", "explanation": "Meaning 'their seats'."},
            {"type": "mcq", "question": "Which sentence is correct?", "options": ["The dog is mine.", "The dog is my.", "The dog is me.", "The dog is I."], "correct_option_index": 0, "explanation": "Mine is the correct possessive pronoun."}
        ]
    },
    {
        "id": "pronoun_sub_5",
        "title": "Possessive Adjectives vs. Pronouns",
        "image": "assets/pronoun_possessive_adj.jpg",
        "content": "### What's the difference?\n\nMany people confuse **Possessive Adjectives** (my, your, our) with **Possessive Pronouns** (mine, yours, ours).\n\n1. **Possessive Adjectives** MUST be followed by a noun. They act like adjectives describing the noun.\n   - *Example:* This is **my** car. (Followed by 'car')\n   - *Words:* my, your, his, her, its, our, their.\n\n2. **Possessive Pronouns** STAND ALONE. They replace the noun entirely.\n   - *Example:* This car is **mine**. (No noun after 'mine')\n   - *Words:* mine, yours, his, hers, ours, theirs.\n\n*Note:* 'His' and 'its' look exactly the same in both forms!\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**Possessive Adjectives vs. Pronouns:**\n\n1. **Possessive Adjectives:** இவற்றுக்குப் பின் கட்டாயம் ஒரு பெயர்ச்சொல் (Noun) வர வேண்டும்.\n   - *எ.கா:* இது **என்னுடைய** கார் (This is **my** car).\n   - *வார்த்தைகள்:* my, your, his, her, its, our, their.\n\n2. **Possessive Pronouns:** இவை தனித்து நிற்கும். பெயர்ச்சொல் தேவையில்லை.\n   - *எ.கா:* இந்தக் கார் **என்னுடையது** (This car is **mine**).\n   - *வார்த்தைகள்:* mine, yours, his, hers, ours, theirs.",
        "questions": [
            {"type": "mcq", "question": "In 'That is my pen', what is 'my'?", "options": ["Possessive Pronoun", "Possessive Adjective", "Subject Pronoun", "Object Pronoun"], "correct_option_index": 1, "explanation": "It is followed by the noun 'pen'."},
            {"type": "mcq", "question": "In 'That pen is mine', what is 'mine'?", "options": ["Possessive Pronoun", "Possessive Adjective", "Subject Pronoun", "Object Pronoun"], "correct_option_index": 0, "explanation": "It stands alone without a noun after it."},
            {"type": "mcq", "question": "Which word is a possessive adjective?", "options": ["hers", "ours", "your", "mine"], "correct_option_index": 2, "explanation": "You must say 'your [noun]'."},
            {"type": "fill", "question": "Is this ___ jacket? (your / yours)", "answer": "your", "explanation": "Followed by the noun 'jacket'."},
            {"type": "fill", "question": "Is this jacket ___? (your / yours)", "answer": "yours", "explanation": "Stands alone at the end."},
            {"type": "mcq", "question": "Identify the possessive adjective in: 'Our team won the game.'", "options": ["Our", "team", "won", "game"], "correct_option_index": 0, "explanation": "'Our' describes the team."},
            {"type": "mcq", "question": "Which sentence uses a possessive pronoun?", "options": ["Their house is big.", "The big house is theirs.", "My dog is cute.", "Her dress is blue."], "correct_option_index": 1, "explanation": "'theirs' is a pronoun."},
            {"type": "mcq", "question": "Which word functions as BOTH a possessive adjective and pronoun?", "options": ["my", "his", "her", "our"], "correct_option_index": 1, "explanation": "His car (adjective) vs The car is his (pronoun)."},
            {"type": "fill", "question": "I forgot ___ keys at home. (my / mine)", "answer": "my", "explanation": "Followed by keys."},
            {"type": "fill", "question": "Those keys on the table are ___. (my / mine)", "answer": "mine", "explanation": "Stands alone."},
            {"type": "mcq", "question": "Choose the correct sentence.", "options": ["This is mine book.", "This is my book.", "This book is my.", "This book is me."], "correct_option_index": 1, "explanation": "'my' must be followed by a noun."},
            {"type": "mcq", "question": "Choose the correct sentence.", "options": ["The victory is our.", "The victory is ours.", "The victory is we.", "The victory is us."], "correct_option_index": 1, "explanation": "'ours' stands alone."},
            {"type": "fill", "question": "Can I borrow ___ pen? (your / yours)", "answer": "your", "explanation": "Followed by pen."},
            {"type": "fill", "question": "She washed ___ car today. (her / hers)", "answer": "her", "explanation": "Followed by car."},
            {"type": "mcq", "question": "In 'The dog wagged its tail', 'its' is a:", "options": ["Possessive Adjective", "Possessive Pronoun", "Subject", "Verb"], "correct_option_index": 0, "explanation": "Followed by the noun 'tail'."}
        ]
    },
    {
        "id": "pronoun_sub_6",
        "title": "Reflexive Pronouns",
        "image": "assets/pronoun_reflexive.jpg",
        "content": "### Reflecting back to the Subject\n\n**Reflexive Pronouns** end in *-self* (singular) or *-selves* (plural). They are used when the **subject** and the **object** of the verb are exactly the SAME person.\n\n- *Example:* **I** cut **myself** while cooking.\n  (I did the cutting, and I received the cut).\n\nThey are also used for emphasis (Intensive Pronouns): *I will do it myself!*\n\n- **Singular:** myself, yourself, himself, herself, itself.\n- **Plural:** ourselves, yourselves, themselves.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**தன்னிலை பிரதிபெயர்ச்சொற்கள் (Reflexive Pronouns):**\nவாக்கியத்தில் செயலைச் செய்பவரும் (Subject), அச்செயலை ஏற்பவரும் (Object) ஒரே நபராக இருக்கும்போது இது பயன்படுத்தப்படுகிறது. இவை '-self' அல்லது '-selves' என்று முடியும்.\n\n- *எ.கா:* **I** cut **myself** (நான் என்னையே வெட்டிக்கொண்டேன்).\n- **ஒருமை:** myself (என்னை/நானே), yourself (உன்னை/நீயே), himself, herself, itself.\n- **பன்மை:** ourselves (எங்களை/நாங்களே), yourselves, themselves.",
        "questions": [
            {"type": "mcq", "question": "Which of these is a reflexive pronoun?", "options": ["me", "myself", "mine", "I"], "correct_option_index": 1, "explanation": "Ends in -self."},
            {"type": "mcq", "question": "When do you use a reflexive pronoun?", "options": ["To show ownership", "When the subject and object are the same", "To point at things", "To ask questions"], "correct_option_index": 1, "explanation": "Subject = Object (I saw myself)."},
            {"type": "mcq", "question": "Complete: 'She looked at ___ in the mirror.'", "options": ["her", "hers", "herself", "she"], "correct_option_index": 2, "explanation": "She and herself are the same person."},
            {"type": "fill", "question": "He taught ___ how to play the guitar.", "answer": "himself", "explanation": "He = himself."},
            {"type": "fill", "question": "We built this house all by ___.", "answer": "ourselves", "explanation": "We = ourselves (plural)."},
            {"type": "mcq", "question": "What is the plural reflexive pronoun for 'you'?", "options": ["yourself", "yourselves", "your", "yours"], "correct_option_index": 1, "explanation": "Ends in -selves for plural."},
            {"type": "mcq", "question": "Complete: 'The cat cleaned ___.'", "options": ["himself", "herself", "itself", "myself"], "correct_option_index": 2, "explanation": "'itself' is used for animals when gender isn't known."},
            {"type": "mcq", "question": "Identify the intensive pronoun: 'I myself saw the alien.'", "options": ["I", "myself", "saw", "alien"], "correct_option_index": 1, "explanation": "myself is used for emphasis here."},
            {"type": "fill", "question": "They bought ___ some ice cream.", "answer": "themselves", "explanation": "They = themselves."},
            {"type": "fill", "question": "Did you make this cake all by ___? (talking to one person)", "answer": "yourself", "explanation": "Singular 'you' = yourself."},
            {"type": "mcq", "question": "Which is incorrect?", "options": ["hisself", "himself", "themselves", "ourselves"], "correct_option_index": 0, "explanation": "'hisself' is not a word. It's 'himself'."},
            {"type": "mcq", "question": "Which is incorrect?", "options": ["themselfs", "themselves", "myself", "herself"], "correct_option_index": 0, "explanation": "'themselfs' and 'theirselves' are incorrect. It's 'themselves'."},
            {"type": "fill", "question": "The oven turns ___ off when it's done.", "answer": "itself", "explanation": "Oven = itself."},
            {"type": "fill", "question": "I don't need help, I can do it ___.", "answer": "myself", "explanation": "I = myself."},
            {"type": "mcq", "question": "Choose the correct sentence.", "options": ["John and myself went to the store.", "John and I went to the store.", "Myself and John went.", "John and me went."], "correct_option_index": 1, "explanation": "Reflexive pronouns cannot be the main subject of a sentence."}
        ]
    },
    {
        "id": "pronoun_sub_7",
        "title": "Demonstrative Pronouns",
        "image": "assets/pronoun_demonstrative.jpg",
        "content": "### Pointing at things\n\n**Demonstrative Pronouns** are used to point to specific things. They indicate distance (near or far) and number (singular or plural).\n\n- **This** (Singular, near) -> *This is my favorite book.*\n- **That** (Singular, far) -> *That is a tall building.*\n- **These** (Plural, near) -> *These are delicious cookies.*\n- **Those** (Plural, far) -> *Those are expensive shoes.*\n\n*Note:* If they are followed by a noun (e.g., *This book* is good), they are Demonstrative Adjectives. If they stand alone (e.g., *This* is good), they are Demonstrative Pronouns.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**சுட்டுப் பிரதிபெயர்ச்சொற்கள் (Demonstrative Pronouns):**\nகுறிப்பிட்ட பொருட்களைச் சுட்டிக்காட்ட இவை பயன்படுகின்றன. தூரம் மற்றும் எண்ணிக்கையை அடிப்படையாகக் கொண்டு 4 வார்த்தைகள் உள்ளன:\n\n- **This (இது):** அருகில் உள்ள ஒரு பொருள்.\n- **That (அது):** தூரத்தில் உள்ள ஒரு பொருள்.\n- **These (இவைகள்):** அருகில் உள்ள பல பொருட்கள்.\n- **Those (அவைகள்):** தூரத்தில் உள்ள பல பொருட்கள்.",
        "questions": [
            {"type": "mcq", "question": "Which word is a demonstrative pronoun?", "options": ["He", "Who", "This", "Myself"], "correct_option_index": 2, "explanation": "'This' points to something near."},
            {"type": "mcq", "question": "Which pronoun points to a SINGULAR object FAR away?", "options": ["This", "That", "These", "Those"], "correct_option_index": 1, "explanation": "'That' is singular and far."},
            {"type": "mcq", "question": "Which pronoun points to PLURAL objects NEAR you?", "options": ["This", "That", "These", "Those"], "correct_option_index": 2, "explanation": "'These' is plural and near."},
            {"type": "fill", "question": "Look at the stars! ___ are so bright tonight.", "answer": "Those", "explanation": "Stars are plural and far away."},
            {"type": "fill", "question": "Here, hold ___ for me. (handing a singular object)", "answer": "this", "explanation": "Singular and near."},
            {"type": "mcq", "question": "In the sentence 'That is a fast car', 'That' is a:", "options": ["Demonstrative Adjective", "Demonstrative Pronoun", "Personal Pronoun", "Noun"], "correct_option_index": 1, "explanation": "It stands alone without a noun directly after it."},
            {"type": "mcq", "question": "In 'That car is fast', 'That' is a:", "options": ["Demonstrative Adjective", "Demonstrative Pronoun", "Personal Pronoun", "Noun"], "correct_option_index": 0, "explanation": "It is followed directly by the noun 'car'."},
            {"type": "fill", "question": "___ are my shoes right here.", "answer": "These", "explanation": "Plural and near ('right here')."},
            {"type": "fill", "question": "Was ___ your brother who just walked away?", "answer": "that", "explanation": "Singular and far ('walked away')."},
            {"type": "mcq", "question": "Which of these is NOT a demonstrative pronoun?", "options": ["This", "That", "There", "Those"], "correct_option_index": 2, "explanation": "'There' is an adverb of place."},
            {"type": "mcq", "question": "Complete: '___ is the best day of my life!'", "options": ["This", "These", "Those", "Them"], "correct_option_index": 0, "explanation": "The day is currently happening (near in time) and singular."},
            {"type": "fill", "question": "Are ___ your bags over there?", "answer": "those", "explanation": "Bags are plural and far ('over there')."},
            {"type": "mcq", "question": "Which pairs are singular?", "options": ["This, That", "These, Those", "This, These", "That, Those"], "correct_option_index": 0, "explanation": "This and That are both singular."},
            {"type": "mcq", "question": "Which pairs are plural?", "options": ["This, That", "These, Those", "This, These", "That, Those"], "correct_option_index": 1, "explanation": "These and Those are both plural."},
            {"type": "fill", "question": "___ smells amazing! (holding a plate of food)", "answer": "This", "explanation": "Singular and physically near."}
        ]
    },
    {
        "id": "pronoun_sub_8",
        "title": "Interrogative Pronouns",
        "image": "assets/pronoun_interrogative.jpg",
        "content": "### Asking Questions\n\n**Interrogative Pronouns** are used to ask questions. They stand in for the answer (a noun) that you don't know yet.\n\n- **Who:** Asking about a person (Subject). *Who is at the door?*\n- **Whom:** Asking about a person (Object). *Whom did you call?*\n- **Whose:** Asking about ownership. *Whose are these keys?*\n- **What:** Asking about things/animals. *What is in the box?*\n- **Which:** Asking to make a choice between specific options. *Which do you prefer?*\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**கேள்விப் பிரதிபெயர்ச்சொற்கள் (Interrogative Pronouns):**\nகேள்விகளைக் கேட்க இவை பயன்படுகின்றன. பதில் வரப்போகும் பெயர்ச்சொல்லுக்குப் பதிலாக இவை அமைகின்றன.\n\n- **Who (யார்):** நபர்களைப் பற்றிக் கேட்க (எழுவாய்).\n- **Whom (யாரை/யாருக்கு):** நபர்களைப் பற்றிக் கேட்க (செயப்படுபொருள்).\n- **Whose (யாருடையது):** உரிமையைக் கேட்க.\n- **What (என்ன):** பொருட்கள்/விலங்குகளைப் பற்றிக் கேட்க.\n- **Which (எது/எந்த):** குறிப்பிட்ட விருப்பங்களில் ஒன்றைத் தேர்ந்தெடுக்க.",
        "questions": [
            {"type": "mcq", "question": "Which pronoun is used to ask about a person doing an action?", "options": ["What", "Which", "Who", "Whose"], "correct_option_index": 2, "explanation": "'Who' is the subject interrogative pronoun."},
            {"type": "mcq", "question": "Which pronoun asks about ownership?", "options": ["Who", "Whom", "Whose", "What"], "correct_option_index": 2, "explanation": "'Whose' asks who something belongs to."},
            {"type": "mcq", "question": "Which pronoun is used when there are limited choices?", "options": ["What", "Which", "Who", "Whom"], "correct_option_index": 1, "explanation": "'Which' implies a choice from a specific set (e.g., Which color, red or blue?)."},
            {"type": "fill", "question": "___ is knocking at the door?", "answer": "Who", "explanation": "Asking for the subject person."},
            {"type": "fill", "question": "___ did you invite to the party?", "answer": "Whom", "explanation": "Asking for the object person (You invited *them*)."},
            {"type": "mcq", "question": "Complete: '___ is your favorite food?'", "options": ["Who", "What", "Whose", "Whom"], "correct_option_index": 1, "explanation": "'What' asks about a thing."},
            {"type": "mcq", "question": "Complete: '___ of these two shirts looks better?'", "options": ["Who", "What", "Which", "Whose"], "correct_option_index": 2, "explanation": "Making a choice between two specific shirts."},
            {"type": "fill", "question": "___ shoes are these on the floor?", "answer": "Whose", "explanation": "Asking about ownership."},
            {"type": "fill", "question": "___ happened here last night?", "answer": "What", "explanation": "Asking about an event/thing."},
            {"type": "mcq", "question": "Which is correct in formal English?", "options": ["Who did you give the book to?", "To whom did you give the book?", "Whose did you give the book to?", "What did you give the book to?"], "correct_option_index": 1, "explanation": "'Whom' is the object of the preposition 'to'."},
            {"type": "mcq", "question": "Identify the interrogative pronoun: 'What do you want?'", "options": ["What", "do", "you", "want"], "correct_option_index": 0, "explanation": "'What' starts the question."},
            {"type": "mcq", "question": "Are 'why' and 'how' interrogative pronouns?", "options": ["Yes", "No", "Only why", "Only how"], "correct_option_index": 1, "explanation": "No, they are interrogative adverbs (they don't replace nouns)."},
            {"type": "fill", "question": "___ won the game?", "answer": "Who", "explanation": "Subject person."},
            {"type": "fill", "question": "___ is the capital of France?", "answer": "What", "explanation": "Asking about a thing/place."},
            {"type": "mcq", "question": "Which is an interrogative pronoun?", "options": ["That", "Those", "Which", "Himself"], "correct_option_index": 2, "explanation": "'Which' is used for questions."}
        ]
    },
    {
        "id": "pronoun_sub_9",
        "title": "Indefinite Pronouns",
        "image": "assets/pronoun_indefinite.jpg",
        "content": "### Unspecified People, Things, or Places\n\n**Indefinite Pronouns** do not point to any specific person, thing, or amount. They are vague.\n\n- **People:** someone, anyone, everyone, nobody, everybody.\n- **Things:** something, anything, everything, nothing.\n- **Places:** somewhere, anywhere, everywhere, nowhere.\n- **Amounts:** all, some, any, several, none, few, many.\n\n*Important Rule:* Most indefinite pronouns ending in -one, -body, or -thing are **SINGULAR** (e.g., *Everybody is* happy, NOT *Everybody are* happy).\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**நிச்சயமற்ற பிரதிபெயர்ச்சொற்கள் (Indefinite Pronouns):**\nஇவை ஒரு குறிப்பிட்ட நபரையோ, பொருளையோ துல்லியமாகக் குறிக்காமல் பொதுவாகக் குறிக்கின்றன.\n\n- **நபர்கள்:** someone (யாரோ ஒருவர்), anyone (யாராவது), everyone (எல்லோரும்), nobody (யாரும் இல்லை).\n- **பொருட்கள்:** something, anything, everything, nothing.\n*முக்கிய விதி:* -one, -body, -thing என முடியும் வார்த்தைகள் எப்போதும் **ஒருமையாகவே (Singular)** கருதப்படும். (எ.கா: Everyone **is** here).",
        "questions": [
            {"type": "mcq", "question": "Which is an indefinite pronoun?", "options": ["He", "They", "Someone", "Which"], "correct_option_index": 2, "explanation": "'Someone' doesn't specify exactly who."},
            {"type": "mcq", "question": "Are pronouns ending in -body (like everybody) singular or plural?", "options": ["Singular", "Plural", "Both", "Depends on the sentence"], "correct_option_index": 0, "explanation": "They take singular verbs (Everybody IS)."},
            {"type": "mcq", "question": "Choose the correct verb: 'Everyone ___ going to the party.'", "options": ["is", "are", "am", "be"], "correct_option_index": 0, "explanation": "Everyone is singular."},
            {"type": "fill", "question": "I have looked ___ for my keys, but I can't find them.", "answer": "everywhere", "explanation": "Meaning in all places."},
            {"type": "fill", "question": "Does ___ have a pen I can borrow?", "answer": "anyone", "explanation": "Asking if any person has one."},
            {"type": "mcq", "question": "Which word refers to NO people?", "options": ["Nothing", "Nobody", "Nowhere", "None"], "correct_option_index": 1, "explanation": "Nobody = no person."},
            {"type": "mcq", "question": "Choose the correct sentence.", "options": ["Somebody left their bag.", "Somebody left his or her bag.", "Both A and B are acceptable in modern English.", "Neither is correct."], "correct_option_index": 2, "explanation": "Modern English often uses singular 'their' for gender-neutral indefinite pronouns."},
            {"type": "fill", "question": "I have ___ to wear! My closet is empty.", "answer": "nothing", "explanation": "Meaning zero things."},
            {"type": "fill", "question": "___ is perfect; we all make mistakes.", "answer": "Nobody", "explanation": "No person."},
            {"type": "mcq", "question": "Which indefinite pronoun is PLURAL?", "options": ["Everyone", "Someone", "Several", "Anybody"], "correct_option_index": 2, "explanation": "'Several' means more than one (e.g., Several ARE here)."},
            {"type": "mcq", "question": "Identify the indefinite pronoun: 'Many are called, but few are chosen.'", "options": ["Many", "but", "are", "chosen"], "correct_option_index": 0, "explanation": "'Many' (and 'few') are indefinite pronouns here."},
            {"type": "fill", "question": "Is there ___ good to eat in the fridge?", "answer": "anything", "explanation": "Any thing."},
            {"type": "fill", "question": "I know a secret, but I won't tell ___.", "answer": "anyone", "explanation": "Any person."},
            {"type": "mcq", "question": "Choose the correct verb: 'Nothing ___ impossible.'", "options": ["is", "are", "were", "am"], "correct_option_index": 0, "explanation": "Nothing is singular."},
            {"type": "mcq", "question": "Which word is NOT an indefinite pronoun?", "options": ["All", "Some", "Those", "None"], "correct_option_index": 2, "explanation": "'Those' is a demonstrative pronoun."}
        ]
    },
    {
        "id": "pronoun_sub_10",
        "title": "Relative Pronouns",
        "image": "assets/pronoun_relative.jpg",
        "content": "### Connecting Clauses\n\n**Relative Pronouns** are used to connect a dependent clause to an independent clause. They relate back to a noun mentioned previously in the sentence.\n\n- **Who / Whom:** Used for people. *The man **who** lives next door is friendly.*\n- **Which:** Used for animals or things. *The car **which** I bought is blue.*\n- **That:** Used for people, animals, or things. *The book **that** I read was great.*\n- **Whose:** Shows possession. *The boy **whose** dog ran away is sad.*\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**தொடர்புப் பிரதிபெயர்ச்சொற்கள் (Relative Pronouns):**\nஇரண்டு வாக்கியங்களை அல்லது சொற்றொடர்களை இணைக்க இவை பயன்படுகின்றன. இவை முன்பு கூறப்பட்ட ஒரு பெயர்ச்சொல்லைக் குறிக்கும்.\n\n- **Who / Whom (யார்/யாரை):** நபர்களைக் குறிக்க. (*எ.கா:* என் அருகில் வசிக்கும் மனிதர்... The man **who** lives...)\n- **Which (எது/எந்த):** பொருட்கள்/விலங்குகளைக் குறிக்க.\n- **That (அது/எது):** நபர்கள், பொருட்கள் இரண்டிற்கும் பயன்படுத்தலாம்.\n- **Whose (யாருடைய):** உரிமையைக் குறிக்க.",
        "questions": [
            {"type": "mcq", "question": "Which relative pronoun is used ONLY for people?", "options": ["Which", "That", "Who", "What"], "correct_option_index": 2, "explanation": "'Who' is strictly for people."},
            {"type": "mcq", "question": "Which relative pronoun is used ONLY for animals or things?", "options": ["Who", "Whom", "Which", "Whose"], "correct_option_index": 2, "explanation": "'Which' cannot be used for people."},
            {"type": "mcq", "question": "Which relative pronoun can be used for BOTH people and things?", "options": ["Who", "Which", "That", "Whom"], "correct_option_index": 2, "explanation": "'That' is versatile (e.g., the man that I saw, the car that I bought)."},
            {"type": "fill", "question": "The girl ___ won the race is my sister.", "answer": "who", "explanation": "Refers to the girl (person/subject)."},
            {"type": "fill", "question": "The dog ___ bit me is in the yard.", "answer": "which", "explanation": "Refers to an animal (or 'that')."},
            {"type": "mcq", "question": "Complete: 'The woman ___ purse was stolen went to the police.'", "options": ["who", "which", "whose", "whom"], "correct_option_index": 2, "explanation": "'Whose' shows possession of the purse."},
            {"type": "mcq", "question": "Identify the relative pronoun: 'This is the house that Jack built.'", "options": ["This", "is", "that", "Jack"], "correct_option_index": 2, "explanation": "'that' connects the clauses and refers to the house."},
            {"type": "fill", "question": "The book ___ I am reading is very interesting.", "answer": "that", "explanation": "Or 'which'. Refers to a thing."},
            {"type": "fill", "question": "I know the boy ___ bicycle is broken.", "answer": "whose", "explanation": "Shows ownership of the bicycle."},
            {"type": "mcq", "question": "Choose the correct pronoun: 'The person to ___ you should speak is the manager.'", "options": ["who", "which", "that", "whom"], "correct_option_index": 3, "explanation": "'Whom' is the object of the preposition 'to'."},
            {"type": "mcq", "question": "Are interrogative pronouns and relative pronouns the same words?", "options": ["Yes, often", "No, never", "Only who", "Only which"], "correct_option_index": 0, "explanation": "Words like who, which, and whose serve as both depending on if they ask a question or connect a clause."},
            {"type": "fill", "question": "Do you know the man ___ is standing over there?", "answer": "who", "explanation": "Refers to the man."},
            {"type": "fill", "question": "I lost the watch ___ my father gave me.", "answer": "which", "explanation": "Or 'that'. Refers to a thing."},
            {"type": "mcq", "question": "Complete: 'He is the only one ___ can help us.'", "options": ["which", "what", "who", "whom"], "correct_option_index": 2, "explanation": "Refers to a person (one) doing the action (help)."},
            {"type": "mcq", "question": "Which sentence is INCORRECT?", "options": ["The man who called is here.", "The car which is red is mine.", "The boy which is crying is sad.", "The dog that barked is loud."], "correct_option_index": 2, "explanation": "You cannot use 'which' for a person (boy)."}
        ]
    }
]

with open('data/curriculum.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Pronoun topic
topic = next((t for t in data['topics'] if t['name'] == 'Pronoun'), None)
if topic:
    existing_ids = [s['id'] for s in topic['subtopics']]
    for sub in new_subtopics:
        if sub['id'] not in existing_ids:
            topic['subtopics'].append(sub)

with open('data/curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added Pronoun learning subtopics 4 to 10 successfully!")
