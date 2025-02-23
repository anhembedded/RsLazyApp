from lazyApp import lazyAppUI_T
from utility.log import Logger_T, logging

if __name__ == "__main__":
    log = Logger_T()
    log.log(message="____Starting [lazyAppUI_T]____", level=logging.INFO)
    lazyApp = lazyAppUI_T()
    lazyApp.run()