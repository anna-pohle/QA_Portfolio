BASE_URL = "https://grocerymate.masterschool.com/"

DEFAULT_TIMEOUT = 5000  # 5 Sekunden in Millisekunden
EXTENDED_TIMEOUT = 10000  # 10 Sekunden in Millisekunden


BROWSER_CONFIG = {
    "headless": False,
    "slow_mo": 500, # 0,5 Sekunden in Millisekunden
    "timeout": DEFAULT_TIMEOUT,
    "args": ["--start-maximized"]
}
