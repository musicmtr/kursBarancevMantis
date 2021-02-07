from model.project import Project
import uuid


def test_del_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.project.open_manage_project()
    if len(app.project.get_project_list()) == 0:
        app.project.open_create_new_project()
        app.project.fill_form_project(Project(name_project=str(uuid.uuid4().hex), status="stable",
                                              description="TESTdescription", view_status="private"))
        app.project.confirm_add_project()
    old_list_project = app.soap.get_project_list(username, password)
    app.project.del_project()
    app.project.open_manage_project()
    new_list_project = app.soap.get_project_list(username, password)
    assert len(old_list_project) - 1 == len(new_list_project)
    old_list_project[0:1] = []
    assert old_list_project == new_list_project
    assert sorted(old_list_project, key=Project.id_or_max) == sorted(new_list_project, key=Project.id_or_max)
