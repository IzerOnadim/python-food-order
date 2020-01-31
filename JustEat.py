from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

details = {}

with open("privateInfo.txt","r") as f:
    # extract the data from the file
    lines = f.read().split("\n")
    # remove empty lines
    lines = list(filter(None, lines))

    for l in lines:
        # split the data on each line
        d = l.split(" ")
        # put the data into a dictionary
        details.update({d[0][:-1] : d[1]})

class JustEatOrder(object):
    def __init__(self, email, password, postcode):

        self.email = email
        self.password = password
        self.postcode = postcode

        # configure options to stop pop-ups
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications" : 1
        })

        # create driver object
        self.driver = webdriver.Chrome(options=options)

    def open(self):
        '''opens the main page'''
        # Load the main page
        self.driver.get("https://www.just-eat.co.uk/")

    def signup(self, name, notifications = False):
        '''Creates a new account with given details'''
        # Load the main page
        self.driver.get("https://www.just-eat.co.uk/")

        # click button that takes you to the login page
        signup_button = self.driver.find_element_by_xpath("//*[@id=\"footer-customer-service\"]/li[3]/a")
        signup_button.click()

        # fill name
        name_fill = self.driver.find_element_by_xpath("//*[@id=\"Name\"]")
        name_fill.send_keys(name)

        # fill email
        email_fill = self.driver.find_element_by_xpath("//*[@id=\"Email\"]")
        email_fill.send_keys(self.email)

        # fill password
        password_fill = self.driver.find_element_by_xpath("//*[@id=\"Password\"]")
        password_fill.send_keys(self.password)

        # stop just eat from sending you notifications
        if not notifications:
            notification_button = self.driver.find_element_by_xpath("//*[@id=\"NewsletterCheckboxValue\"]")

        # press sign up button
        signup_confirm = self.driver.find_element_by_xpath("//*[@id=\"content\"]/div/div/div/div/div[2]/form/div[5]/input")
        signup_confirm.click()

    def login(self):
        '''Logs the user in to their account'''
        # Load the main page
        self.driver.get("https://www.just-eat.co.uk/")

        # click button that takes you to the login page
        login_button = self.driver.find_element_by_xpath("/html/body/app/div/header/div[2]/nav/div/ul/li[2]/a")
        login_button.click()

        # fill email
        email_fill = self.driver.find_element_by_xpath("//*[@id=\"Email\"]")
        email_fill.send_keys(self.email)

        # fill password
        password_fill = self.driver.find_element_by_xpath("//*[@id=\"Password\"]")
        password_fill.send_keys(self.password)

        # press button finish login
        login_confirm = self.driver.find_element_by_xpath("//*[@id=\"login\"]/div[2]/form/div[4]/input")
        login_confirm.click()

    def enter_postcode(self):
        # Load the main page
        self.driver.get("https://www.just-eat.co.uk/")

        # fill in postcode
        postcode_fill = self.driver.find_element_by_xpath("//*[@id=\"skipToMain\"]/form/div/div/label/input")
        postcode_fill.send_keys(self.postcode)

        # click search button
        search_button = self.driver.find_element_by_xpath("//*[@id=\"skipToMain\"]/form/div/button")
        search_button.click()

order = JustEatOrder(details.get("Email"), details.get("Password"), details.get("Postcode"))
order.open()
order.signup(details.get("Name"))
order.enter_postcode()
#order.signup("asdafsdjfhajskdbf", False)
