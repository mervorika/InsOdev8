import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()

HOME_PAGE_LOCATOR = "https://seleniumautomation.inone.useinsider.com/"
HomePageExpectedTitle = "Inone - Login - Insider Inone"

driver.get(HOME_PAGE_LOCATOR)
time.sleep(2)
assert HomePageExpectedTitle == driver.title
print("INFO: seleniumautomation anasayfası başarıyla açıldı.")


SIGN_IN_EMAIL_LOCATOR = '//input[@id="email"]'
emailInput = driver.find_element(by=By.XPATH, value = SIGN_IN_EMAIL_LOCATOR)
emailInput.send_keys("EMAIL")

SIGN_IN_PASSWORD_LOCATOR = '//input[@id="password"]'
passwordInput = driver.find_element(by=By.XPATH, value = SIGN_IN_PASSWORD_LOCATOR)
passwordInput.send_keys("PASSWORD")

SIGN_IN_SUBMIT = '//button[@id="login-button"]'
submitButton = driver.find_element(by=By.XPATH, value = SIGN_IN_SUBMIT)
submitButton.click()

time.sleep(2)


INSTORY_LOCATOR = "https://seleniumautomation.inone.useinsider.com/instory-all"

driver.get(INSTORY_LOCATOR)
time.sleep(2)

CREATE_INSTORY = '//button[@id="create-mobile-campaign"]'
createButton = driver.find_element(by=By.XPATH, value = CREATE_INSTORY)
createButton.click()

time.sleep(3)

CAMPAIGN_NAME_LOCATOR = '//input[@id="campaign-name"]'
campName = driver.find_element(by=By.XPATH, value = CAMPAIGN_NAME_LOCATOR)
campName.send_keys("mbtest4")
campaignName = "mbtest4"

CREATE_BUTTON = '//button[@id="accept"]'
createButton = driver.find_element(by=By.XPATH, value = CREATE_BUTTON)
createButton.click()

time.sleep(7)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(4)

PAGE_RULES_LOCATOR = '//a[contains(@class, "qa-page-rules")]'
pageRules = driver.find_element(by=By.XPATH, value = PAGE_RULES_LOCATOR)
pageRules.click()

time.sleep(4)

RULE_SELECTOR = '//button[@id="conditionList0"]'
ruleSelector = driver.find_element(by=By.XPATH, value = RULE_SELECTOR)
ruleSelector.click()

time.sleep(4)

PAGE_TYPE_RULE = '//a[contains(@class, "conditionList0-page-type")]'
pageType = driver.find_element(by=By.XPATH, value = PAGE_TYPE_RULE)
pageType.click()

time.sleep(4)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(8)

NEW_VARIATION = '//button[@id="add-new-variation"]'
newVariation = driver.find_element(by=By.XPATH, value = NEW_VARIATION)
newVariation.click()

time.sleep(4)

SINGLE_STORY = '//ul[@class="template-list"]/li[1]//a[@class="btn-select"]'
singleStory = driver.find_element(by=By.XPATH, value = SINGLE_STORY)
singleStory.click()

time.sleep(15)

OK_BUTTON = '//div[@id="inline-select-notification"]//a'
okButton = driver.find_element(by=By.XPATH, value = OK_BUTTON)
okButton.click()

time.sleep(4)
driver.switch_to.frame(driver.find_element(by=By.XPATH, value = '//iframe[@id="ins-skeleton-partner-iframe"]'))
HEADER_NAV_DIV = '//div[@class="top-header"]'
headerDiv = driver.find_element(by=By.XPATH, value = HEADER_NAV_DIV)
headerDiv.click()

time.sleep(4)

driver.switch_to.default_content()

APPEND_AFTER = '//li[contains(@class, "append-after")]'
appendAfter = driver.find_element(by=By.XPATH, value = APPEND_AFTER)
appendAfter.click()

time.sleep(6)

SAVE_BUTTON = '//button[@id="save"]'
saveButton = driver.find_element(by=By.XPATH, value = SAVE_BUTTON)
saveButton.click()

time.sleep(10)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(8)

SAVE_NEXT_BUTTON = '//button[@id="save-and-next"]'
saveNextButton = driver.find_element(by=By.XPATH, value = SAVE_NEXT_BUTTON)
saveNextButton.click()

time.sleep(10)

ACTIVE_BUTTON = '//label[@for="Active"]'
activeButton = driver.find_element(by=By.XPATH, value = ACTIVE_BUTTON)

variationName = driver.find_element(by=By.XPATH, value = '//p[@class="in-form-status-wrapper__text"]').text
variationName = variationName.split(":",1)[0]
variationName = variationName.split("Variation",1)[1]
variationName = "Variation"+variationName

action = ActionChains(driver)
action.move_to_element(driver.find_element(by=By.XPATH, value = '//textarea[@id="note"]')).perform()

activeButton.click()

time.sleep(4)

LAUNCH_BUTTON = '//button[@id="save-and-next"]'
launchButton = driver.find_element(by=By.XPATH, value = LAUNCH_BUTTON)
launchButton.click()

time.sleep(10)

CAMPAIGN_CHECK = '//tbody[@class="vuetable-body"]//div[@data-information="'+campaignName+'"]'

checkVal = False
try:
    campaignCheck = driver.find_element(by=By.XPATH, value = CAMPAIGN_CHECK)
    checkVal = True
except Exception:
    checkVal = False

assert checkVal
print("INFO: Eklenen kampanya başarıyla listede görüntülendi.")

time.sleep(6)
done = False
INSTORIES = '//tbody[@class="vuetable-body"]/tr'
for line in driver.find_elements(by=By.XPATH, value= INSTORIES):
    if done == True:
        break
    name = line.find_element(by=By.XPATH, value='.//td[contains(@class, "camp-name")]//p')
    if name.text == campaignName:
        print("INFO: Eklenen kampanya tespit edildi.")
        status = line.find_element(by=By.XPATH, value='.//td[contains(@class, "camp-status")]//p')
        assert status.text == "Active"
        print("INFO: Eklenen kampanyanın statüsü aktif olarak görüntülendi.")
        testLink = line.find_element(by=By.XPATH, value='.//div[contains(@class, "is-test-link")]//p')
        testLink.click()
        dropdown = line.find_element(by=By.XPATH, value='.//div[contains(@class, "is-test-link")]//div[@id="dropDownList"]')
        assert dropdown.text.__contains__(variationName)
        print("INFO: Eklenen kampanyanın eklenen varyasyonu görüntülendi.")
        done = True


time.sleep(6)

