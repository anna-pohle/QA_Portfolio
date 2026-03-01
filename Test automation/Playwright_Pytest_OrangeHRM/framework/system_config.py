"""
System configuration for the OrangeHRM test environment.

Centralized configuration for URLs, timeouts, and browser settings.
"""

# Base URL of the application
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php"

# Timeouts (in milliseconds)
# SHORT_TIMEOUT:    For quick visibility checks (e.g. tooltip, datepicker closing)
# DEFAULT_TIMEOUT:  Standard for element interactions and page default timeout
# EXTENDED_TIMEOUT: For longer operations (page navigation, dialog waits)
SHORT_TIMEOUT = 5000       # 5 seconds
DEFAULT_TIMEOUT = 10000    # 10 seconds
EXTENDED_TIMEOUT = 30000   # 30 seconds

# Browser configuration
BROWSER_CONFIG = {
    "headless": False,
    "slow_mo": 500,  # 0.5 seconds in milliseconds
    "timeout": DEFAULT_TIMEOUT,
    "args": ["--start-maximized"],
}
