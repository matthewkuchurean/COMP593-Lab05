import requests

POKE_URL = 'https://pokeapi.co/api/v2/pokemon/'

def search_for_pokemon(pokedex_info):
    """Checks the pokemon in the PokeAPI
    Args:
        pokedex_info (str): Pokemon name or Pokedex number
    Returns:
        str: Returns the pokemons information from the API and if it's a real pokemon
    """
    pokedex_info = str(pokedex_info).strip().lower()
    pokedex = POKE_URL + pokedex_info
    resp_msg = requests.get(pokedex)
    if resp_msg.ok:
        info = resp_msg.json()
        real = True
        return info, real
    else:
        real = False
        return None, real
        
print(search_for_pokemon('Ninetales'))