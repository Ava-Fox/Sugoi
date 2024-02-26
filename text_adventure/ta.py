import json

player = {}

with open("sample.json", "r") as file:
    data = json.loads(file.read())
    arc = data["intro"]
    while True:
        title = arc["title"]
        print(f"~~~~~  {title}  ~~~~~")
        for p in arc["story"]:
            print(p)
        if arc["player_input"]:
            print(arc["player_input"]["question"])
            answer = input("> ")
            if answer in arc["player_input"]:
                print(arc["player_input"][answer])
            aspect = arc["player_input"]["aspect"]
            player[aspect] = answer
        if arc["options"]:
            i = 1
            for op in arc["options"]:
                print(f"{i}.", op["text"])
                i += 1
            choice = int(input("> "))
            choice -= 1
            next_arc = arc["options"][choice]["arc"]
            arc = data[next_arc]
        else:
            print("End of game!")
            print(player)
            break
    
    