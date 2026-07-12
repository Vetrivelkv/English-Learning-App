import json
import os

new_subtopics = [
    {
        "id": "verb_sub_1",
        "title": "Introduction to Verbs",
        "image": "",
        "content": "### The Engine of a Sentence\n\nA **Verb** is the most important part of a sentence. It tells us what the subject is doing (Action) or what state the subject is in (State of Being).\n\n1. **Action Verbs:** Show physical or mental action.\n   - *Examples:* run, jump, think, eat, read.\n   - *Sentence:* He **runs** every morning.\n2. **State of Being Verbs:** Show existence or a state. They don't show action.\n   - *Examples:* am, is, are, was, were, be, being, been.\n   - *Sentence:* She **is** happy.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**வினைச்சொல் (Verb) என்றால் என்ன?**\nஒரு வாக்கியத்தின் மிக முக்கியமான பகுதி வினைச்சொல். இது ஒரு செயலை அல்லது ஒருவரின் நிலையை (State of being) குறிக்கும்.\n\n1. **செயல் (Action Verbs):** உடல் அல்லது மனதால் செய்யும் செயல்கள். (எ.கா: ஓடு - run, சாப்பிடு - eat, சிந்தி - think).\n2. **நிலை (State of Being):** ஒரு செயலைக் குறிக்காமல், ஒருவர் அல்லது ஒரு பொருள் எப்படி இருக்கிறது/இருந்தது என்பதைக் குறிப்பது. (எ.கா: am, is, are, was, were).",
        "questions": [
            {"type": "mcq", "question": "What does a verb primarily show?", "options": ["A person or thing", "An action or state of being", "A description of a noun", "How an action is done"], "correct_option_index": 1, "explanation": "Verbs show action or being."},
            {"type": "mcq", "question": "Which of these is an ACTION verb?", "options": ["is", "am", "jump", "are"], "correct_option_index": 2, "explanation": "Jump is a physical action."},
            {"type": "mcq", "question": "Which of these is a STATE OF BEING verb?", "options": ["was", "think", "run", "sleep"], "correct_option_index": 0, "explanation": "Was shows existence in the past."},
            {"type": "mcq", "question": "Identify the verb: 'The cat sleeps on the sofa.'", "options": ["The", "cat", "sleeps", "sofa"], "correct_option_index": 2, "explanation": "Sleeps is the action."},
            {"type": "mcq", "question": "Identify the verb: 'I am very tired.'", "options": ["I", "am", "very", "tired"], "correct_option_index": 1, "explanation": "'am' is the state of being verb."},
            {"type": "fill", "question": "The boy ___ the ball. (kicked / boy)", "options": ["kicked", "boy", "the", "ball"], "correct_option_index": 0, "explanation": "Kicked is the action."},
            {"type": "fill", "question": "She ___ a doctor. (is / jump)", "options": ["is", "jump", "doctor", "she"], "correct_option_index": 0, "explanation": "'is' describes her state."},
            {"type": "mcq", "question": "Which sentence has an action verb?", "options": ["He is sad.", "They are here.", "She reads a book.", "I am tall."], "correct_option_index": 2, "explanation": "Reads is an action."},
            {"type": "mcq", "question": "Which sentence has a state of being verb?", "options": ["We ate pizza.", "They were angry.", "He drove the car.", "I wrote a letter."], "correct_option_index": 1, "explanation": "Were is a state of being verb."},
            {"type": "fill", "question": "They ___ to the store yesterday. (walked / were)", "options": ["walked", "were", "they", "store"], "correct_option_index": 0, "explanation": "Walked is the past action."},
            {"type": "mcq", "question": "Is 'think' an action verb?", "options": ["Yes, mental action", "No, it's a state of being", "No, it's a noun", "Yes, physical action"], "correct_option_index": 0, "explanation": "Thinking is a mental action."},
            {"type": "fill", "question": "The flowers ___ beautiful. (are / grow)", "options": ["are", "grow", "flowers", "beautiful"], "correct_option_index": 0, "explanation": "Are is the state of being."},
            {"type": "mcq", "question": "Every complete sentence must have a ___.", "options": ["Noun", "Verb", "Adjective", "Pronoun"], "correct_option_index": 1, "explanation": "A verb is the engine of the sentence."},
            {"type": "mcq", "question": "Which list contains ONLY state of being verbs?", "options": ["am, is, are", "run, jump, is", "think, am, play", "was, were, eat"], "correct_option_index": 0, "explanation": "Am, is, and are all show existence."},
            {"type": "fill", "question": "I ___ a student. (am / study)", "options": ["am", "study", "I", "student"], "correct_option_index": 0, "explanation": "'am' connects I to student."}
        ]
    },
    {
        "id": "verb_sub_2",
        "title": "Action vs Linking Verbs",
        "image": "",
        "content": "### Doing vs Linking\n\n1. **Action Verbs:** Tell what the subject is *doing*.\n   - *Example:* John **tasted** the soup.\n2. **Linking Verbs:** Do NOT show action. Instead, they *link* the subject to a noun or adjective that describes it. (Think of them as an equal sign '=').\n   - *Example:* The soup **tasted** good. (Soup = good).\n   - *Common Linking Verbs:* am, is, are, was, were, seem, become, feel, taste, smell, look.\n\n*Trick:* If you can replace the verb with 'am', 'is', or 'are' and it still makes sense, it's a linking verb!\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**Action vs Linking Verbs:**\n\n1. **Action Verbs (செயல்):** ஒருவர் என்ன செய்கிறார் என்பதைக் குறிக்கும். (எ.கா: அவன் சூப்பை ருசித்தான் - He tasted the soup).\n2. **Linking Verbs (இணைப்பு):** இது செயலைக் குறிக்காது. எழுவாயை (Subject) அதனைப் பற்றி விவரிக்கும் சொல்லுடன் இணைக்கும். (ஒரு '=' குறி போலச் செயல்படும்).\n   - *எ.கா:* சூப் சுவையாக இருந்தது (The soup tasted good). இங்கே சூப் எதையும் ருசிக்கவில்லை, அதன் சுவை எப்படி இருந்தது என்பதை இணைக்கிறது.",
        "questions": [
            {"type": "mcq", "question": "What does a linking verb do?", "options": ["Shows strong action", "Links the subject to a describing word", "Acts as a noun", "Connects two sentences"], "correct_option_index": 1, "explanation": "It connects the subject to more info about it."},
            {"type": "mcq", "question": "In 'The flower smells sweet', 'smells' is:", "options": ["Action Verb", "Linking Verb", "Noun", "Adjective"], "correct_option_index": 1, "explanation": "Flower = sweet. The flower isn't using a nose to smell."},
            {"type": "mcq", "question": "In 'She smells the flower', 'smells' is:", "options": ["Action Verb", "Linking Verb", "Noun", "Adjective"], "correct_option_index": 0, "explanation": "She is physically doing the action of smelling."},
            {"type": "fill", "question": "He ___ tired. (seems / runs)", "options": ["seems", "runs", "he", "tired"], "correct_option_index": 0, "explanation": "Seems connects He to tired."},
            {"type": "fill", "question": "The boy ___ the ball. (threw / is)", "options": ["threw", "is", "boy", "ball"], "correct_option_index": 0, "explanation": "Threw is an action."},
            {"type": "mcq", "question": "Which verb is almost ALWAYS a linking verb?", "options": ["taste", "look", "is", "feel"], "correct_option_index": 2, "explanation": "'is' always acts as a state of being/linking verb."},
            {"type": "mcq", "question": "Identify the linking verb: 'They became friends.'", "options": ["They", "became", "friends", "None"], "correct_option_index": 1, "explanation": "They = friends."},
            {"type": "mcq", "question": "Identify the action verb: 'The dog looked at me.'", "options": ["The", "dog", "looked", "me"], "correct_option_index": 2, "explanation": "The dog is physically using its eyes."},
            {"type": "fill", "question": "The music sounds ___. (loud / loudly)", "options": ["loud", "loudly", "music", "sounds"], "correct_option_index": 0, "explanation": "Sounds is a linking verb, so it takes an adjective (loud)."},
            {"type": "fill", "question": "I ___ happy today. (feel / jump)", "options": ["feel", "jump", "I", "happy"], "correct_option_index": 0, "explanation": "Feel links I to happy."},
            {"type": "mcq", "question": "Is 'appear' an action or linking verb in: 'He appeared suddenly.'", "options": ["Action", "Linking", "Both", "Neither"], "correct_option_index": 0, "explanation": "He physically showed up (action)."},
            {"type": "mcq", "question": "Is 'appear' an action or linking verb in: 'He appeared angry.'", "options": ["Action", "Linking", "Both", "Neither"], "correct_option_index": 1, "explanation": "He = angry (linking)."},
            {"type": "fill", "question": "The weather ___ hot. (was / ran)", "options": ["was", "ran", "weather", "hot"], "correct_option_index": 0, "explanation": "Was links weather to hot."},
            {"type": "mcq", "question": "Which sentence has a linking verb?", "options": ["I run fast.", "I eat apples.", "I am a student.", "I write well."], "correct_option_index": 2, "explanation": "Am links I to student."},
            {"type": "mcq", "question": "Which sentence has an action verb?", "options": ["She is nice.", "They seem sad.", "We feel cold.", "He kicked it."], "correct_option_index": 3, "explanation": "Kicked is a physical action."}
        ]
    },
    {
        "id": "verb_sub_3",
        "title": "Helping (Auxiliary) Verbs",
        "image": "",
        "content": "### The Sidekicks\n\nSometimes a main verb needs a little help to show the correct time (tense) or meaning. **Helping Verbs** (or Auxiliary Verbs) come BEFORE the main verb.\n\n- *Main Verb only:* She **plays** tennis.\n- *With Helping Verb:* She **is** playing tennis. (is = helping, playing = main)\n- *Another Example:* They **have** eaten. (have = helping, eaten = main)\n\n**Common Helping Verbs:** am, is, are, was, were, be, being, been, have, has, had, do, does, did, will, would, can, could, should.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**உதவி வினைச்சொற்கள் (Helping / Auxiliary Verbs):**\nமுக்கிய வினைச்சொல்லுக்கு (Main verb) உதவி செய்வதற்காக அதற்கு முன்னால் வரும் வினைச்சொற்கள். இவை காலம் (Tense) மற்றும் অর্থেরத் தெளிவை உருவாக்குகின்றன.\n\n- *எ.கா:* She **is** playing. (இங்கு 'playing' என்பது முக்கிய செயல். 'is' என்பது அது நிகழ்காலத்தில் நடப்பதைக் குறிக்க உதவும் helping verb).",
        "questions": [
            {"type": "mcq", "question": "What is the role of a helping verb?", "options": ["To replace the main verb", "To help the main verb show tense or meaning", "To act as a noun", "To describe an adjective"], "correct_option_index": 1, "explanation": "It supports the main verb."},
            {"type": "mcq", "question": "In 'I am eating', what is the helping verb?", "options": ["I", "am", "eating", "None"], "correct_option_index": 1, "explanation": "'am' is helping 'eating'."},
            {"type": "mcq", "question": "In 'I am eating', what is the main verb?", "options": ["I", "am", "eating", "None"], "correct_option_index": 2, "explanation": "'eating' is the main action."},
            {"type": "fill", "question": "She ___ finished her homework. (has / jump)", "options": ["has", "jump", "she", "finished"], "correct_option_index": 0, "explanation": "'has' helps 'finished'."},
            {"type": "fill", "question": "They ___ going to the park. (are / went)", "options": ["are", "went", "they", "going"], "correct_option_index": 0, "explanation": "'are' helps 'going'."},
            {"type": "mcq", "question": "Identify the helping verb: 'He will run the race.'", "options": ["He", "will", "run", "race"], "correct_option_index": 1, "explanation": "'will' shows future tense, helping 'run'."},
            {"type": "mcq", "question": "Can 'is' be a main verb AND a helping verb?", "options": ["Yes", "No", "Only main", "Only helping"], "correct_option_index": 0, "explanation": "Main (He is happy) vs Helping (He is running)."},
            {"type": "fill", "question": "I ___ not know the answer. (do / jumping)", "options": ["do", "jumping", "I", "not"], "correct_option_index": 0, "explanation": "'do' helps 'know'."},
            {"type": "fill", "question": "We ___ been waiting for hours. (have / are)", "options": ["have", "are", "we", "waiting"], "correct_option_index": 0, "explanation": "'have' is a helping verb."},
            {"type": "mcq", "question": "Find the entire verb phrase: 'She could have been sleeping.'", "options": ["sleeping", "been sleeping", "could have been sleeping", "She could"], "correct_option_index": 2, "explanation": "It includes all helping verbs + main verb."},
            {"type": "mcq", "question": "Which is NOT a helping verb?", "options": ["was", "has", "did", "apple"], "correct_option_index": 3, "explanation": "Apple is a noun."},
            {"type": "fill", "question": "The dog ___ barking loudly. (was / barked)", "options": ["was", "barked", "dog", "loudly"], "correct_option_index": 0, "explanation": "'was' helps 'barking'."},
            {"type": "mcq", "question": "In 'I did my homework', is 'did' a main or helping verb?", "options": ["Main", "Helping", "Both", "Neither"], "correct_option_index": 0, "explanation": "There is no other verb, so 'did' is the main verb."},
            {"type": "mcq", "question": "In 'I did not go', is 'did' a main or helping verb?", "options": ["Main", "Helping", "Both", "Neither"], "correct_option_index": 1, "explanation": "It helps the main verb 'go'."},
            {"type": "mcq", "question": "Which sentence has NO helping verb?", "options": ["She is reading.", "He will play.", "They walked home.", "I am writing."], "correct_option_index": 2, "explanation": "Walked is the only verb."}
        ]
    },
    {
        "id": "verb_sub_4",
        "title": "Transitive vs Intransitive Verbs",
        "image": "",
        "content": "### Do you need an Object?\n\nAction verbs can be divided into two types:\n\n1. **Transitive Verbs:** These verbs MUST have a direct object receiving the action. (You can ask \"What?\" or \"Who?\" after the verb).\n   - *Example:* She **kicked** the ball. (Kicked what? The ball. Transitive).\n   - *Example:* He **bought** a car. (Bought what? A car. Transitive).\n\n2. **Intransitive Verbs:** These verbs DO NOT take a direct object. They make sense on their own.\n   - *Example:* The baby **cried**. (Cried what? Makes no sense. Intransitive).\n   - *Example:* She **slept** peacefully. (Slept what? Makes no sense. Intransitive).\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**Transitive vs Intransitive:**\n\n1. **Transitive Verbs (செயப்படுபொருள் குன்றிய வினை):** இந்த வினைச்சொற்களுக்கு ஒரு Direct Object (செயப்படுபொருள்) கட்டாயம் தேவை. (எதை? யாரை? என்று கேள்வி கேட்க முடிந்தால் அது Transitive).\n   - *எ.கா:* நான் பந்தை **உதைத்தேன்**. (எதை உதைத்தேன்? பந்தை).\n2. **Intransitive Verbs (செயப்படுபொருள் குன்றா வினை):** இவற்றுக்கு Object தேவையில்லை.\n   - *எ.கா:* குழந்தை **அழுதது**. (எதை அழுதது எனக் கேட்க முடியாது. செயல் அத்துடன் முடிகிறது).",
        "questions": [
            {"type": "mcq", "question": "A transitive verb must have a direct ___.", "options": ["subject", "object", "adjective", "adverb"], "correct_option_index": 1, "explanation": "It needs an object to receive the action."},
            {"type": "mcq", "question": "An intransitive verb does NOT have a direct ___.", "options": ["subject", "object", "noun", "verb"], "correct_option_index": 1, "explanation": "It doesn't transfer action to anything."},
            {"type": "mcq", "question": "In 'I ate an apple', is 'ate' transitive or intransitive?", "options": ["Transitive", "Intransitive", "Linking", "Helping"], "correct_option_index": 0, "explanation": "Ate what? An apple. It has an object."},
            {"type": "mcq", "question": "In 'I sneezed loudly', is 'sneezed' transitive or intransitive?", "options": ["Transitive", "Intransitive", "Linking", "Helping"], "correct_option_index": 1, "explanation": "Sneezed what? Loudly is an adverb, not an object."},
            {"type": "fill", "question": "She reads books. 'Reads' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "she", "books"], "correct_option_index": 0, "explanation": "Reads what? Books."},
            {"type": "fill", "question": "The bird flew away. 'Flew' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "bird", "away"], "correct_option_index": 1, "explanation": "Flew what? No object."},
            {"type": "mcq", "question": "Which sentence contains a transitive verb?", "options": ["The sun shines.", "He laughed.", "She drank milk.", "They arrived."], "correct_option_index": 2, "explanation": "Drank what? Milk."},
            {"type": "mcq", "question": "Which sentence contains an intransitive verb?", "options": ["I wrote a letter.", "The baby slept.", "He caught the ball.", "She painted a picture."], "correct_option_index": 1, "explanation": "Slept takes no object."},
            {"type": "fill", "question": "He gave me a gift. 'Gave' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "he", "gift"], "correct_option_index": 0, "explanation": "Gave what? A gift."},
            {"type": "fill", "question": "The clock ticked. 'Ticked' is ___. (transitive / intransitive)", "options": ["transitive", "intransitive", "clock", "ticked"], "correct_option_index": 1, "explanation": "Ticked what? Nothing."},
            {"type": "mcq", "question": "Can some verbs be BOTH transitive and intransitive depending on the sentence?", "options": ["Yes", "No", "Only helping verbs", "Only linking verbs"], "correct_option_index": 0, "explanation": "Yes. (e.g., 'I read a book' vs 'I love to read')."},
            {"type": "mcq", "question": "Is 'run' transitive or intransitive here? 'I run a business.'", "options": ["Transitive", "Intransitive", "Both", "Neither"], "correct_option_index": 0, "explanation": "Run what? A business."},
            {"type": "mcq", "question": "Is 'run' transitive or intransitive here? 'I run in the park.'", "options": ["Transitive", "Intransitive", "Both", "Neither"], "correct_option_index": 1, "explanation": "Run what? In the park is a location, not a direct object."},
            {"type": "fill", "question": "Transitive verbs answer the question 'Who' or '___'?", "options": ["Why", "Where", "What", "When"], "correct_option_index": 2, "explanation": "Asking 'what' finds the direct object."},
            {"type": "mcq", "question": "Identify the direct object: 'He pushed the cart.'", "options": ["He", "pushed", "the", "cart"], "correct_option_index": 3, "explanation": "The cart receives the push."}
        ]
    },
    {
        "id": "verb_sub_5",
        "title": "Regular vs Irregular Verbs",
        "image": "",
        "content": "### Changing to the Past Tense\n\nWhen we talk about things that happened in the past, verbs change their form.\n\n1. **Regular Verbs:** These follow a simple, predictable rule. To make them past tense, you just add **-ed** or **-d** to the end.\n   - *Examples:* walk -> walked, jump -> jumped, smile -> smiled.\n\n2. **Irregular Verbs:** These DO NOT follow the rules! They completely change their spelling in the past tense (or don't change at all). You just have to memorize them.\n   - *Examples:* go -> went, eat -> ate, catch -> caught, run -> ran.\n   - *No change:* put -> put, cut -> cut.\n\n---\n\n### தமிழ் விளக்கம் (Tamil Explanation)\n\n**Regular vs Irregular Verbs:**\n\n1. **Regular Verbs:** கடந்த காலத்திற்கு (Past tense) மாற்றும்போது, வழக்கமாக '-ed' அல்லது '-d' சேர்த்து எழுதப்படும் வினைகள்.\n   - *எ.கா:* play -> played.\n2. **Irregular Verbs:** கடந்த காலத்திற்கு மாறும்போது, ஸ்பெல்லிங் (spelling) முற்றிலும் மாறுபடும் அல்லது மாறாமலேயே இருக்கும். இவற்றுக்கு விதிகள் இல்லை.\n   - *எ.கா:* write -> wrote, buy -> bought, cut -> cut.",
        "questions": [
            {"type": "mcq", "question": "How do you make a regular verb past tense?", "options": ["Add -ing", "Add -ed or -d", "Add -s", "Change the vowel"], "correct_option_index": 1, "explanation": "Regular verbs follow the -ed rule."},
            {"type": "mcq", "question": "Which of these is a regular verb?", "options": ["eat", "go", "play", "see"], "correct_option_index": 2, "explanation": "Play becomes played."},
            {"type": "mcq", "question": "Which of these is an irregular verb?", "options": ["talk", "run", "jump", "walk"], "correct_option_index": 1, "explanation": "Run becomes ran (not runned)."},
            {"type": "fill", "question": "The past tense of 'work' is ___. (regular)", "options": ["worked", "worken", "wrought", "working"], "correct_option_index": 0, "explanation": "Add -ed."},
            {"type": "fill", "question": "The past tense of 'sing' is ___. (irregular)", "options": ["singed", "sang", "sung", "singing"], "correct_option_index": 1, "explanation": "Irregular spelling change."},
            {"type": "mcq", "question": "What is the past tense of 'catch'?", "options": ["catched", "caught", "cot", "catch"], "correct_option_index": 1, "explanation": "Caught is the irregular past tense."},
            {"type": "mcq", "question": "What is the past tense of 'buy'?", "options": ["buyed", "bought", "bring", "brought"], "correct_option_index": 1, "explanation": "Bought is the irregular past tense."},
            {"type": "fill", "question": "He ___ to school yesterday. (go -> past tense)", "options": ["goed", "went", "gone", "going"], "correct_option_index": 1, "explanation": "Went is the past tense of go."},
            {"type": "fill", "question": "She ___ the door. (close -> past tense)", "options": ["closed", "cloze", "close", "closing"], "correct_option_index": 0, "explanation": "Closed is regular."},
            {"type": "mcq", "question": "Is 'put' regular or irregular?", "options": ["Regular", "Irregular", "Both", "Neither"], "correct_option_index": 1, "explanation": "Past tense is 'put' (not putted), so it's irregular."},
            {"type": "mcq", "question": "What is the past tense of 'teach'?", "options": ["teached", "taught", "tought", "teach"], "correct_option_index": 1, "explanation": "Taught is irregular."},
            {"type": "fill", "question": "We ___ a movie. (watch -> past tense)", "options": ["watched", "watchen", "watching", "watch"], "correct_option_index": 0, "explanation": "Watched is regular."},
            {"type": "fill", "question": "I ___ a letter. (write -> past tense)", "options": ["writed", "wrote", "written", "writing"], "correct_option_index": 1, "explanation": "Wrote is irregular."},
            {"type": "mcq", "question": "Which verb doesn't change spelling in the past tense?", "options": ["eat", "see", "cut", "look"], "correct_option_index": 2, "explanation": "Cut -> cut."},
            {"type": "mcq", "question": "Is 'think' regular or irregular?", "options": ["Regular (thinked)", "Irregular (thought)", "Both", "Neither"], "correct_option_index": 1, "explanation": "Thought is irregular."}
        ]
    }
]

with open('data/curriculum.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

verb_topic = next((t for t in data['topics'] if t['name'] == 'Verb'), None)
if not verb_topic:
    verb_topic = {
        "name": "Verb",
        "subtopics": []
    }
    data['topics'].append(verb_topic)

existing_ids = [s['id'] for s in verb_topic['subtopics']]
for sub in new_subtopics:
    if sub['id'] not in existing_ids:
        verb_topic['subtopics'].append(sub)

with open('data/curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Added Verb learning subtopics 1 to 5 successfully!")
