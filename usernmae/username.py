def username():
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
        return username
