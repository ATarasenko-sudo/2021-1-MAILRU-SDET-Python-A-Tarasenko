from selenium.webdriver.common.by import By


class StartPageLocators:

    CHECK_LANGUAGE_LOCATOR = (By.XPATH, '//div[contains(text(), "En")]')
    AUTH_RU_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(), "Войти")]')
    AUTH_EN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(text(), "Log in")]')
    AUTH_EMAIL_ROW_LOCATOR = (By.NAME, 'email')
    AUTH_PASSWOR_ROW_LOCATOR = (By.NAME, 'password')
    LOGGIN_RU_BUTTON_LOCATOR = (By.XPATH, '//div[@class = "js-target-common-modals"]//div[contains(text(), "Войти")]')
    LOGGIN_EN_BUTTON_LOCATOR = (By.XPATH, '//div[@class = "js-target-common-modals"]//div[contains(text(), "Log in")]')
    WRONG_LOG_PASS_LOCATOR = (By.XPATH, '//div[@class = "formMsg_text"]/text()')

class FailAutorizationPageLocators(StartPageLocators):
    WRONG_LOG_PASS_LOCATOR = (By.XPATH, '//div[@class = "formMsg_text"]')

class CampaignPageLocators(StartPageLocators):
    CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(text(), "Create campaign")]')
    TRAFFIC_LOCATOR = (By.XPATH, '//div[contains(text(), "Traffic")]')
    ENTER_URL_LOCATOR = (By.XPATH, '//div[@class="js-main-url-wrap"]//input')

    CAMPAIGN_NAME_LOCATOR = (By.XPATH,'//div[@class = "campaign-name"]//div[@class="input__wrap"]//input')

    OPEN_SLIDER_LOCATOR = (By.XPATH, '//div[@data-scroll-name = "setting-age"]')
    SELECT_AGE_LOCATOR = (By.XPATH, '//div[@class="age-setting"]//div[@class="select"]')
    SELECT_CUSTOM_AGE_LOCATOR = (By.XPATH, '//div[@class="age-setting"]//div[@class="select"]//span[contains(text(), "Custom age set")]')
    INPUT_AGE_LOCATOR = (By.XPATH, '//div[@class="textarea"]//div//textarea')

    OPEN_LOCATION_LOCATOR = (By.XPATH, '//div[@class = "js-header-wrapper"]//span[@class="js-setting-label-separator"]')
    INPUT_REGION_LOCATOR = (By.XPATH, '//div//input[@placeholder="Add or remove region"]')
    ADD_REGION_LOCATOR = (By.XPATH, '//div[@class=""]//div[contains(text(), "Add")]')

    PAYMENT_LOCATOR = (By.XPATH,'//span[contains(text(), "optimize Clicks, paying for Clicks, strategy: Maximum number of clicks")]')
    CLICK_LOCATOR = (By.ID, "optimization-item-1")
    IMP_LOCATOR = (By.ID, "optimization-item-0")


    
    OPEN_CURRENT_OPTIONS_LOCATOR = (By.XPATH, '//div[@class="js-header-wrapper"]//span[contains(text(), "Context targeting")]')

    ENTER_CATEGORY_LOCATOR = (By.XPATH, '//div[@class="js-context-form-wrap"]//input')
    TEXT_CONTEXT_LOCATOR = (By.XPATH, '//div[@class="js-context-form-wrap"]//textarea')
    CREATE_CONTEXT_LOCATOR = (By.XPATH, '//div[contains(text(), "Create")]')

    GROUP_CONFIG_LOCATOR = (By.XPATH, '//div[@class="js-header-wrapper"]//span[contains(text(), "Groups and applications in social networks")]')
    ENTER_GROUP_LOCATOR = (By.XPATH, '//div[@class = "js-apps-and-groups-wrap"]//input')
    SELECT_GROUP_LOCATOR = (By.XPATH, '//div[contains(text(), "Select all")]')
    CREATE_GROUP_LOCATOR = (By.XPATH, '//div[@class = "js-apps-and-groups-wrap"]//div[@data-test="button"]//div[contains(text(),"Create")]')



    BUDGET_LOCATOR = (By.XPATH, '//span[@title = "budget is unlimited"]')
    DAILY_BUDGET_LOCATOR = (By.XPATH, '//div[@class = "budget-setting__item-wrap"]//input[@data-test = "budget-per_day"]')
    TOTAL_BUDGET_LOCATOR = (By.XPATH, '//div[@class = "budget-setting__item-wrap"]//input[@data-test = "budget-total"]')

    ADS_FORMAT_LOCATOR = (By.XPATH, '//span[contains(text(), "Teaser")]')


    AD_TITLE_LOCATOR = (By.XPATH, '//input[@placeholder = "Enter ad title"]')
    AD_TEXT_LOCATOR = (By.XPATH, '//textarea[@placeholder = "Enter ad text"]')

    BIG_IMG_LOCATOR = (By.XPATH,'//div[@class = "js-pattern-banners"]')
    UPLOAD_LOCATOR = (By.XPATH, '//input[@type ="file"]')
    IMG_MENU_LOCATOR = (By.XPATH,'//div[contains(text(), "Show creative library")]')
    SMALL_IMG_LOCATOR = (By.XPATH, '//input[@type="file"][@data-test = "image_90x75"]')
    CROPP_SUBMIT_LOCATOR = (By.XPATH, '//div[@class = "image-cropper"]//input[@type = "submit"]')
    
    SAVE_AD_LOCATOR = (By.XPATH, '//div[@data-test="submit_banner_button"]')

    CREATE_NEW_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(text(), "Create a campaign")]')

    CHECK_CAMPAIGN_LOCATOR = (By.XPATH, '//a[@title]')

    


