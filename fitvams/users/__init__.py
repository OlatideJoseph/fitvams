from flask import Blueprint
user=Blueprint('users',__name__,
template_folder='templates',
static_folder='static'
)