from flask import Blueprint,render_template

admin_bp=Blueprint('admin',__name__)

@admin_bp.route('/setting',methods=['GET','POST'])
def setting():
    return render_template('admin/setting.html')







