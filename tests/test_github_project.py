import time
from playwright.sync_api import APIRequestContext, Page, expect

def test_create_project_card(
    gh_context: APIRequestContext,
    project_column_ids: list[str]) -> None:

    # Prep test data
    now = time.time()
    note = f'A new task at {now}'

    # Create a new card
    c_response = gh_context.post(
        f'/projects/columns/{project_column_ids[0]}/cards',
        data={'note': note})
    expect(c_response).to_be_ok()
    assert c_response.json()['note'] == note

    # Retrieve the newly created card
    card_id = c_response.json()['id']
    r_response = gh_context.get(f'/projects/columns/cards/{card_id}')
    expect(r_response).to_be_ok()
    assert r_response.json() == c_response.json()