from flask import Blueprint,render_template

blog_bp=Blueprint('blog',__name__)

@blog_bp.route('/index',methods=['GET','POST'])
def index():
    return render_template('index.html')









