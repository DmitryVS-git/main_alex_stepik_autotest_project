from datetime import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')

    # Method assert a word
    def assert_word(self, word, expected_result):
        value_word = word.text
        assert value_word == expected_result, f'Word "{value_word}" != Expected result "{expected_result}"'
        print('Good value word')

    # Method making a screenshot
    def make_screenshot(self):
        date_now = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        name_screenshot = f'screenshot_{date_now}'
        self.driver.save_screenshot(f".\\screen\\{name_screenshot}.png")

    # Method assert url
    def assert_url(self, given_url):
        get_url = self.driver.current_url
        assert get_url == given_url, 'URL are different!'
        print('Good value URL')
