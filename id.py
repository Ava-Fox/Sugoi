import uuid
import json

bleh = {
    1: {
        "prompt": "How are you?",
        "answers": {
            "I'm good": 2
        }
    },
    2: {
        "prompt": "OK",
        "answers": {
            "How are you?": 1,
            "Goodbye": None
        }
    }
}

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(bleh))

