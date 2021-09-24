from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,CommentForm,UpdateProfile,PostForm
from ..models import User,Blog,Comment
from .. import db,photos
from datetime import datetime
from ..requests import get_quote





@main.route('/')
def index():
    quote = get_quote()
    tittle='blog-app'
    return render_template("index.html", quote=quote, tittle=tittle)
  
  
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)    



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form) 


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))       

@main.route('/blogs')
@login_required
def blogs():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15)

    return render_template('blogs.html', all_blogs=all_blogs)

@main.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).first()

    return render_template('post.html', post=post)



@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteBlog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.blogs'))   

@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def updateBlog(id):
    blog = Blog.query.get_or_404(id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('main.blogs'))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('updateBlog.html', form=form)    


@main.route('/post')
def add():
    return render_template('post.html')

@main.route('/addblog', methods=['GET','POST'])
@login_required
def addpost():

    form =  PostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_blog = Blog(title=title,
                        content=content, user=current_user)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', form=form)




@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    
    blog = Blog.query.filter_by(id=id).first()
    blogComments = Comment.query.filter_by(blog_id=id).all()
    if form.validate_on_submit():
        content = form.comment.data

        new_comment = Comment(
            blog_id=blog.id, content=content, user=current_user)

        new_comment.save()
        print(new_comment)
        # return redirect(url_for('main.index'))

    return render_template('new_comment.html', comment_form=form,blog_comment=blogComments)

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect (url_for('main.blogs'))    