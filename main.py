import threading
import time

import random as ran

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions

# Local modules
import credentials


# Browser engine
def get_driver():
    options = webdriver.ChromeOptions()
    # Insert settings here
    options.headless = True # Comment this line to see browsers
    options.add_argument('--incognito')
    dr = webdriver.Chrome(options=options)
    return dr


# Mass create accounts
def create_account(url, list_username, list_kingdom, random=False):
    dr = get_driver()
    dr.get(url)
    while True:
        if random:
            local_random = ran.Random()
            username = local_random.choice(list_username)
            kingdom = local_random.choice(list_kingdom)
        else:
            username = list_username
            kingdom = list_kingdom
        # Credentials
        password = credentials.password()
        try:
            filler_username = f'{username}{credentials.filler(len(username))}'
            filler_kingdom = f'{kingdom}{credentials.filler(len(kingdom))}'
            # Goto signup
            dr.find_element(By.ID, 'SignupButton').click()
            # Fill form
            dr.find_element(By.NAME, 'username').send_keys(filler_username)
            dr.find_element(By.NAME, 'password').send_keys(password)
            dr.find_element(By.NAME, 'repeat-password').send_keys(password)
            # captcha = dr.find_element(By.XPATH, '//form[@class="centered account-form"]/p').text
            # dr.find_element(By.NAME, 'captcha').send_keys(captcha[:11])
            dr.find_element(By.CLASS_NAME, 'submit-button').click()
            # Create kingdom
            dr.find_element(By.LINK_TEXT, 'Siege!').click()
            dr.find_element(By.NAME, 'kingdom_name').send_keys(filler_kingdom)
            dr.find_element(By.CLASS_NAME, 'submit-button').click()
            # Logout
            dr.find_element(By.LINK_TEXT, 'Logout').click()
            print(f'Account created with username: {filler_username} and kingdom name: {filler_kingdom}')
        except exceptions.NoSuchElementException as e:
            print('Account creation failed')
            print('May be due to SIGNUP_LOCKED or modified element attributes, trying again in 60 seconds')
            time.sleep(60)
            print('trying again')
            time.sleep(1)


# Main function
def main():
    random = False
    url = 'https://yaksiege-1.johnnyl19432.repl.co/'
    username = input('Enter Username (recommended 16 char max) >>> ')
    # Choose random names from list
    if username == 'random':
        random = True
        with open('sus_kingdom.txt', 'r') as f:
            kingdom = f.read().splitlines()
        with open('sus_username.txt', 'r') as f:
            username = f.read().splitlines()
    else:
        kingdom = input('Enter kingdom name (recommended 16 char max) >>> ')
    t = input('Threads? (leave blank for no) >>> ')
    # Create threads
    # Parallel creation
    if t:
        threads = []
        count = int(input("How many? >>> "))
        for i in range(count):
            th = threading.Thread(target=create_account, args=(url, username, kingdom, random))
            th.daemon = True # Quickly quit program
            threads.append(th)
        for th in threads:
            th.start()
        for th in threads:
            th.join()
    else:
        create_account(url, username, kingdom, random)


if __name__ == '__main__':
    main()
