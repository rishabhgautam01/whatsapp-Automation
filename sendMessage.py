
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd

import time

driver = webdriver.Firefox()
driver.maximize_window()


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 60)
print("Scan the QR code , you have 20 seconds")
c = input("Y to continue")

def sendMsg(target,message):
    searchBar = wait.until(EC.presence_of_element_located((
            By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")))
    searchBar.clear()
        # driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
    # searchBar.click()
    try:
        searchBar.send_keys(target+Keys.ENTER)
        # time.sleep(5)
        # contactTile = driver.find_element_by_class_name("matched-text _3Whw5")

        selected_contact = wait.until(EC.presence_of_element_located((
        	By.XPATH, "//span[@title='" + target + "']")))
            # driver.find_element_by_xpath("//span[@title='" + target + "']")
        # selected_contact = driver.find_element_by_class_name("eJ0yJ _13opk")
        time.sleep(2)
        selected_contact.click()


        time.sleep(5)
        msg_x="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"

        msgBox = wait.until(EC.presence_of_element_located((
            By.XPATH, msg_x)))
        msgBox.click()
        msgBox.send_keys(message+Keys.ENTER)


        return True
    except Exception as e:
        print(e)
        return False



message="""
message content
"""

f = open("sentDetails.txt","w")


df = pd.read_csv("whatsappMsgList.csv")



for i, row in df.iterrows():
    contactNumber =df.at[i, 'Number']
    contactName =df.at[i,"Name"]
    # m = "Hi {} \n{}".format(contactName,message)
    t = sendMsg(contactName,message)

    # time.sleep(5)
    if  t:
        print("Message sent to  {} {} ".format(contactName,contactNumber))
        f.write("{} {} {}\n".format(contactName,contactNumber,"SENT"))
        # time.sleep(5)

    else :
        print("Message not sent to  {} {} ".format(contactName, contactNumber))
        f.write("{} {} {}\n".format(contactName, contactNumber,"NOT SENT"))



f.close()


