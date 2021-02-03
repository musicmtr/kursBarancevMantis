from model.project import Project

def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.open_create_new_project()
    app.project.fill_form_project(Project(name_project="TESTname"))
    app.project.fill_form_project(Project(description="TESTdescription"))