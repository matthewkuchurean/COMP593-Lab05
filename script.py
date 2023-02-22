from pastebin_api import post_new_paste
from PokeAPI import search_for_pokemon
import sys

def main():
    search_term = get_search_term()
    poke_list = search_for_pokemon(search_term)
    if poke_list:
        title, body_text =get_paste_data(poke_list, search_term)
        paste_url = post_new_paste(title, body_text, '1M')
        print(f'URL of new paste: {paste_url}')

    return

def get_search_term():
    num_params = len(sys.argv) -1
    if num_params >0:
        return sys.argv[1]
    else:
        print("Error: Missing search term")
    return

def get_paste_data(poke_list, search_term):
    title = f'"{search_term}\'s" abilities'
    divider = '\n-'.join(poke_list)
    body_text =  '-' + divider

    return title, body_text

if __name__ == '__main__':
    main()