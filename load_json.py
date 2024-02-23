import json

with open("sample.json", "r") as file:
    data = json.loads(file.read())
    print(data)
    start = data['1']
    while True:
        print(start['prompt'])
        answer = input("> ")
        if answer in start['answers']:
            if answer == "Goodbye":
                break
            next_start = start['answers'][answer]
            print(next_start)
            start = data[str(next_start)]