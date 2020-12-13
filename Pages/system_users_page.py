from selenium.webdriver.common.by import By

from Pages.add_user_page import AddUserPage
from Pages.menu_bar import MenuBar


class SystemUsersPage(MenuBar):

    __search_user_name_tbox = By.ID, "searchSystemUser_userName"
    __search_user_role_dd = By.ID, "searchSystemUser_userType"
    __search_emp_name_cbox = By.ID, "searchSystemUser_employeeName_empName"
    __search_status_dd = By.ID, "searchSystemUser_status"

    __search_btn = By.ID, "searchBtn"
    __reset_btn = By.ID, "resetBtn"

    __add_btn = By.ID, "btnAdd"
    __delete_btn = By.ID, "btnDelete"


    def click_add(self):
        self._click_element(self.__add_btn)
        return AddUserPage(self.driver)


