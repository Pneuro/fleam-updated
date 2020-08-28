from wtforms import Form, StringField, IntegerField, SelectField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(Form):
    id = ''
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[Length(min=6, max=20),DataRequired()])
    submit = SubmitField('Login')
    

class RegistrationForm(Form):
    id = ''
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[Length(min=6, max=20),DataRequired()])
    password2 = StringField('Confirm Password', validators=[EqualTo(password),DataRequired()])
    submit = SubmitField('Login')
    
    
    
class SearchForm(Form):
    query = StringField('Search')
    city = SelectField('City', choices=[
        # Alabama
        ('auburn', 'Auburn, Alabama'), 
        ('bham', 'Birmingham, Alabama'),
        ('dothan', 'Dothan, Alabama'),
        ('shoals', 'Florence / Shoals, Alabama'),
        ('gadsden', 'Gadsden-Anniston, Alabama'),
        ('huntsville', 'Hunstville / Decatur, Alabama'),
        ('mobile', 'Mobile, Alabama'),
        ('montgomery', 'Montgomery, Alabama'),
        ('tuscaloosa', 'Tuscaloosa, Alabama'),
        
        # Alaska
        ('anchorage', 'Anchorage, Alaska'),
        ('fairbanks', 'Anchorage, Alaska'),
        ('kenai', 'Kenai Peninsula, Alaska'),
        ('juneau', 'Southeast Alaska, Alaska'),
        
        # Arizona
        ('flagstaff', 'Flagstaff / Sedona, Arizona'),
        ('mohave', 'mohave, Arizona'),
        ('phoenix', 'Phoenix, Arizona'),
        ('prescott', 'Prescott, Arizona'),
        ('showlow', 'Show Low, Arizona'),
        ('sierravista', 'Sierra Vista, Arizona'),
        ('tucson', 'Tucson, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        
        # Arkansas
        ('fayar', 'Fayetteville, Arkansas'),
        ('fortsmith', 'Fayetteville, Arkansas'),
        ('jonesboro', 'Fayetteville, Arkansas'),
        ('littlerock', 'Fayetteville, Arkansas'),
        ('texarkana', 'Fayetteville, Arkansas'),
        
        # California
        ('bakersfield', 'Bakersfield, Arizona'),
        ('chico', 'chico, Arizona'),
        ('fresno', 'fresno, Arizona'),
        ('goldcountry', 'Yuma, Arizona'),
        ('hanford-corcoran', 'Yuma, Arizona'),
        ('humboldtcounty', 'Yuma, Arizona'),
        ('imperialcounty', 'Yuma, Arizona'),
        ('inlandempire', 'Yuma, Arizona'),
        ('losangeles', 'Yuma, Arizona'),
        ('mendocinocounty', 'Yuma, Arizona'),
        ('merced', 'Yuma, Arizona'),
        ('modesto', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ('yuma', 'Yuma, Arizona'),
        ])
    price = IntegerField()
    submit = SubmitField('Search')
    
    
    
