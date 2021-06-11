# Single User Automation
# Can send predecided messages to a specifed user



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import pytz
from selenium.common.exceptions import NoSuchElementException


chromedriver_path = r'C:\Users\Rishabh\Downloads\chromedriver_win32\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
webdriver.get("https://web.whatsapp.com/")
wait = WebDriverWait(webdriver, 60)
print("Scan the QR code and press Y")
c = input("Y to continue")


# SET IST
IST = pytz.timezone('Asia/Kolkata')


def searchUser(user):
    searchBar = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")))
    searchBar.clear()

    count = 0


    try:
        #Type user name in search bar
        searchBar.send_keys(user+Keys.ENTER)
        # / html / body / div / div[1] / div[1] / div[4] / div[1] / header / div[2] / div[2] / span

        #Wait Unitl user contact pops up
         #86400
        # selected_contact = wait.until(EC.presence_of_element_located((
        #     By.XPATH, "//span[@title='" + user + "'")))
        # sleep(5)

        # selected_contact.click()

        print("Search Done")





    except Exception as e :
        print("Error in search")
        print(e)







def checkOnline( ):


    while(True):
       # _7yrSq _3-8er selectable-text copyable-text
       try:
           #  86400

           # isOnline = WebDriverWait(webdriver, 86400).until(EC.presence_of_element_located((
           #     By.XPATH, '/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span')))

           isOnline = webdriver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span')

           if isOnline != None :

                return True


       except Exception as e:
           # print("Error checking online ")
           # print(e)
           return False




first_time = False
now = datetime.now(IST)
time1 = now.replace(hour=12, minute=30, second=0, microsecond=0)
# time1 = now.replace(hour=6, minute=0, second=0, microsecond=0)
time1Bool = False
time2 = now.replace(hour = 11, minute =0, second =0, microsecond =0)
# time2 = now.replace(hour=6, minute=0, second=0, microsecond=0)
time2Bool = False






memories =[""]   # Messages to be send based in msgTime list


#MSG LIST

msgTime = [now.replace(hour=9, minute=0, second=0, microsecond=0), now.replace(hour=9, minute=45, second=0, microsecond=0),
           now.replace(hour=10, minute=30, second=0, microsecond=0),now.replace(hour=10, minute=50, second=0, microsecond=0),
           now.replace(hour=11, minute=0, second=0, microsecond=0), now.replace(hour=11, minute=30, second=0, microsecond=0),
           now.replace(hour=12, minute=0, second=0, microsecond=0),now.replace(hour=12, minute=30, second=0, microsecond=0)]

def chat():
    datetime_ist = datetime.now(IST)
    onlineTime =  datetime_ist.strftime('%H:%M')
    msg = ""
    global first_time
    msg += "Hi ! Ma'am you  are online :)  , at time : " + onlineTime + ":-* \n"
    if first_time == False:
        msg = ""  # First time msg, like good morning, hello
        first_time = True


    global time1
    global time1Bool
    global time2
    global time2Bool

    if time1 < datetime_ist  and time1Bool == False:
        msg += " "  # Msg to be added on specific time 1
        time1Bool = True
    if time2 < datetime_ist and time2Bool == False :
        msg += " "  # Msg to be added on specific time 2
        time2 = time2.replace(hour = 12, minute =0, second =0, microsecond =0)
        time2Bool = True
    global memories

    global msgTime
    if len(msgTime) >0:
        time3 = msgTime[0]
    if time3 < datetime_ist and len(memories) >0:
        msg += "Here is msg from him \n"
        msg += memories.pop(0)
        msg += ":-*"
        msgTime.pop(0)




    try:
        msg_x = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"

        msgBox = wait.until(EC.presence_of_element_located((
            By.XPATH, msg_x)))
        msgBox.click()
        msgBox.send_keys(msg + Keys.ENTER)
    except Exception as e:
        print(e)
        print("Error in sending chat")

def process():
    try :


        searchUser("")  # USERS NAME

        flag = False
        flag1 = True
        sleep(5)
        while True:
            if checkOnline() == False:

                flag = True
                flag2 = False
                sleep(5)

            elif checkOnline() == True and flag == True and flag2 == False:
                datetime_ist = datetime.now(IST)
                onlineTime = datetime_ist.strftime('%H:%M')
                print("Online @[" + onlineTime + "]")
                flag = False

            if flag == False:
                print("Online")
                flag = True
                flag2 = True
                chat()
    except Exception as e:
        print(e)
        sleep(120)
        process()



# process()



def try_msg():
    try:
        ele = webdriver.find_elements(By.CLASS_NAME,"_3XpKm_20zqk")
        print(len(ele))
        print(ele[::-1].get_attribute('aria-label'))
        c = int(input("Try again ?  press 1"))
        if c == 1:
            try_msg()
    except Exception as e:
        print(e)
        c = int(input("Try again ?  press 1"))
        if c == 1:
            try_msg()




# input("PRESS ANY KEY")
# sleep(5)
# try_msg()
#


# under process
def replied():

        #     _3ExzF
        #
        # document.getElementsByClassName("_3XpKm _20zqk")[11].children[0].getAttribute("aria-label")
        input("Press")
        sleep(5)
        ele = webdriver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[3]/div[20]/div/div/div/div[1]/div")
        print(ele)
        print(ele.text)

        ele





# try:
#     replied()
# except Exception as e:
#     print(e)
#     replied()
#
#
#
#
#
