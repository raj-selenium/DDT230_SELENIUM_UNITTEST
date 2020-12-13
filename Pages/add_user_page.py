from selenium.webdriver.common.by import By

from Pages.menu_bar import MenuBar

class AddUserPage(MenuBar):

    url = MenuBar.url+""

    __user_role_dd = By.ID, "systemUser_userType"
    __employeeName_cbox = By.ID, "systemUser_employeeName_empName"
    __username_tbox = By.ID, "systemUser_userName"
    __status_dd = By.ID, "systemUser_status"
    __password_tbox = By.ID, "systemUser_password"
    __confirm_password_tbox = By.ID, "systemUser_confirmPassword"

    __save_btn = By.ID, "btnSave"
    __cancel_btn = By.ID, "btnCancel"

    __validation_txt = By.CSS_SELECTOR, "[class=validation-error]"

    def select_role(self, role):
        self._select_by_text(self.__user_role_dd, role)

    def select_status(self, status):
        self._select_by_text(self.__status_dd, status)

    def enter_employee_name(self, name):
        if name == "":
            return self.get_validation_msg(self.__employeeName_cbox)
        self._input_text(self.__employeeName_cbox, name)

    def enter_username(self, name):
        if name == "":
            return self.get_validation_msg(self.__username_tbox)
        self._input_text(self.__username_tbox, name)

    def enter_password(self, password):
        if len(password) < 8:
            return self.get_validation_msg(self.__password_tbox)
        self._input_text(self.__password_tbox, password)

    def enter_confirm_password(self, password, confirm_password):
        if password != confirm_password:
            return self.get_validation_msg(self.__confirm_password_tbox)
        self._input_text(self.__confirm_password_tbox, confirm_password)

    def click_save(self):
        self._click_element(self.__save_btn)

    def click_cancel(self):
        self._click_element(self.__cancel_btn)

    def get_validation_msg(self, locator):
        dynamic_loc = f"{self.__validation_txt[1]}+[for='{locator[1]}']"
        self._get_text((self.__validation_txt[0], dynamic_loc))