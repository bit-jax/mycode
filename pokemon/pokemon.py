import requests
def main():
    pokenum = input("pick a number between 1 and 151!\n>")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    print(pokeapi['sprites']['front_default'])
    for i in pokeapi['moves']:
        print(i['move']['name'])
    # print(pokeapi['game_indices'])
    print('games appeared in: ' + str(len(pokeapi['game_indices'])) + ' games')
main()