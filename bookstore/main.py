import os

from flask import Flask, render_template, flash

from forms import AddBookForm
from books import add_book, lookup_isbn

app = Flask(__name__)

app.config['SECRET_KEY'] = (os.environ.get('GAE_APPLICATION', 'super') +
                            os.environ.get('GAE_DEPLOYMENT_ID', 'secret'))


@app.route('/books/add', methods=['GET', 'POST'])
def submit_add():
    form = AddBookForm()
    if form.validate_on_submit():
        add_book(lookup_isbn(form.isbn.data))

        flash('ISBN saved {}'.format(form.isbn.data))
        form.isbn.data = None

    return render_template('add.html', form=form), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
