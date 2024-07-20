import random
from playwright.sync_api import Page, expect # Synchronous API
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


# --headed: to see browser
# --headless: to NOT see browser (faster)

# Accepts Page object
def test_basic_duckduckgo_search(
    page : Page,
    search_page : DuckDuckGoSearchPage,
    result_page : DuckDuckGoResultPage
    ) -> None:

    search_input_list = ["Kendrick", "Python", "Spongebob"]
    SEARCH_INP = random.choice(search_input_list)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search(SEARCH_INP)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(SEARCH_INP)

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(SEARCH_INP)

    # And the search result title contains the phrase
    expect(page).to_have_title(f"{SEARCH_INP} at DuckDuckGo")
