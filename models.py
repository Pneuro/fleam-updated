from wtforms import Form, StringField, IntegerField, SelectField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(Form):
    id = ''
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[
                           Length(min=6, max=20), DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(Form):
    id = ''
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[
                           Length(min=6, max=20), DataRequired()])
    password2 = StringField('Confirm Password', validators=[
                            EqualTo(password), DataRequired()])
    submit = SubmitField('Login')


class SearchForm(Form):
    query = StringField('Search', validators=[
                        DataRequired()], default='Lawnmower')
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
        ('hanford', 'Hanford-Corcoran, California'),
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

        # Connecticut
        ('newlondon', 'Eastern Connecticut'),
        ('hartford', 'Hartford, Connecticut'),
        ('newhaven', 'New Haven, Connecticut'),
        ('nwct', 'Northwest Connecticut'),

        # Delaware
        ('delaware', 'Delaware'),

        # District of Columbia
        ('washingtondc', 'Washington DC')

        # Florida
        ('miami', 'Broward County, Florida'),
        ('daytona', 'Daytona Beach, Florida'),
        ('keys', 'Florida Keys, Florida'),
        ('miami', 'Fort Lauderdale, Florida'),
        ('fortmyers', 'ft myers / SW florida, Florida'),
        ('gainesville', 'Gainesville, Florida'),
        ('cfl', 'Heartland, Florida'),
        ('jacksonville', 'Jacksonville, Florida'),
        ('lakeland', 'Lakeland, Florida'),
        ('miami', 'Miami / Dade, Florida'),
        ('lakecity', 'North Central, Florida'),
        ('ocala', 'Ocala, Florida'),
        ('okaloosa', 'Okaloosa / Walton, Florida'),
        ('orlando', 'Orlando, Florida'),
        ('panamacity', 'Panama City, Florida'),
        ('pensacola', 'Pensacola, Florida'),
        ('sarasota', 'Sarasota-Bradenton, Florida'),
        ('miami', 'South Florida, Florida'),
        ('spacecoast', 'Space Coast, Florida'),
        ('staugustine', 'St Augustine, Florida'),
        ('tallahassee', 'Tallahassee, Florida'),
        ('tampa', 'Tampa Bay Area, Florida'),
        ('treasure', 'Treasure Coast, Florida'),
        ('miami', 'Palm Beach County, Florida'),

        # Georgia
        ('albanyga', 'Albany, Georgia'),
        ('athensga', 'Athens, Georgia'),
        ('atlanta', 'Atlanta, Georgia'),
        ('augusta', 'Augusta, Georgia'),
        ('brunswick', 'Brunswick, Georgia'),
        ('columbusga', 'Columbus, Georgia'),
        ('macon', 'Macon / Warner Robins, Georgia'),
        ('nwga', 'Northwest, Georgia'),
        ('savannah', 'Savannah / Hinesville, Georgia'),
        ('statesboro', 'Statesboro, Georgia'),
        ('valdosta', 'Valdosta, Georgia'),

        # Hawaii
        ('honolulu', 'Hawaii'),

        # Idaho
        ('boise', 'Boise, Idaho'),
        ('eastidaho', 'East Idaho'),
        ('lewiston', 'Lewiston / Clarkston, Idaho'),
        ('twinfalls', 'Twin Falls, Idaho'),

        # Illinois
        ('bn', 'Bloomington-Normal'),
        ('champana', 'Champaign Urbana, Illinois'),
        ('chicago', 'Chicago, Illinois'),
        ('decatur', 'Decatur, Illinois'),
        ('lasalle', 'La Salle Co, Illinois'),
        ('mattoon', 'Mattoon-Charleston, Illinois'),
        ('peoria', 'Peoria, Illinois'),
        ('ci', 'Rockford, Illinois'),
        ('ci', 'Southern Illinois'),
        ('ci', 'Springfield, Illinois'),
        ('ci', 'Wester Illinois'),

        # Indiana
        # Iowa
        # Kansas
        # Kentucy
        # Louisiana
        # Maine
        # Maryland
        # Massachusetts
        # Michigan
        # Minnesota
        # Mississippi
        # Missouri
        # Montana
        # Nebraska
        # Nevada
        # New Hampshire
        # New Jersey
        # New Mexico
        # New  York
        # North Carolina
        # North Dakota

        # Ohio
        ('cleveland', 'Cleveland, Ohio'),


    ])
    price = IntegerField(default=500)
    submit = SubmitField('Search')
