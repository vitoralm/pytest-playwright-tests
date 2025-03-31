import pytest
from playwright.sync_api import sync_playwright
import os
import allure

@pytest.fixture(scope="session")
def local_debug(request):
    """Adding 'local_debug' parameter."""
    return request.config.getoption("--local_debug")


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run browser in headed mode", default=False)
    parser.addoption("--local_debug", action="store_true", help="Local debug session", default=False)
    parser.addoption("--browser", action="store", default="chromium", help="Browser to use: chromium, firefox, webkit")


@pytest.fixture(scope="function")
def page(request):
    headed = request.config.getoption("--headed")
    browser_name = request.config.getoption("--browser")

    with sync_playwright() as p:
        match browser_name:
            case "chromium":
                browser = p.chromium.launch(headless=not headed)
            case "firefox":
                browser = p.firefox.launch(headless=not headed)
            case "webkit":
                browser = p.webkit.launch(headless=not headed)

        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com")
        yield page
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    raw_stack_trace = rep.longreprtext
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode):
                if "page" in item.fixturenames:
                    page = item.funcargs["page"]
                else:
                    print("Can't take screenshot", call)
                    return
            allure.attach(
                page.screenshot(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print(f"Can't take screenshot: {e}")
        if raw_stack_trace and item.config.getoption("--local_debug"):
            print("-------------------------------- local_debug --------------------------------")
            input(raw_stack_trace)
