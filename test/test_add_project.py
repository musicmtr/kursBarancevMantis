from model.project import Project
import uuid


def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.open_create_new_project()
    app.project.fill_form_project(Project(name_project=str(uuid.uuid4().hex), status="stable",
                                          description="TESTdescription", view_status="private"))
    app.project.confirm_add_project()