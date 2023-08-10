import time

from behave import when, then


@when("the user clicks the search icon")
def click_search_icon(context):
    context.app.header.click_search_icon()


@when("enters '{search_query}' in the search bar")
def search_for_product(context, search_query):
    context.app.home_page.search_for_product(search_query)
    time.sleep(5)


@then("the user is redirected to search results page")
def verify_correct_page_opened(context):
    expected_url = 'https://www.apple.com/us/search/iPhone-14?src=globalnav'
    context.app.search_results_page.verify_correct_page_opened(expected_url)
    time.sleep(10)


@then("the search results contain 'iPhone 14'")
def verify_iphone_14_found(context):
    expected_text = 'iPhone 14 and iPhone 14 Plus'
    context.app.search_results_page.verify_iphone_14_found(expected_text)










