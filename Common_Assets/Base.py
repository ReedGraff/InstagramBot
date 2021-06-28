from datetime import datetime

time = datetime.today()
current_time = time.strftime("%H:%M:%S")
current_date = time.strftime("%B %d, %Y")


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.filepath = []
    
    def log(self):
        print("\n" * 5)
        print("Now running " + self.username + " at " + current_time + " on " + current_date)
        print("\n" * 5)
        try:
            import os 
            import glob
            cookie_del = glob.glob("config/*cookie.json")
            os.remove(cookie_del[0])
        except:
            print("Skipped the delete")
    
    def DIY_txt_to_list(self, filepath):
        file = open(filepath, "r")
        list_of_lists = [(line.strip()).split() for line in file]
        file.close()
        flat_list = []
        for sublist in list_of_lists:
            for item in sublist:
                flat_list.append(item)
        self.flat_list = flat_list
    
    def DIY_follow_from_list(self):
        # Requires DIY_txt_to_list to be run prior
        list_of_users = self.flat_list

        import os
        import sys
        from time import sleep
        from random import randint

        sys.path.append(os.path.join(sys.path[0], "../"))
        from instabot import Bot

        bot = Bot()
        bot.login(username=self.username, password=self.password)
        
        def check_if_string_in_file(file_name, string_to_search):
            """ Check if any line in the file contains given string """
            with open(file_name, 'r') as read_obj:
                for line in read_obj:
                    if string_to_search in line:
                        return True
            return False
        
        for i in list_of_users:
            if check_if_string_in_file('config/followed.txt', bot.get_user_id_from_username(i)):
                print("Already following " + i + " skipping...")
            else:
                print("Attempting to follow " + i)
                bot.follow(bot.get_user_id_from_username(i))
                print("Successfully followed " + i)
                # sleep(randint(40, 100))


        """
        for i in list_of_users:
            print("Attempting to follow " + i)
            bot.follow(bot.get_user_id_from_username(i))
            print("Successfully followed " + i)
            sleep(randint(40, 100))
        """
        """
        with open("config/followed.txt") as followed:
            for i in list_of_users:
                id = str(bot.get_user_id_from_username(i)
                if id in followed.read():
                    print("Already following " + i + " skipping...")
                else:
                    print("Attempting to follow " + i)
                    bot.follow(bot.get_user_id_from_username(i))
                    print("Successfully followed " + i)
                    sleep(randint(40, 100))
        """
    
    def DIY_follow_from_list_with_selenium(self):
        # Requires DIY_txt_to_list to be run prior
        list_of_users = self.flat_list

        from time import sleep
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from random import randint
        from selenium.webdriver.common.keys import Keys

        """
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
        """
        driver = webdriver.Chrome(executable_path="chromedriver.exe")

        driver.get("https://www.instagram.com/")
        sleep(5)
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.username)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        driver.find_element_by_xpath("//button[@type='submit']")\
            .click()
        for i in list_of_users:
            sleep(5)
            search = driver.find_element_by_xpath("//input[@type='text']")
            search.send_keys(i)
            sleep(5)
            user = driver.find_element_by_class_name("-qQT3")
            user.click()
            sleep(5)
            """
            # Inner_Value = inside of follow btn https://www.tutorialspoint.com/get-html-source-of-webelement-in-selenium-webdriver-using-python
            Button_path = driver.find_element_by_class_name("_5f5mN    -fzfL     _6VtSN     yZn4P   ")
            Button_path = driver.find_element_by_class_name("sqdOP  L3NKy   y3zKF     ")
            Button_path = driver.find_element_by_class_name("//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
            Button_path = driver.find_element_by_class_name("//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button")
            Button_path = driver.find_element_by_class_name("//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
            # list of possible buttons... iterate through each and see if any has an innnerhtml of folow, requested... if none then print assumned following
            """
            possible_buttons = driver.find_elements_by_tag_name("button")
            """
            for j in possible_buttons:
                Inner_Value = j.get_attribute("innerHTML")
                if Inner_Value == "Follow" or Inner_Value == "Follow Back":
                    print("Attempting to follow " + i)
                    sleep(randint(50, 100))
                    j.click()
                    print("Assumed following " + i)
                    # Instabot check if followed?
                elif Inner_Value == "Request":
                    print("Already requested to follow " + i)
                else:
                    print("Assumed following " + i)
                    # Instabot check if followed?
            """
            btn_num = 0
            for j in possible_buttons:
                Inner_Value = j.get_attribute("innerHTML")
                if Inner_Value == "Follow" or Inner_Value == "Follow Back":
                    print("Attempting to follow " + i)
                    sleep(randint(50, 100))
                    j.click()
                    print("Assumed following " + i)
                    # Instabot check if followed?
                elif Inner_Value == "Request":
                    print("Already requested to follow " + i)
                else:
                    print("Checking Button #" + str(btn_num) + " on " + i + "'s page")
                    btn_num += 1
