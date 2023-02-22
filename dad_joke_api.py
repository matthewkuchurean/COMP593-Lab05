import requests

DAD_JOKE_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKES_SEARCH_URL = f'{DAD_JOKE_API_URL}search'

def main():
    jokes_list = search_for_dad_jokes('cow')
    print(*jokes_list, sep='\n')
    return

def search_for_dad_jokes(search_terms):
    """Gets a list of dad jokes that contain a search term
    Args:
        List (str): list of jokes containing search terms
    """
    # Setup the header parameter
    header_params = {
        'Accept': 'application/json',
    }
    # Setup the query string parameters
    query_str_params = {
        'term': search_terms
    }

 # Send the GET request to the PasteBin API
    print(f'Searching DadJokes API for "{search_terms}" jokes...', end='')
    resp_msg = requests.get(DAD_JOKES_SEARCH_URL, headers=header_params, params=query_str_params)

    # Check whether the GET request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        jokes_portion = body_dict['results']
        jokes_list = [j['joke']for j in jokes_portion]
        return jokes_list
    else:
        print('failed')
        print(f'Status code {resp_msg.status_code} ({resp_msg.reason})')



def get_random_dad_joke():
    """Gets a random dad joke
    Returns:
        str: dad joke
    """
    # Setup the header parameter
    header_params = {
        'Accept': 'application/json',
    }

 # Send the GET request to the PasteBin API
    print('Sending GET request to DadJokes API...', end='')
    resp_msg = requests.get(DAD_JOKE_API_URL, headers=header_params)

    # Check whether the GET request was successful
    if resp_msg.ok:
        print('success')
        joke_dict = resp_msg.json()
        return joke_dict['joke']
    else:
        print('failed')
        print(f'Status code {resp_msg.status_code} ({resp_msg.reason})')


if __name__ == '__main__':
    main()
