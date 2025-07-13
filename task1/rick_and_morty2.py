import requests
import csv

def get_characters():
    characters = []
    page = 1
    while True:
        response = requests.get(f"https://rickandmortyapi.com/api/character?page={page}")
        data = response.json()
        for character in data['results']:
            if (
                character['species'] == 'Human' and
                character['status'] == 'Alive' and
                "Earth" in character['origin']['name']
            ):
                characters.append({
                    'Name': character['name'],
                    'Location': character['location']['name'],
                    'Image': character['image']
                })
        if not data['info']['next']:
            break
        page += 1
    return characters

def write_to_csv(characters):
    with open('rick_and_morty_characters.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Location', 'Image'])
        writer.writeheader()
        for character in characters:
            writer.writerow(character)

def main():
    characters = get_characters()
    write_to_csv(characters)

if __name__ == "__main__":
    main()

