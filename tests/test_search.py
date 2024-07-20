import random
from playwright.sync_api import Page, expect # Synchronous API

HOME="https://www.duckduckgo.com"

# --headed: to see browser
# --headless: to NOT see browser (faster)

# Accepts Page object
def test_basic_duckduckgo_search(page : Page) -> None:
    search_input_list = ["Kendrick", "Python", "Spongebob"]
    SEARCHBOX_INP = "#searchbox_input"
    SEARCH_FORM_INP = "#search_form_input"
    BTN = "Search" # aria-label
    RESULTS_LIST = 'li[data-layout="organic"]'
    SEARCH_INP = random.choice(search_input_list)
    # Given the DuckDuckGo home page is displayed
    page.goto(HOME)
    # When the user searches for a phrase
    page.locator(SEARCHBOX_INP).fill(SEARCH_INP)
    page.get_by_role("button").all()[1].click()
    # Then the search result query is the phrase
    expect(page.locator(SEARCH_FORM_INP)).to_have_value(SEARCH_INP)
    # And the search result links pertain to the phrase
    page.locator(RESULTS_LIST).nth(4).wait_for()
    titles = page.locator(RESULTS_LIST).all_text_contents()
    matches = [t for t in titles if SEARCH_INP.lower() in t.lower()]
    assert len(matches) > 0
    # And the search result title contains the phrase
    expect(page).to_have_title(f"{SEARCH_INP} at DuckDuckGo")
