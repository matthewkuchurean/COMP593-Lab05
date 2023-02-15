import requests

 = 'https://icanhazdadjoke.com/'

def main():
    
    
    return 


def get_random_dad_joke():

    #seeting up header params 
    header_params = {
        'Accept': 'application/json'
    }
print ('Sending GET request to Dad Joke API....', end='') 
resp_msg = requests.get(dad_jokes_url, headers=header_params)
    return
if '__name__' == '__main__'
    main()
