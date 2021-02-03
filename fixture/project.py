import time
from selenium.webdriver.support.select import Select
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_create_new_project(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()

    def fill_form_project(self, project):
        wd = self.app.wd
        self.change_field_value(field_name='name', text=project.name_project)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        time.sleep(5)
        wd.find_element_by_css_selector("input[name='inherit_global']").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_status)
        self.change_field_value(field_name='description', text=project.description)
        time.sleep(5)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            # wd.find_element_by_css_selector(field_name).click()

    def confirm_add_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Add Project']").click()





