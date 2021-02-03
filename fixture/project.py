import time
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
        self.change_field_value(field_name='description', text=project.description)
        time.sleep(5)


    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            # wd.find_element_by_css_selector(field_name).click()


