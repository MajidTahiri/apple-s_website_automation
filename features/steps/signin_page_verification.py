from behave import when, then


@when("the user clicks on the shopping bag")
def open_shopping_cart(context):
    context.app.header.open_shopping_cart()


@when("the user clicks on the Sign in link")
def click_signin_link(context):
    context.app.home_page.click_signin_link()


@then("the user is on the signin page")
def verify_signin_page_is_opened(context):
    page_title = 'Sign in for faster checkout.'
    context.app.signin_page.verify_signin_page_is_opened(page_title)




