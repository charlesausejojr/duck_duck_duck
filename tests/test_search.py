import pytest
import random
from playwright.sync_api import Page, expect # Synchronous API
from utils.utils import Utilities
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

# --headed: to see browser
# --headless: to NOT see browser (faster)

RANDOM_WORDS = Utilities().get_random_words(random.randint(5,10))

@pytest.mark.parametrize('phrase', RANDOM_WORDS)
def test_basic_duckduckgo_search(
    phrase: str,
    page : Page,
    search_page : DuckDuckGoSearchPage,
    result_page : DuckDuckGoResultPage
    ) -> None:

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for a phrase
    search_page.search(phrase)

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase)

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase)

    # And the search result title contains the phrase
    expect(page).to_have_title(f"{phrase} at DuckDuckGo")
