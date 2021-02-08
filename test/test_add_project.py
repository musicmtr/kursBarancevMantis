from model.project import Project
import uuid


def test_add_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    #app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    old_project = app.soap.get_project_list(username, password)
    app.project.open_create_new_project()
    project = Project(name_project=str(uuid.uuid4().hex))
    app.project.fill_name_project(project)
    app.project.confirm_add_project()
    new_list_project = app.soap.get_project_list(username, password)
    assert len(old_project) + 1 == len(new_list_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_list_project, key=Project.id_or_max)

