from flask import Blueprint
post=Blueprint('posts',__name__,
template_folder='templates',
static_folder='static'
)