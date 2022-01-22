from flask import Blueprint
message=Blueprint('messages',__name__,
template_folder='templates',
static_folder='static'
)