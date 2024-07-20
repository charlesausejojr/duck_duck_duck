from playwright.sync_api import Page

HOME_URL = "https://www.duckduckgo.com"
SEARCHBOX_INP = "#searchbox_input"

# One method per page
class DuckDuckGoSearchPage:
    def __init__(self, page : Page) -> None:
        self.page           = page
        self.search_input   = page.locator(SEARCHBOX_INP)

    def load(self):
        self.page.goto(HOME_URL)
    
    def search(self, phrase : str):
        self.search_input.fill(phrase)
        self.page.get_by_role("button").all()[1].click()
