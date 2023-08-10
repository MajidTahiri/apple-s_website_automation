import time

from behave import when, then


@when("the user clicks on the Store link in the navigation")
def click_store_link(context):
    context.app.header.click_store_link()


@when("clicks find a store")
def click_find_store(context):
    current_window = context.app.stores_page.click_find_store()
    context.current_window = current_window


@then("the user is redirected to the Apple Store locator page")
def verify_store_locator_page_open(context):
    expected_url = 'https://www.apple.com/retail/'
    context.app.stores_page.verify_store_locator_page_open(expected_url, context.current_window)


@then("the user can search for stores by location")
def find_store_by_location(context):
    context.original_window = context.driver.current_window_handle
    search_query = "Berkeley"
    context.app.retail_page.find_store_by_location(search_query)


@then("the user can switch back to the original window")
def switch_to_original_window(context):
    # Get the original window handle that you stored earlier
    original_window = context.original_window

    # Switch back to the original window
    context.driver.switch_to.window(original_window)






