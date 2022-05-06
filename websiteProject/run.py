from app import myapp_obj, createDatabase, login, User
createDatabase(myapp_obj)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

myapp_obj.run()
