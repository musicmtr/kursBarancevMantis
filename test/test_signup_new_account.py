

def test_signup_new_account(app):
    username = "user1"
    password = "test"
    app.james.ensure_users_exists(username, password)