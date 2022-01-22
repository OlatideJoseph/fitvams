from flask import Blueprint
follower=Blueprint('followers',__name__,
template_folder='templates',
static_folder='static'
)