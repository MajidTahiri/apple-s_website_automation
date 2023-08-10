import time

from behave import when, then


@when("the user hover over the iPhone link")
def hover_over_iphone_link(context):
    context.app.header.hover_over_iphone_link()
    time.sleep(10)


# @when("clicks the iPhone 14 Pro link from the drop down menu")
# def click_iphone_14_pro(context):
#     context.app.home_page.click_iphone_14_pro()
#
#
# @then("the user clicks on the Apple logo to go back to the homepage")
# def click_apple_logo(context):
#     context.app.header.click_apple_logo()
