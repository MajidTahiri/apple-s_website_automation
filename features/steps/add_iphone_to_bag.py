import time

from behave import given, when, then


@given("the user is on Apple's homepage")
def open_apple_website(context):
    context.app.base_page.open_url('https://www.apple.com/')


@when("the user clicks the 'iPhone' link")
def click_iphone_link(context):
    context.app.header.click_iphone_link()


@when("clicks the 'Shop iPhone' link")
def click_shop_iphone_link(context):
    context.app.iPhone_page.click_shop_iphone_link()


@when("select an iPhone model")
def select_iphone_model(context):
    context.app.buy_iPhone_page.select_iphone_model()


@when("the user selects iphone 14")
def select_iphone_14(context):
    context.app.buy_iPhone_page.select_iphone_14()


@when("select iphone color")
def select_iphone_color(context):
    context.app.buy_iPhone_page.select_iphone_color()


@when("select iphone storage")
def select_iphone_storage(context):
    context.app.buy_iPhone_page.select_iphone_storage()


@when("select 'No trade-in'")
def select_no_trade_in(context):
    context.app.buy_iPhone_page.select_no_trade_in()


@when("select payment option")
def select_payment_option(context):
    context.app.buy_iPhone_page.select_payment_option()


@when("choose a carrier")
def choose_carrier(context):
    context.app.buy_iPhone_page.choose_carrier()


@when("choose a coverage")
def choose_coverage(context):
    context.app.buy_iPhone_page.choose_coverage()


@when("add iPhone to cart")
def add_to_cart(context):
    context.app.buy_iPhone_page.add_to_cart()


@then("review bag")
def review_bag(context):
    context.app.buy_iPhone_page.review_bag()