class CampaignMenuPageLocators(StartPageLocators):
    FIND_CHECKBOX_LOCATOR = (By.XPATH, '//div[@data-row-id="central-1"]//div[@data-entity-type="campaign"]//input ')
    FIND_ACTION_MENU_LOCATOR = (By.XPATH, '//div[@data-test="select"]//span[contains(text(), "Actions")]')
    DELETE_BUTTON_LOCATOR = (By.XPATH, '//li[@title = "Delete"]')



class SegmentConfigPageLocators(StartPageLocators):
    GO_TO_SEGMENTS_LOCATOR = (By.XPATH, '//a[@href = "/segments"]')

    CHECK_EXIST_SEGMENTS = (By.XPATH, '//div[contains(text(),"How to get started?")]')
    CREATE_NEW_SEGMENT = (By.XPATH, '//a[contains(text(),"Create")]')
    CREATE_NEW_SEGMENT_ALT_LOCATOR = (By.XPATH, '//button//div[contains(text(),"Create segment")]')

    APPS_AND_GAMES_LOCATOR = (By.XPATH, '//div[contains(text(),"Apps and games in social networks")]')
    GROUPS_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(text(),"Groups OK and VK")]')

    SEARCH_SEGMENT_LOCATOR = (By.XPATH, '//div[@class = "sources-list"]//div[@class="input__wrap"]//input')
    CHECKBOX_SEGMENT_LOCATOR = (By.XPATH, '//div[@class = "adding-segments-source"]//div//input')

    ADD_SEGMENT_BUTTON_LOCATOR = (By.XPATH, '//div[@class="adding-segments-modal"]//button[@data-class-name="Submit"]')

    
    SEGMENT_NAME_FIELD_LOCATOR = (By.XPATH,'//div[@class ="js-segment-name" ]//input')
    SUBMIT_SEGMENT_LOCATOR = (By.XPATH, '//button[@data-class-name = "Submit"]')

    CHECK_SEGMENT_LOCATOR = (By.XPATH, '//a[@title]')


    CHECKBOX_SEGMENT_MENU_LOCATOR = (By.XPATH, '//div[@aria-label="grid"]//div[@data-row-id="central-0"]//input')
    SAVE_ID_LOCATOR = (By.XPATH, '//div[@data-row-id="central-0"]//span')
    ACTIONS_BUTTON_LOCATOR = (By.XPATH, '//span[contains(text(), "Actions")]')
    REMOVE_BUTTON_LOCATOR = (By.XPATH, '//li[contains(text(), "Remove")]')
    

    











