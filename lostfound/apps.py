from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class ReportForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Report')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        # Here you would typically save the data to a database
        flash('Your report has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('report.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
