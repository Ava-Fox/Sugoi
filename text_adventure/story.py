import uuid
import json

story = {
    "intro": { 
        "title": "In music school...",
        "story": [
            "You're practicing your instrument in music school when a hot guy catches you play.",
        ],
        "player_input": {
            "aspect": "instrument",
            "question": "What do you play?",
            "options": ["bass", "guitar", "drums", "flute"],
            "instrument": "",
            "bass": "bass remark here",
            "guitar": "guitar remark here",
            "drums": "drums remark here",
            "flute": "flute remark here"
        },
        "options": [
            {
                "text": "Go to practice",
                "arc": "practice"
            },
            {
                "text": "Stay at school",
                "arc": "lame"
            }
        ],
    },
    "lame": {
        "title": "You are a coward",
        "story": ["You realize you're too much of a loser to be cool and you drop all of your stuff in your rush to escape, embarrassing yourself thoroughly."],
        "player_input": {},
        "options": []
    },
    "practice": {
        "title": "At Griffin R.'s house",
        "story": ["You made it to practice!"],
        "player_input": {},
        "options": []
    }
}

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(story))