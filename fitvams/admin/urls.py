from fitvams.admin import admin
@admin.route('/')
def index():
    return 'admin access'