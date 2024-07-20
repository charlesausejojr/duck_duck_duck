from playwright.sync_api import Page # Synchronous API

HOME="https://www.duckduckgo.com"

# --headed: to see browser
# --headless: to NOT see browser (faster)

# Accepts Page object
def test_basic_duckduckgo_search(page : Page) -> None:
    search_input_list = ["Kendrick Lamar", "Python", "Spongebob"]
    INP = "#searchbox_input"
    BTN = "Search" # aria-label
    # Given the DuckDuckGo home page is displayed
    page.goto(HOME)
    # When the user searches for a phrase
    page.locator(INP).fill("Kendrick Lamar")
    page.get_by_role("button").all()[1].click()
    # Then the search result query is the phrase
    # And the search result links pertain to the phrase
    # And the search result title contains the phrase
