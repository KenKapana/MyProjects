import doctest
START = 0

BEFORE_2010 = '200'
AFTER_2010 = '20'

input_date_split = tuple[str, str, str]
INPUT_DAY = 0
INPUT_MONTH = 1
INPUT_YEAR = 2

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
          'Nov', 'Dec']

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

def create_date(date: str) -> tuple:
    """ formats the date in int from year to date
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    >>> create_date('21-Jan-9')
    (2009, 1, 21)
    """
    result_list = []
    
    date = date.split('-')
    
    if 0 < int(date[INPUT_YEAR]) and int(date[INPUT_YEAR]) < 10:
        year = BEFORE_2010 + date[INPUT_YEAR]
    else:
        year = AFTER_2010 + date[INPUT_YEAR]
        
    result_list.append(int(year))
    #year
    
    index = 0
    while date[INPUT_MONTH] != months[index]:
        
        index += 1    
    result_list.append(index+1)
    #month
    
    result_list.append(int(date[INPUT_DAY]))
    #date
    
    date_info = tuple(result_list)
    
    return date_info

def create_show(type_:str, name:str, authors:list[str], actors:list[str], date:str):
    """combines input into one tuple
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
    '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))   
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
    '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
     ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
      'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
     (2019, 7, 1))
    >>> create_show('TV Show', 'The Avengers', '', '', '15-Feb-18')
    ('TV Show', 'The Avengers', [], [], (2018, 2, 15))
    >>> create_show('Movie', 'Fight Club', \
    'Uchenna Martinek:Mwayi Berardi:Jie Stroman:Jose Bryan:Xia Nielsen', \
    '', '12-Jan-23') # doctest: +NORMALIZE_WHITESPACE
    ('Movie', 'Fight Club', ['Uchenna Martinek', 'Mwayi Berardi', \
    'Jie Stroman', 'Jose Bryan', 'Xia Nielsen'], [], (2023, 1, 12))
    """
    show = []
    show.append(type_)
    show.append(name)
    if authors == '':
        show.append([])
    else:
        show.append(authors.split(':'))
    if actors == '':
        show.append([])
    else:
        show.append(actors.split(':'))
    show.append(create_date(date))
    
    return tuple(show)

def read_file(filename: str) -> list[NetflixShow]:
    """ Reads file at filename into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    """
    lo_shows = []
    
    file_handle = open(filename, 'r', encoding="utf8")
    show = file_handle.readline()
    show = file_handle.readline()
    while show != '':
        
        show_split = show.split(',')
        #print(show_split)
        one_show = create_show(show_split[INPUT_TYPE], show_split[INPUT_TITLE], show_split[INPUT_DIRECTORS], show_split[INPUT_CAST], show_split[INPUT_DATE])
        lo_shows.append(one_show)
        show = file_handle.readline()
    file_handle.close()
    
    return lo_shows
                
def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    """ Returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    """

    lo_oldest = []
    if show_data == []:
        return show_data
    oldest = show_data[START][DATE]
    
    for date in show_data:
        if date[DATE][YEAR] < oldest[YEAR]:
            oldest = date[DATE]
        if date[DATE][YEAR] == oldest[YEAR]:
            
            if date[DATE][MONTH] < oldest[MONTH]:
                oldest = date[DATE]
            if date[DATE][MONTH] == oldest[MONTH]:
                
                if date[DATE][DAY] < oldest[DAY]:
                    oldest = date[DATE]

    for show in show_data:
        
        if show[DATE] == oldest:
            lo_oldest.append(show[TITLE])
            
    return lo_oldest


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    """ Returns a sorted list of actors that are in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts) # doctest: +NORMALIZE_WHITESPACE
    ['Emma Stone', 'Hugh Bonneville', 'Lily Travers', 'Michael Cera', \
    'Om Puri', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Jonah Hill', 'Om Puri']
    """
    
    lo_actors = []
    result = []
    most_appearance = 0
    for lo_movie_info in shows:

        for actors in lo_movie_info[CAST]:
            lo_actors.append(actors)
        
    for actor in lo_actors:
        if most_appearance < lo_actors.count(actor):
            most_appearance = lo_actors.count(actor)
            
    for actor in lo_actors:
        if most_appearance == lo_actors.count(actor) and actor not in result:
            result.append(actor)
        result.sort()
    return result

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    """ returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    If terms is empty, all elements in show_data will be included in the returned list.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
     ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
      'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
      'Anupam Kher', 'Madhavan'],  \
     (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, []) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
       'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
       'Anupam Kher', 'Madhavan'],  \
      (2018, 8, 2)),\
     ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
      (2017, 12, 12)),\
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]
    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], 
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], 
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
        'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
        'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
       (2017, 12, 12)), \
      ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], \
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12)), \
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]
    """
    lo_shows = []
    if terms == []:
        lo_shows = show_data
    for shows in show_data:
        for keyword in terms:
            if keyword.lower() in shows[TITLE].lower() and shows not in lo_shows:
                lo_shows.append(shows)
    return lo_shows

