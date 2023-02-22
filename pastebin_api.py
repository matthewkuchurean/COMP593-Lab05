import requests 

developer_key = 'COoML7cUu-s0tkE_pcTv8EpzMg9Z_sU0'
pastebin_api_url = "https://pastebin.com/api/api_post.php"
resp_msg = requests.get(pastebin_api_url)

def main ():
    url = ("This is a title", "this\nis\nthe\n body", '1H', True)
    print(f'New paste URL: {url}')

def post_new_paste(title, body_text, expiration='10M',listed=False):
    # SETUP PARAMS 

    paste_params = {
        'api_dev_key': developer_key, 
        'api_option': 'paste',
        'api_paste_code': body_text, 
        'api_paste_name': title,
        'api_paste_expire_expire_date': expiration,
        'api_paste_private' : 0 if listed else 1
    }  
# send the post request 

    print('Sending post request')
    resp_msg = requests.post(pastebin_api_url, data=paste_params)

    if resp_msg.ok:
        print('sucess')
        return resp_msg.text
    else:
         print(f'Request failed.')
         print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
         print(f'Reason: {resp_msg.text}') 
#return

if '__name__' == '__main__':
    main()

