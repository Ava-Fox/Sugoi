import json

with open("sample.json", "r") as file:
    data = json.loads(file.read())
    start = data['1']
    while True:
        print(start['prompt'])
        answer = input("> ")
        if answer in start['answers']:
            if answer == "Goodbye":
                print("Goodbye!")
                break
            next_start = start['answers'][answer]
            start = data[str(next_start)]