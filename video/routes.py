from flask import render_template, url_for, flash, redirect, request
from video import app, db
from video.forms import Register
from video.models import Videos
import secrets
import os
from PIL import Image
from flask import send_file
from werkzeug.utils import secure_filename


@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def home():
    videos = os.listdir(os.path.join(os.getcwd(), 'video', 'static', 'videos'))
    print('all-', videos)
    likes = []
    downloads = []
    for video_name in videos:
        get_feedbacks1 = Videos.query.filter_by(video_name=video_name).first()
        likes.append(get_feedbacks1.video_likes)
        downloads.append(get_feedbacks1.video_do)
        print('do', downloads)
    out = []
    for video, like, download in zip(videos, likes, downloads):
        out.append([video, like, download])

    return render_template('user_operation.html', title='videos', out=out)


@app.route('/download/<video_name>', methods=['GET', 'POST'])
def download(video_name):
    print(video_name)
    get_feedbacks1 = Videos.query.filter_by(video_name=video_name).first()
    print("Print Feedbacks", type(get_feedbacks1), get_feedbacks1)
    get_feedbacks1.video_do += 1
    db.session.commit()
    get_feedbacks1 = Videos.query.filter_by(video_name=video_name).first()
    print("Print Feedbacks1", type(get_feedbacks1), get_feedbacks1)
    return send_file('static/videos/'+video_name, as_attachment=True)

@app.route('/likes/<video_name>', methods=['GET', 'POST'])
def likes(video_name):
    print(video_name)
    get_feedbacks1 = Videos.query.filter_by(video_name=video_name).first()
    print("Print Feedbacks", type(get_feedbacks1), get_feedbacks1)
    get_feedbacks1.video_likes += 1
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = Register()
    
    if form.validate_on_submit():
        print(dir(form.video_file.data))
        print(form.video_file.name, form.video_file.data, form.video_file.data.filename, form.video_file.data.name )
        filename = secure_filename(form.video_file.data.filename)
        form.video_file.data.save(os.path.join(os.getcwd(), 'video', 'static', 'videos', filename))
        video = Videos(video_name=filename, video_do=0, video_likes=0)
        db.session.add(video)
        db.session.commit()
        print(video)
        flash('Your video is saved', 'success')

        return redirect(url_for('admin'))

    return render_template('admin.html', title='Register', form=form)

@app.route('/test', methods=['POST'])
def test():    
    print('testt')
    rf=request.form
    print(rf)
    for key in rf.keys():
        data=key
    print(data, type(data))
    data = eval(data)
    print(type(data), data['video'], data['count'])

    get_feedbacks1 = Videos.query.filter_by(video_name=data['video']).first()
    print("Print Feedbacks", type(get_feedbacks1), get_feedbacks1)
    get_feedbacks1.video_do = data['count']
    db.session.commit()
    return redirect(url_for('home'))
