This project is meant to showcase the Pytest framework with Playwright lib to run E2E tests in a real QA daily-work scenario with a effective Allure Report.

This project use Allure Report, so in order to view results you should install `allure` CLI, please view `https://allurereport.org/docs/install-for-macos/`

Install poetry using `pipx install poetry`

View official docs for more details
- https://pipx.pypa.io/stable/installation/
- https://python-poetry.org/docs/#installing-with-pipx

Create python venv manually `python3 -m venv venv`

Run `source venv/bin/activate` to activate the virtual environment

Run `poetry run playwright install` to install playwright content

Run `poetry install` to get all Python dependencies

FYI tested app is https://www.saucedemo.com/

- Run login tests with `poetry run task test login`
- Run login tests with headed mode `poetry run task test_headed login`
- Run login tests with local_debug `poetry run task test_local login` (it will also disable headless tests)
- Run lint to format project files `poetry run task lint`
- Show Allure Report by running `allure serve ./results`

NOTE: tests can run with chromium (default), webkit and firefox

Running tests using a Docker container

- `docker build . -f Dockerfile -t vitoralm/pytest-playwright-tests:latest`
- `docker run --rm -e BROWSER="webkit" -e TEST="all" -e QASE_API_TOKEN=${QASE_API_TOKEN} -v $(pwd)/results:/app/results vitoralm/pytest-playwright-tests:latest`
- `docker push vitoralm/pytest-playwright-tests:latest`
- https://hub.docker.com/repository/docker/vitoralm/pytest-playwright-tests/tags

This project uses pre-commit hooks

`pre-commit install` to enable to hooks from the yaml local file. It will trigger black and flake8