def query(show_data: list[NetflixShow]) -> list[str]:
    """
    Returns a sorted list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    >>> get_shows_with_search_terms([('TV Show', 'The Godfather', ['Chidiebere Stroman', 'Shandiin Smith'], \
    ['Wayan Budai', 'Neo Berardi'], (2016, 11, 20)), \
    ('Movie', 'The Crown', ['Charis Stroman', 'Chidiebere Scriven'], \
    ['Chidiebere Blum', 'Connie Gereben'], (2016, 4, 17)), \
    ('TV Show', 'The Shawshank Redemption', ['Badr Garfield', 'Nur Martinek'], \
    ['Mayamiko MacAoidh', 'Uchenna Alserda', 'Jing Martinek'], (2013, 6, 25)), \
    ('Movie', 'The Simpsons', ['Uchenna Garfield'], [], (2009, 10, 21)), \
    ('Movie', 'The Office', \
    ['Bob MacAoidh', 'Jie Budai', 'Neo Berardi', 'Connie Blum'], \
    ['Shandiin Garfield'], (2001, 12, 3)), \
    ('Movie', 'Black Mirror', \
    ['Bob Nielsen', 'Neo MacAoidh', 'Charis Garfield', 'Uchenna Lee', \
    'Nur Martinek', 'Xia Scriven', 'Badr Berardi', 'Dada Berardi'], \
    ['Jing Martinek', 'Dada MacAoidh'], (2001, 9, 3)), \
    ('Movie', 'The Dark Knight', \
    ['Neo Alserda', 'Xia Stroman', 'Connie MacAoidh', 'Jose Berardi'], \
    ['Uchenna Stroman', 'Mayamiko Garfield', 'Mwayi Nielsen', 'Mwayi MacAoidh', \
    'Bob Stroman', 'Uchenna Nielsen', 'Dada Garfield', 'Jie Alserda'], \
    (2021, 1, 7))], \
    ['OFFICE', 'DARK', 'REDEMPTION', 'MIRROR', 'SIMPSONS', 'THE']) # doctest: +NORMALIZE_WHITESPACE
    [('TV Show', 'The Godfather', ['Chidiebere Stroman', 'Shandiin Smith'], \
    ['Wayan Budai', 'Neo Berardi'], (2016, 11, 20)), ('Movie', 'The Crown', \
    ['Charis Stroman', 'Chidiebere Scriven'], ['Chidiebere Blum', 'Connie Gereben'], \
    (2016, 4, 17)), ('TV Show', 'The Shawshank Redemption', ['Badr Garfield', 'Nur Martinek'], \
    ['Mayamiko MacAoidh', 'Uchenna Alserda', 'Jing Martinek'], (2013, 6, 25)), \
    ('Movie', 'The Simpsons', ['Uchenna Garfield'], [], (2009, 10, 21)), \
    ('Movie', 'The Office', ['Bob MacAoidh', 'Jie Budai', 'Neo Berardi', 'Connie Blum'], \
    ['Shandiin Garfield'], (2001, 12, 3)), ('Movie', 'Black Mirror', \
    ['Bob Nielsen', 'Neo MacAoidh', 'Charis Garfield', 'Uchenna Lee', 'Nur Martinek', \
    'Xia Scriven', 'Badr Berardi', 'Dada Berardi'], ['Jing Martinek', 'Dada MacAoidh'], \
    (2001, 9, 3)), ('Movie', 'The Dark Knight', ['Neo Alserda', 'Xia Stroman', 'Connie MacAoidh', \
    'Jose Berardi'], ['Uchenna Stroman', 'Mayamiko Garfield', 'Mwayi Nielsen', 'Mwayi MacAoidh', \
    'Bob Stroman', 'Uchenna Nielsen', 'Dada Garfield', 'Jie Alserda'], (2021, 1, 7))]
    """
    
    lo_shows = []
    lo_popular_actors = get_actors_in_most_shows(show_data)
    
    for actor in lo_popular_actors:
        for shows in show_data:
            if actor in shows[CAST] and shows[TITLE] not in lo_shows:
                lo_shows.append(shows[TITLE])
    lo_shows.sort()            
    
    return lo_shows
    