from model.project import Project
import uuid


def test_add_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    old_list_project = app.project.get_project_list()
    app.project.open_create_new_project()
    project = Project(name_project=str(uuid.uuid4().hex), status="stable",
                                          description="TESTdescription", view_status="private")
    app.project.fill_form_project(project)
    app.project.confirm_add_project()
    new_list_project = app.project.get_project_list()
    assert len(old_list_project) + 1 == len(new_list_project)
    old_list_project.append(project)
    assert sorted(old_list_project, key=Project.id_or_max) == sorted(new_list_project, key=Project.id_or_max)
