from curses import window
from selenium import webdriver

class Browser(object):
    #inicia o Firefox
    driver = webdriver.Firefox()
    #Tempo máximo para carregar a página
    driver.set_page_load_timeout(30)
    #Maximiza a ganela ao ser iniciada
    driver.maximize_window()

    #fecha o browser
    def browser_quit(self):
        self.driver.quit()

    #limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorege.clear()')
        self.driver.refresh()
        