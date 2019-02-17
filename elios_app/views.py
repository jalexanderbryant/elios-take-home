from elios_app import app

@app.route('/')
@app.route('/home/')
def home():
    return "Hello, world!"

@app.route('/users/')
def list_users():
  """ List all users - Will return a table"""
  return "All Users"

@app.route('/users/<int:user_id>/')
def list_single_user(user_id):
  """ Return a user profile """
  return "User profile for USER=%s" % user_id

@app.route('/users/<int:user_id>/edit')
def edit_user_name(user_id):
  """Edit a single user's name """
  return "Edit user's fullname for USER=%s" % user_id