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
        ('fortsmith', 'Fort Smith, Arkansas'),
        ('jonesboro', 'Jonesboro, Arkansas'),
        ('littlerock', 'Little Rock, Arkansas'),
        ('texarkana', 'Texarkana, Arkansas'),
        
        # California
        ('bakersfield', 'Bakersfield, California'),
        ('chico', 'Chico, California'),
        ('fresno', 'Fresno, California'),
        ('goldcountry', 'Gold Country, California'),
        ('hanford-corcoran', 'Hanford-Corcoran, California'),
        ('humboldt', 'Humboldt County, California'),
        ('imperial', 'Imperial County, California'),
        ('inlandempire', 'Inland Empire, California'),
        ('losangeles', 'Los Angeles, California'),
        ('mendocino', 'Mendocino County, California'),
        ('merced', 'Merced, California'),
        ('modesto', 'Modesto, California'),
        ('monteray', 'Monteraybay, California'),
        ('orangecounty', 'Orange County, California'),
        ('palmsprings', 'Palm Springs, California'),
        ('redding', 'Redding, California'),
        ('sacramento', 'Sacramento, California'),
        ('sandiego', 'San Diego, California'),
        ('sfbay', 'San Francisco Bay Area, California'),
        ('slo', 'San Luis Obispo, California'),
        ('santabarbara', 'Santa Barbara, California'),
        ('santamaria', 'Santa Maria, California'),
        ('siskiyou', 'Siskiyou County, California'),
        ('stockton', 'Stockton, California'),
        ('susanville', 'Susanville, California'),
        ('ventura', 'Ventura County, California'),
        ('visalia', 'Visalia-Tulare, California'),
        ('yubasutter', 'Yuba-Sutter, California'),
        
        # Colorado
        ('boulder', 'Boulder, Colorado'),
        ('cosprings', 'Colorado Springs, Colorado'),
        ('denver', 'Denver, Colorado'),
        ('eastco', 'easternco, Colorado'),
        ('fortcollins', 'Fort Collins / North CO, Colorado'),
        ('rockies', 'highrockies, Colorado'),
        ('pueblo', 'pueblo, Colorado'),
        ('westslope', 'westernslope, Colorado'),
        
        
        
        ])
    price = IntegerField()
    submit = SubmitField('Search')
    
    
    
