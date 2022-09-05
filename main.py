from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def main():
    br = webdriver.Chrome(ChromeDriverManager().install())
    br.get('https://yaksiege-1.johnnyl19432.repl.co/')
    # Credentials
    username = 'JohnnyLbozo'
    password = 'AVeryLongPassword' # impliment random pass generator
    kingdom = 'OhNoYouHaveVirus'
    iteration = 220
    while True:
        iteration += 1
        # Goto signup
        br.find_element(By.LINK_TEXT, 'Signup').click()
        # Fill form
        br.find_element(By.NAME, 'username').send_keys(f'{username}{str(iteration)}')
        br.find_element(By.NAME, 'password').send_keys(password)
        br.find_element(By.NAME, 'repeat-password').send_keys(password)
        br.find_element(By.CLASS_NAME, 'submit-button').click()
        # create kingdom
        br.find_element(By.LINK_TEXT, 'Siege!').click()
        br.find_element(By.NAME, 'kingdom_name').send_keys(f'{kingdom}{str(iteration)}')
        br.find_element(By.CLASS_NAME, 'submit-button').click()
        # logout
        br.find_element(By.LINK_TEXT, 'Logout').click()

if __name__ == '__main__':
    main()