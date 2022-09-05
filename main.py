import threading
import random
import string
import secrets

from selenium import webdriver
from selenium.webdriver.common.by import By


def filler(length):
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=(20-length)))
    return x


def password():
    p = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(30))
    return p


def get_driver():
    options = webdriver.ChromeOptions()
    options.headless = True # Comment this line to see browsers
    dr = webdriver.Chrome(options=options)
    return dr


def create_account(url, username, kingdom):
    dr = get_driver()
    dr.get(url)
    while True:
        # Credentials
        password = password()
        filler_username = f'{username}{filler(len(username))}'
        filler_kingdom = f'{kingdom}{filler(len(kingdom))}'
        # Goto signup
        dr.find_element(By.ID, 'SignupButton').click()
        # Fill form
        dr.find_element(By.NAME, 'username').send_keys(filler_username)
        dr.find_element(By.NAME, 'password').send_keys(password)
        dr.find_element(By.NAME, 'repeat-password').send_keys(password)
        dr.find_element(By.CLASS_NAME, 'submit-button').click()
        # Create kingdom
        dr.find_element(By.LINK_TEXT, 'Siege!').click()
        dr.find_element(By.NAME, 'kingdom_name').send_keys(filler_kingdom)
        dr.find_element(By.CLASS_NAME, 'submit-button').click()
        # Logout
        dr.find_element(By.LINK_TEXT, 'Logout').click()
        print('Account Created')


def main():
    url = 'https://yaksiege-1.johnnyl19432.repl.co/'
    username = input('Enter Username (recommended 15 char max) >>> ')
    kingdom = input('Enter kingdom name (recommended 15 char max) >>> ')
    t = input('Threads? (leave blank for no) >>> ')
    # Create threads
    if t:
        threads = []
        count = int(input("How many? >>> "))
        for i in range(count):
            th = threading.Thread(target=create_account, args=(url, username, kingdom))
            th.daemon = True
            threads.append(th)
            th.start()
        for th in threads:
            th.join()
    else:
        create_account(url, username, kingdom)


if __name__ == '__main__':
    main()
