from model.project import Project
import uuid


def test_del_project(app):

    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.open_manage_project()
    if len(app.project.get_project_list()) == 0:
        app.project.open_create_new_project()
        app.project.fill_form_project(Project(name_project=str(uuid.uuid4().hex), status="stable",
                                              description="TESTdescription", view_status="private"))
        app.project.confirm_add_project()
    old_list_project = app.project.get_project_list()
    app.project.del_project()
    app.project.open_manage_project()
    new_list_project = app.project.get_project_list()
    assert len(old_list_project) - 1 == len(new_list_project)
    old_list_project[0:1] = []
    assert old_list_project == new_list_project
