from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
class ContactForm(FlaskForm):
	name = StringField("Name: ", validators=[DataRequired(message="This field must be completed.")])
	email = StringField("Email: ", 
		validators=[Length(min=6, message=("A little bit too short to be an email address...")),
					Length(max=40, message=("Email address looks a little too long to be accepted...")),
					Email(message=("Not a valid email address."))])
	subject = StringField("Subject: ", validators=[DataRequired(message="This field must be completed.")])
	message = TextAreaField("Message", validators=[DataRequired(message="This field must be completed.")])
	submit = SubmitField("Submit")

	# <form method="POST" id="contact-form" name="contact-form" class="contact-form">
	# 								<div class="form-group col-md-12">
	# 									{{ form.name.label }}: {{ form.name(id="name", class="form-control", name="name", placeholder="Name") }}
	# 								</div>
	# 								<div>
	# 									{{ form.email.label }}: {{ form.email(id="email", class="form-control", name="email", placeholder="Email") }}
	# 								</div>
	# 								<div>
	# 									{{ form.subject.label }}: {{ form.subject(id="subject", class="form-control", name="subject", placeholder="Subject") }}
	# 								</div>
	# 								<div>
	# 									{{ form.message.label }}: {{ form.message(id="message", class="form-control", name="message", placeholder="Message") }}
	# 								</div>
	# 								<div>
	# 									{{ form.submit.label }}
	# 								</div>
	# 							</form>