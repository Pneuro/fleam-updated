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
        ('washingtondc', 'Washington DC'),

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
        ('rockford', 'Rockford, Illinois'),
        ('carbondale', 'Southern Illinois'),
        ('springfieldil', 'Springfield, Illinois'),
        ('quincy', 'Wester Illinois'),

        # Indiana
        ('bloomington', 'Bloomington, Indiana'),
        ('evansville', 'Evansville, Indiana'),
        ('fortwayne', 'Fort Wayne, Indiana'),
        ('indianapolis', 'Indianapolis, Indiana'),
        ('kokomo', 'Kokomo, Indiana'),
        ('tippecanoe', 'Lafayette / West Lafayette, Indiana'),
        ('muncie', 'Muncie / Anderson, Indiana'),
        ('richmondin', 'Richmond, Indiana'),
        ('southbend', 'South Bend / Michiana, Indiana'),
        ('terrehaute', 'Terre Haute, Indiana'),


        # Iowa
        ('ames', 'Ames, Iowa'),
        ('cedarrappids', 'Cedar Rapids, Iowa'),
        ('desmoines', 'Des Moines, Iowa'),
        ('dubuque', 'Dubuque, Iowa'),
        ('fortdodge', 'Fort Dodge, Iowa'),
        ('iowacity', 'Iowa City, Iowa'),
        ('masoncity', 'Mason City, Iowa'),
        ('quadcities', 'Quad Cities, Iowa/Illinois'),
        ('siouxcity', 'Sioux City, Iowa'),
        ('ottumwa', 'Southeast Iowa'),
        ('waterloo', 'Waterloo / Cedar Falls, Iowa'),


        # Kansas
        ('lawrence', 'Lawrence, Kansas'),
        ('ksu', 'Manhatten, Kansas'),
        ('nwks', 'Northwest Kansas'),
        ('salina', 'Salina, Kansas'),
        ('seks', 'Southeast Kansas'),
        ('swks', 'Southwest Kansas'),
        ('topeka', 'Topeka, Kansas'),
        ('wichita', 'Wichita, Kansas'),

        # Kentucy
        ('bgky', 'Bowling Green, Kentucky'),
        ('eastky', 'Eastern Kentucky'),
        ('lexington', 'Lexington, Kentucky'),
        ('louisville', 'Louisville, Kentucky'),
        ('owensboro', 'Owensboro, Kentucky'),
        ('westky', 'Western Kentucky'),

        # Louisiana
        ('batonrouge', 'Baton Rouge, Louisiana'),
        ('cenla', 'Central Louisiana'),
        ('houma', 'Houma, Louisiana'),
        ('lafayette', 'Lake Charles, Louisiana'),
        ('lakecharles', 'Monroe, Louisiana'),
        ('monroe', 'Monroe, Louisiana'),
        ('neworleans', 'New Orleans, Louisiana'),
        ('shreveport', 'Shreveport, Louisiana'),


        # Maine
        ('maine', 'Maine'),
        # Maryland
        ('annapolis', 'Annapolis, Maryland'),
        ('baltimore', 'Baltimore, Maryland'),
        ('easternshore', 'Eastern Shore, Maryland'),
        ('frederick', 'Frederick, Maryland'),
        ('smd', 'Southern Maryland'),
        ('westmd', 'Western Maryland'),


        # Massachusetts
        ('boston', 'Boston, Massachusettes'),
        ('capecod', 'Cape Cod / Islands, Massachusettes'),
        ('southcoast', 'South Coast, Massachusettes'),
        ('westernmass', 'Western Massachusettes'),
        ('worcester', 'Worcester, / Central Massachusettes'),
        # Michigan
        ('annarbor', 'Ann Arbor, Michigan'),
        ('battlecreek', 'Battle Creek, Michigan'),
        ('centralmich', 'Central Michigan'),
        ('detroit', 'Detroit Metro, Michigan'),
        ('flint', 'Flint, Michigan'),
        ('grandrapids', 'Grand Rapids, Michigan'),
        ('holland', 'Holland, Michigan'),
        ('jxn', 'Jackson, Michigan'),
        ('kalamazoo', 'Kalamazoo, Michigan'),
        ('lansing', 'Lansing, Michigan'),
        ('monroemi', 'Monroe, Michigan'),
        ('muskegon', 'Muskegon, Michigan'),
        ('nmi', 'Northern Michigan'),
        ('porthuron', 'Port Huron, Michigan'),
        ('saginaw', 'Sagina-Midland-BayCity, Michigan'),
        ('swmi', 'Southwest Michigan'),
        ('thumb', 'The Thumb, Michigan'),
        ('battlecreek', 'Upper Peninsula, Michigan'),


        # Minnesota
        ('bemidji', 'Bemidji, Minnesota'),
        ('brainerd', 'Brainerd, Minnesota'),
        ('duluth', 'Duluth / Superior, Minnesota'),
        ('mankato', 'Mankato, Minnesota'),
        ('minneapolis', 'Minneapolis / St Paul, Minnesota'),
        ('rmn', 'Rochester, Minnesota'),
        ('marshall', 'Southerwest Minnesota'),
        ('stcloud', 'St Cloud, Minnesota'),

        # Mississippi
        ('gulfport', 'Gulfport / Biloxi, Mississippi'),
        ('jackson', 'Jackson, Mississippi'),
        ('meridian', 'Meridian, Mississippi'),
        ('northmiss', 'North Mississippi'),
        ('natchez', 'Southwest Mississippi'),

        # Missouri
        ('columbiamo', 'Columbia / Jeff City, Missouri'),
        ('joplin', 'Joplin, Missouri'),
        ('kansascity', 'Kansas City, Missouri'),
        ('kirksville', 'Kirksville, Missouri'),
        ('loz', 'Lake of the Ozarks, Missouri'),
        ('semo', 'Southeast Missouri'),
        ('springfield', 'Springfield, Missouri'),
        ('stjoseph', 'St Joseph, Missouri'),
        ('stlouis', 'St Louis, Missouri'),

        # Montana
        ('billings', 'Billings, Montana'),
        ('bozeman', 'Bozeman, Montana'),
        ('butte', 'Butte, Montana'),
        ('greatfalls', 'Great Falls, Montana'),
        ('helena', 'Helena, Montana'),
        ('kalispell', 'Kalispell, Montana'),
        ('missoula', 'Missoula, Montana'),
        ('montana', 'Eastern Montana'),

        # Nebraska
        ('grandisland', 'Grand Island, Nebraska'),
        ('lincoln', 'Lincoln, Nebraska'),
        ('northplatte', 'North Platte, Nebraska'),
        ('omaha', 'Omaha / Council Bluffs, Nebraska'),
        ('scottsbluff', 'Scottsbluff / Panhandle, Nebraska'),

        # Nevada
        ('elko', 'Elko, Nevada'),
        ('lasvegas', 'Las Vegas, Nevada'),
        ('reno', 'Reno / Tahoe, Nevada'),

        # New Hampshire
        ('nh', 'New Hampshire'),
        # New Jersey
        ('cnj', 'Central New Jersey'),
        ('jerseyshore', 'Jersey Shore, New Jersey'),
        ('newjersey', 'North New Jersey'),
        ('southjersey', 'South New Jersey'),

        # New Mexico
        ('albuquerque', 'Albuquerque, New Mexico'),
        ('clovis', 'Clovis / Portales, New Mexico'),
        ('farmington', 'Farmington, New Mexico'),
        ('lascruces', 'Las Cruces, New Mexico'),
        ('roswell', 'Roswell / Carlsbad, New Mexico'),
        ('santafe', 'Santa Fe / Taos, New Mexico'),
        # New  York
        ('albany', 'Albany, New York'),
        ('bringhamton', 'Binghamton, New York'),
        ('buffalo', 'Buffalo, New York'),
        ('catskills', 'Catskills, New York'),
        ('chautauqua', 'Chautauqua, New York'),
        ('elmira', 'Elmira-Corning, New York'),
        ('fingerlakes', 'Finger Lakes, New York'),
        ('glenfalls', 'Glen Falls, New York'),
        ('hudsonvalley', 'Hudson Valley, New York'),
        ('ithica', 'Ithica, New York'),
        ('longisland', 'Long Island, New York'),
        ('newyork', 'New York City, New York'),
        ('oneonta', 'Oneonta, New York'),
        ('plattsburgh', 'Plattsburgh-Adirondacks, New York'),
        ('potsdam', 'Potsdam-Canton-Messena, New York'),
        ('rochester', 'Rochester, New York'),
        ('syracuse', 'Syracuse, New York'),
        ('twintiers', 'Twin Tiers, New York / Pennsylvania'),
        ('utica', 'Utica / Rome / Oneida, New York'),
        ('watertown', 'Watertown, New York'),
        # North Carolina
        ('asheville', 'Asheville, North Carolina'),
        ('boone', 'Boone, North Carolina'),
        ('charlotte', 'Charlotte, North Carolina'),
        ('eastnc', 'Eastern North Carolina'),
        ('fayetteville', 'Fayetteville, North Carolina'),
        ('greensboro', 'Greensboro, North Carolina'),
        ('hickory', 'Hickory / Lenoir, North Carolina'),
        ('onslow', 'Jacksonville, North Carolina'),
        ('outerbanks', 'Outer Banks North Carolina'),
        ('raleigh', 'Raleigh / Durham / CH, North Carolina'),
        ('wilmington', 'Wilmington, North Carolina'),
        ('winstonsalem', 'Winston / Salem, North Carolina'),
        # North Dakota
        ('bismarck', 'Bismarck, North Dakota'),
        ('fargo', 'Fargo / Moorhead, North Dakota'),
        ('grandforks', 'Grand Forks, North Dakota'),
        ('nd', 'North Dakota'),

        # Ohio
        ('akroncanton', 'Akron / Canton, Ohio'),
        ('ashtabula', 'Ashtabula, Ohio'),
        ('athensohio', 'Athens, Ohio'),
        ('cincinatti', 'Cincinatti, Ohio'),
        ('chillicothe', 'Chillicothe, Ohio'),
        ('cleveland', 'Cleveland, Ohio'),
        ('columbus', 'Columbus, Ohio'),
        ('dayton', 'Dayton / Springfield, Ohio'),
        ('limaohio', 'Lima Findlay, Ohio'),
        ('mansfield', 'Mansfield, Ohio'),
        ('toledo', 'Toledo, Ohio'),
        ('sandusky', 'Sandusky, Ohio'),
        ('tuscarawas', 'Tuscarawas Co, Ohio'),
        ('youngstown', 'Youngstown, Ohio'),
        ('zanesville', 'Zanesville / Cambridge, Ohio'),

        # Oklahoma
        ('lawton', 'Lawton, Oklahoma'),
        ('enid', 'Northwest Oklahoma'),
        ('oklahomacity', 'Oklahoma City, Oklahoma'),
        ('stillwater', 'Stillwater, Oklahoma'),
        ('tulsa', 'Tulsa, Oklahoma'),


        # Oregon
        ('bend', 'Bend, Oregon'),
        ('corvallis', 'Corvallis/Albany, Oregon'),
        ('eastoregon', 'East Oregon'),
        ('eugene', 'Eugene, Oregon'),
        ('klamath', 'Klamath Falls, Oregon'),
        ('medford', 'Medford / Ashland, Oregon'),
        ('oregoncoast', 'Oregon Coast, Oregon'),
        ('portland', 'Portland, Oregon'),
        ('roseburg', 'Roseburg, Oregon'),
        ('salem', 'Salem, Oregon'),

        # Pennsylvania
        ('altoona', 'Altoona / Johnstown, Pennsylvania'),
        ('chambersburg', 'Cumberland Valley, Pennsylvania'),
        ('erie', 'Erie, Pennsylvania'),
        ('harrisburg', 'Harrisburg, Pennsylvania'),
        ('lancaster', 'Lancaster, Pennsylvania'),
        ('allentown', 'Lehigh Valley, Pennsylvania'),
        ('meadville', 'Meadville, Pennsylvania'),
        ('philadelphia', 'Philadelphia, Pennsylvania'),
        ('pittsburgh', 'Pittsburgh, Pennsylvania'),
        ('poconos', 'Poconos, Pennsylvania'),
        ('reading', 'Reading, Pennsylvania'),
        ('scranton', 'Scranton / Wilkes-Barre, Pennsylvania'),
        ('pennstate', 'State College, Pennsylvania'),
        ('williamsport', 'Williamsport, Pennsylvania'),
        ('york', 'York, Pennsylvania'),

        # Rhode Island
        ('providence', 'Rhode Island'),

        # South Carolina
        ('charleston', 'Charleston, South Carolina'),
        ('columbia', 'Columbia, South Carolina'),
        ('florencesc', 'Florence, South Carolina'),
        ('greenville', 'Greenville / Upstate, South Carolina'),
        ('hiltonhead', 'Hilton Head, South Carolina'),
        ('myrtlebeach', 'Myrtle Beach, South Carolina'),

        # South Dakota
        ('nesd', 'Northeast South Dakota'),
        ('csd', 'Pierre / Central South Dakota'),
        ('rapidcity', 'Rapid City / West South Dakota'),
        ('siouxfalls', 'Sioux Falls / Southeast South Dakota'),
        ('sd', 'South Dakota'),

        # Tennessee
        ('chattanooga', 'Chattanooga, Tennessee'),
        ('clarksville', 'Clarksville, Tennessee'),
        ('cookeville', 'Cookeville, Tennessee'),
        ('jacksontn', 'Jackson, Tennessee'),
        ('knoxville', 'Knoxville, Tennessee'),
        ('memphis', 'Memphis, Tennessee'),
        ('nashville', 'Nashville, Tennessee'),
        ('tricities', 'Tri-Cities, Tennessee'),
        # Texas
        ('abilene', 'Abilene, Texas'),
        ('amarillo', 'Amarillo, Texas'),
        ('austin', 'Austin, Texas'),
        ('beaumont', 'Beaumont / Port Arthur, Texas'),
        ('brownsville', 'Brownsville, Texas'),
        ('collegestation', 'College Station, Texas'),
        ('corpuschristi', 'Corpus Christi, Texas'),
        ('dallas', 'Dallas / Fort Worth, Texas'),
        ('nacogdoches', 'Deep East Texas'),
        ('delrio', 'Del Rio / Eagle Pass, Texas'),
        ('elpaso', 'El Paso, Texas'),
        ('houston', 'Galveston, Texas'),
        ('galveston', 'Houston, Texas'),
        ('killeen', 'Killeen / Temple / Ft Hood, Texas'),
        ('laredo', 'Laredo, Texas'),
        ('lubbock', 'Lubbock, Texas'),
        ('mcallen', 'McCallen / Edinburg, Texas'),
        ('odessa', 'Odessa / Midland, Texas'),
        ('sanangelo', 'San Angelo, Texas'),
        ('sanantonio', 'San Antonio, Texas'),
        ('sanmarcos', 'San Marcos, Texas'),
        ('bigbend', 'Southwest Texas'),
        ('texoma', 'Texoma, Texas'),
        ('easttexas', 'Tyler / East Texas'),
        ('victoriatx', 'Victoria, Texas'),
        ('waco', 'Waco, Texas'),
        ('wichitafalls', 'Wichita Falls, Texas'),

        # Utah
        ('logan', 'Logan, Utah'),
        ('ogden', 'Ogden-Clearfield, Utah'),
        ('provo', 'Provo / Orem, Utah'),
        ('saltlakecity', 'Salt Lake City, Utah'),
        ('stgeorge', 'St George, Utah'),

        # Vermont
        ('vermon', 'Vermont'),

        # Virginia
        ('charlottesville', 'Charlottesville, Virginia'),
        ('danville', 'Danville, Virginia'),
        ('fredericksburg', 'Fredericksburg, Virginia'),
        ('norfolk', 'Norfolk, Virginia'),
        ('harrisonburg', 'Harrisonburg, Virginia'),
        ('lynchburg', 'Lynchburg, Virginia'),
        ('blacksburg', 'Blacksburg, Virginia'),
        ('richmond', 'Richmond, Virginia'),
        ('roanoke', 'Roanoke, Virginia'),
        ('swva', 'Southwest Virginia'),
        ('winchester', 'Winchester, Virginia'),

        # Washington
        ('bellingham', 'Bellingham, Washington'),
        ('kpr', 'Kennewick-Pasco-Richland, Washington'),
        ('moseslake', 'Moses Lake, Washington'),
        ('olympic', 'Olympic Peninsula, Washington'),
        ('pullman', 'Pullman / Moscow, Washington'),
        ('seattle', 'Seattle-Tacoma, Washington'),
        ('skagit', 'Skagit / Island / SJI, Washington'),
        ('spokane', 'Spokane / Coeur D\'alene, Washington'),
        ('wenatchee', 'Wenatchee, Washington'),
        ('yakima', 'Yakima, Washington'),


        # West Virginia
        ('charlestonwv', 'Charleston, West Virginia'),
        ('martinsburg', 'Eastern Panhandle, West Virginia'),
        ('huntington', 'Huntington-Ashland, West Virginia'),
        ('morgantown', 'Morgantown, West Virginia'),
        ('wheeling', 'Northern Panhandle, West Virginia'),
        ('parkersburg', 'Parkersburg-Marietta, West Virginia'),
        ('swv', 'Southern West Virginia'),
        ('wv', 'Old West Virginia'),

        # Wisconsin
        ('appleton', 'Appleton-Oshkosh-FDL, Wisconsin'),
        ('eauclaire', 'Eau Claire, Wisconsin'),
        ('greenbay', 'Green Bay, Wisconsin'),
        ('janesville', 'Janesville, Wisconsin'),
        ('racine', 'Kenosha-Racine, Wisconsin'),
        ('lacrosse', 'La Crosse, Wisconsin'),
        ('madison', 'Madison, Wisconsin'),
        ('milwaukee', 'Milwaukee, Wisconsin'),
        ('northernwi', 'Northern Wisconsin'),
        ('sheboygan', 'Sheboygan, Wisconsin'),
        ('wausau', 'Wauau, Wisconsin'),

        # Wyoming
        ('wyoming', 'Wyoming'),

        # Territories
        ('micronesia', 'Guam-Micronesia'),
        ('puertorico', 'Puerto Rico'),
        ('virgin', 'Virgin Islands'),



    ])
    price = IntegerField(default=500)
    submit = SubmitField('Search')

