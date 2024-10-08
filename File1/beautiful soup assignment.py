#!/usr/bin/env python
# coding: utf-8

# # BEAUTIFUL SOUP ASSIGNMENT

# # SOLUTION 1

# In[ ]:


import lxml
import re
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from requests import get


# In[ ]:


url1 = "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"


# In[ ]:


"""docstring for IMDB"""
def __init__(self, url):
    super(IMDB, self).__init__()
    page = get(url)

    self.soup = BeautifulSoup(page.content, 'lxml')

def articleTitle(self):
    return self.soup.find("h1", class_="header").text.replace("\n","")

def bodyContent(self):
    content = self.soup.find(id="main")
    return content.find_all("div", class_="lister-item mode-advanced")

def movieData(self):
    movieFrame = self.bodyContent()
    movieTitle = []
    movieDate = []
    movieRunTime = []
    movieGenre = []
    movieRating = []
    movieScore = []
    movieDescription = []
    movieDirector = []
    movieStars = []
    movieVotes = []
    movieGross = []
    for movie in movieFrame:
        movieFirstLine = movie.find("h3", class_="lister-item-header")
        movieTitle.append(movieFirstLine.find("a").text)
        movieDate.append(re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text))
        try:
            movieRunTime.append(movie.find("span", class_="runtime").text[:-4])
        except:
            movieRunTime.append(np.nan)
        movieGenre.append(movie.find("span", class_="genre").text.rstrip().replace("\n","").split(","))
        try:
        movieRating.append(movie.find("strong").text)
        except:
        movieRating.append(np.nan)
        try:
            movieScore.append(movie.find("span", class_="metascore unfavorable").text.rstrip())
        except:
            movieScore.append(np.nan)
        movieDescription.append(movie.find_all("p", class_="text-muted")[-1].text.lstrip())
        movieCast = movie.find("p", class_="")

        try:
            casts = movieCast.text.replace("\n","").split('|')
            casts = [x.strip() for x in casts]
            casts = [casts[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
            movieDirector.append(casts[0])
            movieStars.append([x.strip() for x in casts[1].split(",")])
        except:
        casts = movieCast.text.replace("\n","").strip()
            movieDirector.append(np.nan)
            movieStars.append([x.strip() for x in casts.split(",")])

        movieNumbers = movie.find_all("span", attrs={"name": "nv"})

        if len(movieNumbers) == 2:
            movieVotes.append(movieNumbers[0].text)
            movieGross.append(movieNumbers[1].text)
        elif len(movieNumbers) == 1:
            movieVotes.append(movieNumbers[0].text)
            movieGross.append(np.nan)
        else:
            movieVotes.append(np.nan)
            movieGross.append(np.nan)

    movieData = [movieTitle, movieDate, movieRunTime, movieGenre, movieRating, movieScore, movieDescription,
                        movieDirector, movieStars, movieVotes, movieGross]
    return movieData
if __name__ == '__main__':
site1 = IMDB(url1)
print("Subject: ", site1.articleTitle())
data = site1.movieData()
for i in range(len(data)):
    print(data[i][:]) #Print the data
Subject:  Feature Film/TV Series(Sorted by Popularity Ascending) 
['Polar', 'Extremely Wicked, Shockingly Evil, and Vile', 'The Punisher', 'Glass', 'Sex Education', 'Game of Thrones', 'True Detective', 'Bohemian Rhapsody', 'Aquaman', 'Vikings', 'You', 'Green Book', 'The Favourite', 'A Star Is Born', 'Once Upon a Time in Hollywood', 'Fast & Furious Presents: Hobbs & Shaw', 'Serenity', 'Roma', 'Birds of Prey (And the Fantabulous Emancipation of One Harley Quinn)', 'The Orville', 'Titans', 'Velvet Buzzsaw', 'Alita: Battle Angel', 'The Walking Dead', 'Outlander', 'Vice', 'Kingdom', 'Mortal Engines', 'Widows', 'Avengers: Endgame', 'Grace and Frankie', 'IO', 'Joker', 'Spider-Man: Into the Spider-Verse', 'Black Mirror', "Grey's Anatomy", 'Shameless', 'Russian Doll', 'Supernatural', 'Suspiria', 'How to Train Your Dragon: The Hidden World', 'Bird Box', 'Star Trek: Discovery', 'American Crime Story', 'Brooklyn Nine-Nine', 'Doragon bôru chô: Burorî', 'BlacKkKlansman', 'Riverdale', 'Peaky Blinders', 'Split', 'Gotham', 'Close', 'The Big Bang Theory', 'The Office', 'The Good Place', 'The Upside', 'The Mule', 'The Passage', 'Conversations with a Killer: The Ted Bundy Tapes', 'Unbreakable Kimmy Schmidt', 'First Man', 'Friends', 'Suits', 'A Quiet Place', 'The Flash', 'Criminal Minds', 'Black Panther', 'Lucifer', 'Bumblebee', 'The Marvelous Mrs. Maisel', 'Arctic', 'Captain Marvel', 'Avengers: Infinity War', 'Tag', 'Fighting with My Family', 'Solo: A Star Wars Story', 'Mary Queen of Scots', 'The Blacklist', 'This Is Us', 'Arrow', 'Escape Room', 'Unbreakable', 'Rent', 'Hunter Killer', 'Stranger Things', 'The Kid Who Would Be King', 'Can You Ever Forgive Me?', 'A Private War', "The Girl in the Spider's Web", 'The Ballad of Buster Scruggs', 'Luther', 'Spider-Man: Far From Home', 'The Greatest Showman', 'Breaking Bad', 'Roswell, New Mexico', 'Friends from College', 'The Lego Movie 2: The Second Part', 'The Boys', 'Law & Order: Special Victims Unit', 'The Last Kingdom']
['2019', '2019', '2017– ', '2019', '2019– ', '2011– ', '2014– ', '2018', '2018', '2013– ', '2018– ', '2018', '2018', '2018', '2019', '2019', '2019', '2018', '2020', '2017– ', 'I 2018– ', '2019', '2019', '2010– ', '2014– ', 'I 2018', '2019– ', '2018', '2018', '2019', '2015– ', '2019', '2019', '2018', '2011– ', '2005– ', '2011– ', '2019– ', '2005– ', 'I 2018', '2019', '2018', '2017– ', '2016– ', '2013– ', '2018', '2018', '2016– ', '2013– ', 'IX 2016', '2014– ', 'I 2019', '2007– ', '2005–2013', '2016– ', '2017', '2018', '2019– ', '2019– ', '2015–2019', '2018', '1994–2004', '2011– ', '2018', '2014– ', '2005– ', '2018', '2015– ', '2018', '2017– ', '2018', '2019', '2018', 'I 2018', '2019', '2018', '2018', '2013– ', '2016– ', '2012– ', '2019', '2000', '2005', '2018', '2016– ', '2019', '2018', '2018', '2018', '2018', '2010– ', '2019', '2017', '2008–2013', '2019– ', '2017– ', '2019', '2019– ', '1999– ', '2015– ']
['118', '108', '53', '129', '45', '57', '55', '134', '143', '44', '60', '130', '119', '136', nan, nan, '106', '135', nan, '44', '45', '113', '122', '44', '64', '132', '45', '128', '129', nan, '30', '96', nan, '117', '60', '41', '46', '30', '44', '152', '104', '124', '60', '42', '22', '100', '135', '45', '60', '117', '42', '94', '22', '22', '22', '126', '116', '60', '60', '30', '141', '22', '44', '90', '43', '42', '134', '42', '114', '57', '97', '128', '149', '100', '108', '135', '124', '43', '45', '42', '99', '106', '138', '122', '51', '120', '106', '110', '117', '133', '60', nan, '105', '49', '60', '30', '106', '60', '60', '60']
[['Action', ' Crime'], ['Biography', ' Crime', ' Thriller'], ['Action', ' Adventure', ' Crime'], ['Drama', ' Sci-Fi', ' Thriller'], ['Comedy', ' Drama'], ['Action', ' Adventure', ' Drama'], ['Crime', ' Drama', ' Mystery'], ['Biography', ' Drama', ' Music'], ['Action', ' Adventure', ' Fantasy'], ['Action', ' Adventure', ' Drama'], ['Crime', ' Drama', ' Romance'], ['Biography', ' Comedy', ' Drama'], ['Biography', ' Comedy', ' Drama'], ['Drama', ' Music', ' Romance'], ['Comedy', ' Drama'], ['Action', ' Adventure'], ['Drama', ' Thriller'], ['Drama'], ['Action', ' Adventure', ' Crime'], ['Adventure', ' Comedy', ' Drama'], ['Action', ' Adventure', ' Drama'], ['Horror', ' Mystery', ' Thriller'], ['Action', ' Adventure', ' Romance'], ['Drama', ' Horror', ' Sci-Fi'], ['Drama', ' Fantasy', ' Romance'], ['Biography', ' Comedy', ' Drama'], ['Action', ' Thriller'], ['Action', ' Adventure', ' Fantasy'], ['Crime', ' Drama', ' Thriller'], ['Action', ' Adventure', ' Fantasy'], ['Comedy'], ['Adventure', ' Drama', ' Romance'], ['Crime', ' Drama', ' Thriller'], ['Animation', ' Action', ' Adventure'], ['Drama', ' Sci-Fi', ' Thriller'], ['Drama', ' Romance'], ['Comedy', ' Drama'], ['Comedy', ' Drama', ' Mystery'], ['Drama', ' Fantasy', ' Horror'], ['Fantasy', ' Horror', ' Mystery'], ['Animation', ' Action', ' Adventure'], ['Drama', ' Horror', ' Sci-Fi'], ['Action', ' Adventure', ' Drama'], ['Biography', ' Crime', ' Drama'], ['Comedy', ' Crime'], ['Animation', ' Action', ' Fantasy'], ['Biography', ' Crime', ' Drama'], ['Crime', ' Drama', ' Mystery'], ['Crime', ' Drama'], ['Horror', ' Thriller'], ['Action', ' Crime', ' Drama'], ['Action', ' Thriller'], ['Comedy', ' Romance'], ['Comedy'], ['Comedy', ' Drama', ' Fantasy'], ['Comedy', ' Drama'], ['Crime', ' Drama', ' Thriller'], ['Action', ' Adventure', ' Drama'], ['Documentary', ' Crime'], ['Comedy', ' Drama'], ['Biography', ' Drama', ' History'], ['Comedy', ' Romance'], ['Comedy', ' Drama'], ['Drama', ' Horror', ' Mystery'], ['Action', ' Adventure', ' Drama'], ['Crime', ' Drama', ' Mystery'], ['Action', ' Adventure', ' Sci-Fi'], ['Crime', ' Drama', ' Fantasy'], ['Action', ' Adventure', ' Sci-Fi'], ['Comedy', ' Drama'], ['Drama'], ['Action', ' Adventure', ' Sci-Fi'], ['Action', ' Adventure', ' Fantasy'], ['Comedy'], ['Biography', ' Comedy', ' Drama'], ['Action', ' Adventure', ' Fantasy'], ['Biography', ' Drama', ' History'], ['Crime', ' Drama', ' Mystery'], ['Comedy', ' Drama', ' Romance'], ['Action', ' Adventure', ' Crime'], ['Action', ' Adventure', ' Thriller'], ['Drama', ' Mystery', ' Sci-Fi'], ['Drama', ' Musical', ' Romance'], ['Action', ' Thriller'], ['Drama', ' Fantasy', ' Horror'], ['Adventure', ' Family', ' Fantasy'], ['Biography', ' Comedy', ' Crime'], ['Biography', ' Drama', ' War'], ['Action', ' Crime', ' Drama'], ['Comedy', ' Drama', ' Musical'], ['Crime', ' Drama', ' Mystery'], ['Action', ' Adventure', ' Comedy'], ['Biography', ' Drama', ' Musical'], ['Crime', ' Drama', ' Thriller'], ['Drama', ' Romance', ' Sci-Fi'], ['Comedy', ' Drama'], ['Animation', ' Action', ' Adventure'], ['Action', ' Drama', ' Sci-Fi'], ['Crime', ' Drama', ' Mystery'], ['Action', ' Drama', ' History']]
['6.3', '7.8', '8.6', '7.0', '8.5', '9.5', '9.0', '8.2', '7.4', '8.6', '7.9', '8.3', '7.9', '7.9', nan, nan, '5.1', '8.0', nan, '7.9', '8.2', '5.8', '7.6', '8.3', '8.5', '7.1', '8.4', '6.2', '7.2', nan, '8.3', '4.7', nan, '8.7', '8.9', '7.6', '8.7', '8.2', '8.5', '7.0', '8.0', '6.7', '7.4', '8.5', '8.4', '8.3', '7.5', '7.5', '8.8', '7.3', '7.9', '5.6', '8.2', '8.8', '8.2', '6.3', '7.2', '7.4', '8.0', '7.7', '7.4', '8.9', '8.6', '7.6', '7.9', '8.1', '7.4', '8.2', '7.1', '8.7', '7.3', nan, '8.5', '6.6', '8.1', '7.0', '6.5', '8.1', '8.7', '7.7', '6.4', '7.3', '7.0', '6.6', '8.9', '6.3', '7.3', '6.7', '6.1', '7.3', '8.5', nan, '7.6', '9.5', '5.4', '6.8', '7.5', nan, '8.0', '8.3']
['19', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, '38', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]
["The world's top assassin, Duncan Vizla, is settling into retirement when his former employer marks him as a liability to the firm. Against his will, he finds himself back in the game going head to head with an army of younger killers.", 'A chronicle of the crimes of Ted Bundy, from the perspective of his longtime girlfriend, Elizabeth Kloepfer, who refused to believe the truth about him for years.', 'After the murder of his family, Marine veteran Frank Castle becomes the vigilante known as "The Punisher," with only one goal in mind: to avenge them.', 'Security guard David Dunn uses his supernatural abilities to track Kevin Wendell Crumb, a disturbed man who has twenty-four personalities.', 'A teenage boy with a sex therapist mother teams up with a high school classmate to set up an underground sex therapy clinic at school.', 'Nine noble families fight for control over the mythical lands of Westeros, while an ancient enemy returns after being dormant for thousands of years.', 'Seasonal anthology series in which police investigations unearth the personal and professional secrets of those involved, both within and outside the law.', 'The story of the legendary rock band Queen and lead singer Freddie Mercury, leading up to their famous performance at Live Aid (1985).', 'Arthur Curry, the human-born heir to the underwater kingdom of Atlantis, goes on a quest to prevent a war between the worlds of ocean and land.', 'Vikings transports us to the brutal and mysterious world of Ragnar Lothbrok, a Viking warrior and farmer who yearns to explore - and raid - the distant shores across the ocean.', 'A clever bookstore manager relies on his savvy Internet know-how to make the woman of his dreams fall in love with him.', 'A working-class Italian-American bouncer becomes the driver of an African-American classical pianist on a tour of venues through the 1960s American South.', 'In early 18th century England, a frail Queen Anne occupies the throne and her close friend, Lady Sarah, governs the country in her stead. When a new servant, Abigail, arrives, her charm endears her to Sarah.', 'A musician helps a young singer find fame, even as age and alcoholism send his own career into a downward spiral.', 'A faded TV actor and his stunt double strive to achieve fame and success in the film industry during the final years of the Hollywood Golden Age in 1969 Los Angeles.', 'Lawman Luke Hobbs and outcast Deckard Shaw form an unlikely alliance when a cyber-genetically enhanced villain threatens the future of humanity.', 'A fishing boat captain juggles facing his mysterious past and finding himself ensnared in a reality where nothing is what it seems.', "A year in the life of a middle-class family's maid in Mexico City in the early 1970s.", 'After splitting up with the Joker, Harley Quinn joins three female superheroes - Black Canary, Huntress and Renee Montoya - to save the life of a little girl (Cassandra Cain) from an evil crime lord.', 'An exploratory ship from Earth faces intergalactic challenges 400 years in the future.', "A team of young superheroes led by Nightwing (formerly Batman's first Robin) form to combat evil and other perils.", 'After a series of paintings by an unknown artist are discovered, a supernatural force enacts revenge on those who have allowed their greed to get in the way of art.', "An action-packed story of one young woman's journey to discover the truth of who she is and her fight to change the world.", 'Sheriff Deputy Rick Grimes wakes up from a coma to learn the world is in ruins, and must lead a group of survivors to stay alive.', 'An English combat nurse from 1945 is mysteriously swept back in time to 1743.', 'The story of Dick Cheney, an unassuming bureaucratic Washington insider, who quietly wielded immense power as Vice President to George W. Bush, reshaping the country and the globe in ways that we still feel today.', 'While strange rumors about their ill king grip a kingdom, the crown prince becomes their only hope against a mysterious plague overtaking the land.', 'In a post-apocalyptic world where cities ride on wheels and consume each other to survive, two people meet in London and try to stop a conspiracy.', "Set in contemporary Chicago, amid a time of turmoil, four women with nothing in common except a debt left behind by their dead husbands' criminal activities, take fate into their own hands, and conspire to forge a future on their own terms.", "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to undo Thanos' actions and restore order to the universe.", 'Finding out that their husbands are not just work partners, but have also been romantically involved for the last twenty years, two women with an already strained relationship try to cope with the circumstances together.', "As a young scientist searches for a way to save a dying Earth, she finds a connection with a man who's racing to catch the last shuttle off the planet.", 'A failed stand-up comedian is driven insane and becomes a psychopathic murderer.', 'Teen Miles Morales becomes Spider-Man of his reality, crossing his path with five counterparts from other dimensions to stop a threat for all realities.', "An anthology series exploring a twisted, high-tech world where humanity's greatest innovations and darkest instincts collide.", 'A drama centered on the personal and professional lives of five surgical interns and their supervisors.', 'A scrappy, fiercely loyal Chicago family makes no apologies.', "A cynical young woman in New York City keeps dying and returning to the party that's being thrown in her honor on that same evening. She tries to find a way out of this strange time loop.", 'Two brothers follow their father\'s footsteps as "hunters", fighting evil supernatural beings of many kinds, including monsters, demons, and gods that roam the earth.', 'A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.', 'When Hiccup discovers Toothless isn\'t the only Night Fury, he must seek "The Hidden World", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.', 'Five years after an ominous unseen presence drives most of society to suicide, a mother and her two children make a desperate bid to reach safety.', 'Ten years before Kirk, Spock, and the Enterprise, the USS Discovery discovers new worlds and lifeforms as one Starfleet officer learns to understand all things alien.', "An anthology series centered around America's most notorious crimes and criminals.", "Jake Peralta, an immature, but talented N.Y.P.D. detective in Brooklyn's 99th Precinct, comes into immediate conflict with his new commanding officer, the serious and stern Captain Ray Holt.", "Goku and Vegeta encounter Broly, a Saiyan warrior unlike any fighter they've faced before.", 'Ron Stallworth, an African American police officer from Colorado Springs, CO, successfully manages to infiltrate the local Ku Klux Klan branch with the help of a Jewish surrogate who eventually becomes its leader. Based on actual events.', 'While navigating the troubled waters of romance, school and family, Archie and his gang become entangled in dark Riverdale mysteries.', 'A gangster family epic set in 1919 Birmingham, England; centered on a gang who sew razor blades in the peaks of their caps, and their fierce boss Tommy Shelby.', 'Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.', "The story behind Detective James Gordon's rise to prominence in Gotham City in the years before Batman's arrival.", 'Sam, a bodyguard and counter-terrorism expert, takes a job protecting a rich young heiress named Zoe. Neither party is keen on the arrangement until a violent kidnapping forces them to go on the run.', 'A woman who moves into an apartment across the hall from two brilliant but socially awkward physicists shows them how little they know about life outside of the laboratory.', 'A mockumentary on a group of typical office workers, where the workday consists of ego clashes, inappropriate behavior, and tedium.', 'Four people and their otherworldly frienemy struggle in the afterlife to define what it means to be good.', "A comedic look at the relationship between a wealthy man with quadriplegia and an unemployed man with a criminal record who's hired to help him.", 'A 90-year-old horticulturist and Korean War veteran is caught transporting $3 million worth of cocaine through Illinois for a Mexican drug cartel.', 'When a botched U.S. government experiment turns a group of death row inmates into highly infectious vampires, an orphan girl might be the only person able to stop the ensuing crisis.', 'A look inside the mind of serial killer Ted Bundy, featuring interviews with him on death row.', 'A woman is rescued from a doomsday cult and starts life over again in New York City.', 'A look at the life of the astronaut, Neil Armstrong, and the legendary space mission that led him to become the first man to walk on the Moon on July 20, 1969.', 'Follows the personal and professional lives of six twenty to thirty-something-year-old friends living in Manhattan.', "On the run from a drug deal gone bad, Mike Ross, a brilliant college dropout, finds himself a job working with Harvey Specter, one of New York City's best lawyers.", 'In a post-apocalyptic world, a family is forced to live in silence while hiding from monsters with ultra-sensitive hearing.', "After being struck by lightning, Barry Allen wakes up from his coma to discover he's been given the power of super speed, becoming the Flash, fighting crime in Central City.", "The cases of the F.B.I. Behavioral Analysis Unit (B.A.U.), an elite group of profilers who analyze the nation's most dangerous serial killers and individual heinous crimes in an effort to anticipate their next moves before they strike again.", "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.", "Lucifer Morningstar has decided he's had enough of being the dutiful servant in Hell and decides to spend some time on Earth to better understand humanity. He settles in Los Angeles - the City of Angels.", 'On the run in the year of 1987, Bumblebee finds refuge in a junkyard in a small Californian beach town. Charlie, on the cusp of turning 18 and trying to find her place in the world, discovers Bumblebee, battle-scarred and broken.', 'A housewife in the 1950s decides to become a stand-up comic.', 'A man stranded in the Arctic after an airplane crash must decide whether to remain in the relative safety of his makeshift camp or to embark on a deadly trek through the unknown.', "Carol Danvers becomes one of the universe's most powerful heroes when Earth is caught in the middle of a galactic war between two alien races.", 'The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.', 'A small group of former classmates organize an elaborate, annual game of tag that requires some to travel all over the country.', 'A former wrestler and his family make a living performing at small venues around the country while his kids dream of joining World Wrestling Entertainment.', 'During an adventure into the criminal underworld, Han Solo meets his future co-pilot Chewbacca and encounters Lando Calrissian years before joining the Rebellion.', "Mary Stuart's attempt to overthrow her cousin Elizabeth I, Queen of England, finds her condemned to years of imprisonment before facing execution.", 'A new FBI profiler, Elizabeth Keen, has her entire life uprooted when a mysterious criminal, Raymond Reddington, who has eluded capture for decades, turns himself in and insists on speaking only to her.', 'A heartwarming and emotional story about a unique set of triplets, their struggles, and their wonderful parents.', 'Spoiled billionaire playboy Oliver Queen is missing and presumed dead when his yacht is lost at sea. He returns five years later a changed man, determined to clean up the city as a hooded vigilante armed with a bow.', 'Six strangers find themselves in a maze of deadly mystery rooms, and must use their wits to survive.', 'A man learns something extraordinary about himself after a devastating accident.', 'This is the film version of the Pulitzer and Tony Award winning musical about Bohemians in the East Village of New York City struggling with life, love and AIDS, and the impacts they have on America.', 'An untested American submarine captain teams with U.S. Navy Seals to rescue the Russian president, who has been kidnapped by a rogue general.', 'When a young boy disappears, his mother, a police chief, and his friends must confront terrifying forces in order to get him back.', 'A band of kids embark on an epic quest to thwart a medieval menace.', 'When Lee Israel falls out of step with current tastes, she turns her art form to deception.', 'One of the most celebrated war correspondents of our time, Marie Colvin is an utterly fearless and rebellious spirit, driven to the frontline of conflicts across the globe to give voice to the voiceless.', 'Young computer hacker Lisbeth Salander and journalist Mikael Blomkvist find themselves caught in a web of spies, cybercriminals and corrupt government officials.', 'Six tales of life and violence in the Old West, following a singing gunslinger, a bank robber, a traveling impresario, an elderly prospector, a wagon train, and a perverse pair of bounty hunters.', "DCI John Luther is a near-genius murder detective whose brilliant mind can't always save him from the dangerous violence of his passions.", 'Peter Parker and his friends go on summer vacation to Europe, where Peter finds himself trying to save his friends against a villain known as Mysterio.', 'Celebrates the birth of show business and tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.', "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's future.", 'A reimagining of Roswell, which centers on the residents of New Mexico, where aliens live undercover among humans.', 'A group of friends from Harvard are facing down their forties. With interwoven and oftentimes complicated relationships with one another. "Friends from College" is a comedic exploration of ...                See full summary\xa0»\n', "It's been five years since everything was awesome and the citizens are facing a huge new threat: Lego Duplo invaders from outer space, wrecking everything faster than they can rebuild.", 'An action story centered on a CIA squad tasked with keeping superheroes in line, by any means necessary.', 'The Special Victims Unit, a specially trained squad of detectives in the NYPD, investigate sexually related crimes.', 'The year is 872, and many of the separate kingdoms of what we now know as England have fallen to the invading Danes, leaving the great kingdom of Wessex standing alone and defiant under the...                See full summary\xa0»\n']
['Jonas Åkerlund', 'Joe Berlinger', nan, 'M. Night Shyamalan', nan, nan, nan, 'Bryan Singer', 'James Wan', nan, nan, 'Peter Farrelly', 'Yorgos Lanthimos', 'Bradley Cooper', 'Quentin Tarantino', 'David Leitch', 'Steven Knight', 'Alfonso Cuarón', 'Cathy Yan', nan, nan, 'Dan Gilroy', 'Robert Rodriguez', nan, nan, 'Adam McKay', nan, 'Christian Rivers', 'Steve McQueen', 'Directors:Anthony Russo, Joe Russo', nan, 'Jonathan Helpert', 'Todd Phillips', 'Directors:Bob Persichetti, Peter Ramsey, Rodney Rothman', nan, nan, nan, nan, nan, 'Luca Guadagnino', 'Dean DeBlois', 'Susanne Bier', nan, nan, nan, 'Tatsuya Nagamine', 'Spike Lee', nan, nan, 'M. Night Shyamalan', nan, 'Vicky Jewson', nan, nan, nan, 'Neil Burger', 'Clint Eastwood', nan, nan, nan, 'Damien Chazelle', nan, nan, 'John Krasinski', nan, nan, 'Ryan Coogler', nan, 'Travis Knight', nan, 'Joe Penna', 'Directors:Anna Boden, Ryan Fleck', 'Directors:Anthony Russo, Joe Russo', 'Jeff Tomsic', 'Stephen Merchant', 'Ron Howard', 'Josie Rourke', nan, nan, nan, 'Adam Robitel', 'M. Night Shyamalan', 'Chris Columbus', 'Donovan Marsh', nan, 'Joe Cornish', 'Marielle Heller', 'Matthew Heineman', 'Fede Alvarez', 'Directors:Ethan Coen, Joel Coen', nan, 'Jon Watts', 'Michael Gracey', nan, nan, nan, 'Mike Mitchell', nan, nan, nan]
[['Mads Mikkelsen', 'Vanessa Hudgens', 'Katheryn Winnick', 'Fei Ren'], ['Lily Collins', 'Zac Efron', 'Angela Sarafyan', 'Sydney Vollmer'], ['Stars:Jon Bernthal', 'Amber Rose Revah', 'Ben Barnes', 'Jason R. Moore'], ['James McAvoy', 'Bruce Willis', 'Samuel L. Jackson', 'Anya Taylor-Joy'], ['Stars:Asa Butterfield', 'Gillian Anderson', 'Emma Mackey', 'Alistair Petrie'], ['Stars:Emilia Clarke', 'Peter Dinklage', 'Kit Harington', 'Lena Headey'], ['Stars:Vince Vaughn', 'Colin Farrell', 'Rachel McAdams', 'Taylor Kitsch'], ['Rami Malek', 'Lucy Boynton', 'Gwilym Lee', 'Ben Hardy'], ['Jason Momoa', 'Amber Heard', 'Willem Dafoe', 'Patrick Wilson'], ['Stars:Gustaf Skarsgård', 'Katheryn Winnick', 'Alexander Ludwig', 'Travis Fimmel'], ['Stars:Penn Badgley', 'Ambyr Childers', 'Elizabeth Lail', 'Luca Padovan'], ['Viggo Mortensen', 'Mahershala Ali', 'Linda Cardellini', 'Sebastian Maniscalco'], ['Olivia Colman', 'Emma Stone', 'Rachel Weisz', 'Nicholas Hoult'], ['Lady Gaga', 'Bradley Cooper', 'Sam Elliott', 'Greg Grunberg'], ['Margot Robbie', 'Margaret Qualley', 'Leonardo DiCaprio', 'Brad Pitt'], ['Eiza González', 'Vanessa Kirby', 'Dwayne Johnson', 'Idris Elba'], ['Matthew McConaughey', 'Anne Hathaway', 'Diane Lane', 'Jason Clarke'], ['Yalitza Aparicio', 'Marina de Tavira', 'Diego Cortina Autrey', 'Carlos Peralta'], ['Margot Robbie', 'Jurnee Smollett-Bell', 'Mary Elizabeth Winstead', 'Ewan McGregor'], ['Stars:Seth MacFarlane', 'Adrianne Palicki', 'Penny Johnson Jerald', 'Scott Grimes'], ['Stars:Teagan Croft', 'Brenton Thwaites', 'Anna Diop', 'Ryan Potter'], ['Jake Gyllenhaal', 'Rene Russo', 'Zawe Ashton', 'Tom Sturridge'], ['Rosa Salazar', 'Christoph Waltz', 'Jennifer Connelly', 'Mahershala Ali'], ['Stars:Andrew Lincoln', 'Norman Reedus', 'Melissa McBride', 'Lauren Cohan'], ['Stars:Caitriona Balfe', 'Sam Heughan', 'Duncan Lacroix', 'Tobias Menzies'], ['Christian Bale', 'Amy Adams', 'Steve Carell', 'Sam Rockwell'], ['Stars:Doona Bae', 'Greg Chun', 'Jun-ho Heo', 'Ji-Hoon Ju'], ['Hera Hilmar', 'Robert Sheehan', 'Hugo Weaving', 'Jihae'], ['Viola Davis', 'Michelle Rodriguez', 'Elizabeth Debicki'], ['Bradley Cooper', 'Brie Larson', 'Scarlett Johansson', 'Evangeline Lilly'], ['Stars:Jane Fonda', 'Lily Tomlin', 'Sam Waterston', 'Martin Sheen'], ['Margaret Qualley', 'Anthony Mackie', 'Danny Huston', 'Tom Payne'], ['Joaquin Phoenix', 'Robert De Niro', 'Zazie Beetz', 'Shea Whigham'], ['Shameik Moore', 'Jake Johnson', 'Hailee Steinfeld', 'Mahershala Ali'], ['Stars:Daniel Lapaine', 'Hannah John-Kamen', 'Michaela Coel', 'Beatrice Robertson-Jones'], ['Stars:Ellen Pompeo', 'Justin Chambers', 'Chandra Wilson', 'James Pickens Jr.'], ['Stars:Emmy Rossum', 'William H. Macy', 'Ethan Cutkosky', 'Jeremy Allen White'], ['Stars:Natasha Lyonne', 'Charlie Barnett', 'Greta Lee', 'Elizabeth Ashley'], ['Stars:Jared Padalecki', 'Jensen Ackles', 'Jim Beaver', 'Misha Collins'], ['Dakota Johnson', 'Tilda Swinton', 'Doris Hick', 'Malgorzata Bela'], ['Jay Baruchel', 'America Ferrera', 'F. Murray Abraham', 'Cate Blanchett'], ['Sandra Bullock', 'Trevante Rhodes', 'John Malkovich', 'Sarah Paulson'], ['Stars:Sonequa Martin-Green', 'Doug Jones', 'Anthony Rapp', 'Mary Wiseman'], ['Stars:Sarah Paulson', 'Cuba Gooding Jr.', 'Courtney B. Vance', 'Sterling K. Brown'], ['Stars:Andy Samberg', 'Stephanie Beatriz', 'Terry Crews', 'Melissa Fumero'], ['Masako Nozawa', 'Aya Hisakawa', 'Ryô Horikawa', 'Toshio Furukawa'], ['John David Washington', 'Adam Driver', 'Laura Harrier', 'Topher Grace'], ['Stars:K.J. Apa', 'Lili Reinhart', 'Camila Mendes', 'Cole Sprouse'], ['Stars:Cillian Murphy', 'Helen McCrory', 'Paul Anderson', 'Sophie Rundle'], ['James McAvoy', 'Anya Taylor-Joy', 'Haley Lu Richardson', 'Jessica Sula'], ['Stars:Ben McKenzie', 'Jada Pinkett Smith', 'Donal Logue', 'Camren Bicondova'], ['Noomi Rapace', 'Olivia Jewson', 'Abdellatif Chaouqi', 'Sophie Nélisse'], ['Stars:Kaley Cuoco', 'Johnny Galecki', 'Jim Parsons', 'Simon Helberg'], ['Stars:Steve Carell', 'Jenna Fischer', 'John Krasinski', 'Rainn Wilson'], ['Stars:Kristen Bell', 'William Jackson Harper', 'Jameela Jamil', "D'Arcy Carden"], ['Kevin Hart', 'Bryan Cranston', 'Nicole Kidman', 'Aja Naomi King'], ['Bradley Cooper', 'Clint Eastwood', 'Michael Peña', 'Manny Montana'], ['Stars:Mark-Paul Gosselaar', 'Saniyya Sidney', 'Jamie McShane', 'Caroline Chikezie'], ['Stars:Hugh Aynesworth', 'Bob Keppel', 'Stephen Michaud', 'Ted Bundy'], ['Stars:Ellie Kemper', 'Jane Krakowski', 'Tituss Burgess', 'Carol Kane'], ['Ryan Gosling', 'Claire Foy', 'Jason Clarke', 'Kyle Chandler'], ['Stars:Jennifer Aniston', 'Courteney Cox', 'Lisa Kudrow', 'Matt LeBlanc'], ['Stars:Gabriel Macht', 'Patrick J. Adams', 'Meghan Markle', 'Sarah Rafferty'], ['Emily Blunt', 'John Krasinski', 'Millicent Simmonds', 'Noah Jupe'], ['Stars:Grant Gustin', 'Candice Patton', 'Danielle Panabaker', 'Carlos Valdes'], ['Stars:Matthew Gray Gubler', 'Kirsten Vangsness', 'A.J. Cook', 'Joe Mantegna'], ['Chadwick Boseman', 'Michael B. Jordan', "Lupita Nyong'o", 'Danai Gurira'], ['Stars:Lauren German', 'Tom Ellis', 'Kevin Alejandro', 'D.B. Woodside'], ['Hailee Steinfeld', 'Jorge Lendeborg Jr.', 'John Cena', 'Jason Drucker'], ['Stars:Rachel Brosnahan', 'Michael Zegen', 'Marin Hinkle', 'Tony Shalhoub'], ['Mads Mikkelsen', 'Maria Thelma Smáradóttir'], ['Brie Larson', 'Gemma Chan', 'Samuel L. Jackson', 'Mckenna Grace'], ['Robert Downey Jr.', 'Chris Hemsworth', 'Mark Ruffalo', 'Chris Evans'], ['Jeremy Renner', 'Ed Helms', 'Jake Johnson', 'Jon Hamm'], ['Dwayne Johnson', 'Florence Pugh', 'Lena Headey', 'Saraya-Jade Bevis'], ['Alden Ehrenreich', 'Woody Harrelson', 'Emilia Clarke', 'Donald Glover'], ['Saoirse Ronan', 'Margot Robbie', 'Jack Lowden', 'Joe Alwyn'], ['Stars:James Spader', 'Megan Boone', 'Diego Klattenhoff', 'Ryan Eggold'], ['Stars:Milo Ventimiglia', 'Mandy Moore', 'Sterling K. Brown', 'Chrissy Metz'], ['Stars:Stephen Amell', 'Katie Cassidy', 'David Ramsey', 'Susanna Thompson'], ['Taylor Russell', 'Logan Miller', 'Jay Ellis', 'Tyler Labine'], ['Bruce Willis', 'Samuel L. Jackson', 'Robin Wright', 'Spencer Treat Clark'], ['Taye Diggs', 'Wilson Jermaine Heredia', 'Rosario Dawson', 'Anthony Rapp'], ['Gerard Butler', 'Gary Oldman', 'Common', 'Linda Cardellini'], ['Stars:Millie Bobby Brown', 'Finn Wolfhard', 'Winona Ryder', 'David Harbour'], ['Louis Ashbourne Serkis', 'Denise Gough', 'Dean Chaumoo', 'Tom Taylor'], ['Melissa McCarthy', 'Richard E. Grant', 'Dolly Wells', 'Ben Falcone'], ['Rosamund Pike', 'Greg Wise', 'Alexandra Moen', 'Tom Hollander'], ['Claire Foy', 'Beau Gadsdon', 'Sverrir Gudnason', 'Lakeith Stanfield'], ['Tim Blake Nelson', 'Willie Watson', 'Clancy Brown', 'Danny McCarthy'], ['Stars:Idris Elba', 'Dermot Crowley', 'Michael Smiley', 'Warren Brown'], ['Zendaya', 'Jake Gyllenhaal', 'Cobie Smulders', 'Samuel L. Jackson'], ['Hugh Jackman', 'Michelle Williams', 'Zac Efron', 'Zendaya'], ['Stars:Bryan Cranston', 'Aaron Paul', 'Anna Gunn', 'Betsy Brandt'], ['Stars:Jeanine Mason', 'Nathan Parsons', 'Michael Vlamis', 'Lily Cowles'], ['Stars:Keegan-Michael Key', 'Cobie Smulders', 'Annie Parisse', 'Nat Faxon'], ['Chris Pratt', 'Elizabeth Banks', 'Will Arnett', 'Tiffany Haddish'], ['Stars:Karl Urban', 'Tomer Capon', 'Jennifer Esposito', 'Erin Moriarty'], ['Stars:Mariska Hargitay', 'Christopher Meloni', 'Ice-T', 'Dann Florek'], ['Stars:Alexander Dreymon', 'Ian Hart', 'David Dawson', 'Eliza Butterworth']]
['29,815', '404', '133,239', '58,153', '33,544', '1,407,282', '424,648', '234,545', '159,280', '324,111', '41,555', '53,118', '44,602', '170,127', nan, nan, '2,975', '69,264', nan, '41,222', '27,867', '16,872', '3,107', '770,334', '88,468', '28,061', '4,441', '34,200', '38,269', nan, '26,862', '17,368', nan, '92,639', '288,545', '206,210', '164,295', '9,438', '345,218', '22,280', '9,164', '176,778', '59,810', '62,952', '132,284', '10,550', '100,900', '78,452', '175,477', '328,942', '187,999', '8,575', '630,471', '281,728', '52,668', '9,986', '17,143', '2,809', '6,341', '52,990', '91,433', '646,066', '318,053', '271,263', '268,071', '135,280', '457,138', '131,247', '48,433', '38,015', '1,008', nan, '581,342', '70,351', '454', '201,929', '8,966', '151,431', '71,289', '372,518', '8,374', '333,024', '46,087', '22,304', '557,424', '1,706', '9,052', '4,075', '16,928', '67,974', '101,060', nan, '187,614', '1,156,819', '2,621', '13,219', '806', nan, '66,557', '49,267']
[nan, nan, nan, '$91.43M', nan, nan, nan, '$209.12M', '$324.94M', nan, nan, '$57.51M', '$29.25M', '$208.11M', nan, nan, '$8.20M', nan, nan, nan, nan, nan, nan, nan, nan, '$44.46M', nan, '$15.95M', '$42.38M', nan, nan, nan, nan, '$176.53M', nan, nan, nan, nan, nan, '$2.47M', nan, nan, nan, nan, nan, '$30.24M', '$48.69M', nan, nan, '$138.29M', nan, nan, nan, nan, nan, '$77.94M', '$102.07M', nan, nan, nan, '$44.94M', nan, nan, '$188.02M', nan, nan, '$700.06M', nan, '$124.81M', nan, '$0.06M', nan, '$678.82M', '$54.55M', nan, '$213.77M', '$16.47M', nan, nan, nan, '$52.87M', '$95.01M', '$29.08M', '$15.77M', nan, '$14.06M', '$8.42M', '$1.63M', '$14.84M', nan, nan, nan, '$174.34M', nan, nan, nan, nan, nan, nan, nan]


# # solution 2

# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_patreon_posts(url):
  """Scrapes post details from a Patreon creator page URL.

  Args:
      url (str): The URL of the Patreon creator page.

  Returns:
      list: A list of dictionaries, each containing scraped information for a post.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'lxml')

    # Find all post elements (adjust selectors as needed)
    posts = soup.find_all('div', class_='post')

    scraped_posts = []
    for post in posts:
      post_data = {}

      # Extract heading
      heading = post.find('h3', class_='post-header__title')
      post_data['Heading'] = heading.text.strip() if heading else None

      # Extract date
      date_tag = post.find('time', class_='post-meta__date')
      post_data['Date'] = date_tag.text.strip() if date_tag else None

      # Extract content snippet
      content = post.find('div', class_='post__content')
      post_data['Content'] = content.text.strip() if content else None

      # Extract YouTube video link (if present)
      youtube_link = None
      for iframe in content.find_all('iframe'):
        if iframe.get('src') and 'youtube.com/embed/' in iframe.get('src'):
          youtube_link = iframe.get('src')
          break
      post_data['YouTube Link'] = youtube_link

      scraped_posts.append(post_data)

    return scraped_posts

  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")
    return []

# Example usage
patreon_url = 'https://www.patreon.com/coreyms'
scraped_data = scrape_patreon_posts(patreon_url)

if scraped_data:
  print("Scraped Post Details:")
  for post in scraped_data:
    print(f"\nHeading: {post['Heading']}")
    print(f"Date: {post['Date']}")
    print(f"Content Snippet:\n{post['Content'][:100]}...")  # Display first 100 chars
    if post['YouTube Link']:
      print(f"YouTube Link: {post['YouTube Link']}")
else:
  print("No posts found or error occurred during scraping.")


# # solution 3

# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_nobroker_houses(locality):
  """Scrapes house details from Nobroker for a given locality.

  Args:
      locality (str): The locality to search for (e.g., "Indira Nagar").

  Returns:
      list: A list of dictionaries, each containing scraped house details.
  """

  base_url = "https://www.nobroker.in/property/rent/bangalore/Bangalore/?searchParam=W3sibGF0IjoxMy4wNDM3NjEyODI5MTkyLCJsb24iOjgwLjIwMDA2ODUxNjk2OTMsInNob3dNYXAiOmZhbHNlLCJwbGFjZUlkIjoiQ2hJSllUTjlULXBsVWpvUk05UmphQXVuWVc0IiwicGxhY2VOYW1lIjoiQ2hlbm5haSIsImNpdHkiOiJjaGVubmFpIn1d&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&locality="
  locality_url = base_url + locality

  try:
    response = requests.get(locality_url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'lxml')

    # Find all property cards (adjust selectors as needed)
    properties = soup.find_all('div', class_='css-763reb ewqz85m')

    scraped_houses = []
    for property in properties:
      house_data = {}

      # Extract title (adjust selector if title element changes)
      title_tag = property.find('h2', class_='heading-6')
      house_data['Title'] = title_tag.text.strip() if title_tag else None

      # Extract location (adjust selector if location element changes)
      location_tag = property.find('div', class_='css-19mggfn e1127z97')
      house_data['Location'] = location_tag.text.strip() if location_tag else None

      # Extract details containing area, EMI, and price (heuristics)
      details = property.find_all('div', class_='css-xrz2ju')  # Adjust selector
      for detail in details:
        detail_text = detail.text.strip()
        if 'sqft' in detail_text:  # Assuming area is indicated by sqft
          house_data['Area'] = detail_text.split()[0]  # Extract area value
        elif 'EMI' in detail_text:  # Assuming EMI is indicated by EMI keyword
          house_data['EMI'] = detail_text.split()[1]  # Extract EMI value (may need further processing)
        elif '₹' in detail_text and not 'EMI' in detail_text:  # Assuming price is indicated by ₹
          house_data['Price'] = detail_text.split()[0]  # Extract price value (may need further processing)

      scraped_houses.append(house_data)

    return scraped_houses

  except requests.exceptions.RequestException as e:
    print(f"Error scraping houses for {locality}: {e}")
    return []

# Example usage
localities = ["Indira Nagar", "Jayanagar", "Rajaji Nagar"]

all_scraped_houses = []
for locality in localities:
  scraped_houses = scrape_nobroker_houses(locality)
  all_scraped_houses.extend(scraped_houses)  # Combine results from all localities

if all_scraped_houses:
  print("Scraped House Details:")
  for house in all_scraped_houses:
    print(f"\nTitle: {house['Title']}")
    print(f"Location: {house['Location']}")
    print(f"Area: {house.get('Area')}")  # Print only if available
    print(f"EMI: {house.get('EMI')}")  # Print only if available
    print(f"Price: {house.get('Price')}")  # Print only if available
else:
  print("No houses found or error occurred during scraping.")


# # solution 4

# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_bewakoof_products(url):
  """Scrapes product details from the given Bewakoof URL.

  Args:
      url (str): The URL of the Bewakoof page to scrape.

  Returns:
      list: A list of dictionaries, each containing scraped product details.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'lxml')

    # Find all product elements (adjust selectors as needed)
    products = soup.find_all('div', class_='productGrid_item')[:10]  # Limit to 10 products

    scraped_products = []
    for product in products:
      product_data = {}

      # Extract product name
      name_tag = product.find('a', class_='productGrid_itemName')
      product_data['Name'] = name_tag.text.strip() if name_tag else None

      # Extract price
      price_tag = product.find('span', class_='priceTag')
      if price_tag:
        price_text = price_tag.text.strip()
        # Assuming price format is "₹[amount]"
        product_data['Price'] = price_text.split('₹')[1] if len(price_text.split('₹')) > 1 else None

      # Extract image URL
      image_tag = product.find('img', class_='productGrid_image')
      product_data['Image URL'] = image_tag.get('src') if image_tag else None

      scraped_products.append(product_data)

    return scraped_products

  except requests.exceptions.RequestException as e:
    print(f"Error scraping products from {url}: {e}")
    return []

# Example usage
url = "https://www.bewakoof.com/bestseller?sort=popular"
scraped_products = scrape_bewakoof_products(url)

if scraped_products:
  print("Scraped Product Details (First 10):")
  for product in scraped_products:
    print(f"\nName: {product['Name']}")
    print(f"Price: {product.get('Price')}")  # Print only if available
    print(f"Image URL: {product.get('Image URL')}")  # Print only if available
else:
  print("No products found or error occurred during scraping.")


# # solution 5

# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_cnbc_news(url):
  """Scrapes news headlines, dates, and links from the given CNBC URL.

  Args:
      url (str): The URL of the CNBC news page to scrape.

  Returns:
      list: A list of dictionaries, each containing scraped news details.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'lxml')

    # Find all news items (adjust selectors as needed)
    news_items = soup.find_all('div', class_='LatestNews-item')

    scraped_news = []
    for item in news_items:
      news_data = {}

      # Extract heading
      heading_tag = item.find('a', class_='LatestNews-headline')
      news_data['Heading'] = heading_tag.text.strip() if heading_tag else None

      # Extract date (assuming date is within the 'LatestNews-vignette' span)
      date_tag = item.find('span', class_='LatestNews-vignette')
      news_data['Date'] = date_tag.text.strip() if date_tag else None

      # Extract news link
      news_link = heading_tag.get('href') if heading_tag else None
      news_data['News Link'] = f"https://www.cnbc.com{news_link}" if news_link else None

      scraped_news.append(news_data)

    return scraped_news

  except requests.exceptions.RequestException as e:
    print(f"Error scraping news from {url}: {e}")
    return []

# Base URL for CNBC's World News
base_url = "https://www.cnbc.com/world/?region=world"

# Scrape news data
scraped_news = scrape_cnbc_news(base_url)

if scraped_news:
  print("Scraped News Headings, Dates, and Links:")
  for news in scraped_news:
    print(f"\nHeading: {news['Heading']}")
    print(f"Date: {news['Date']}")
    print(f"News Link: {news['News Link']}")
else:
  print("No news found or error occurred during scraping.")


# # solution 6

# In[ ]:


import requests
from bs4 import BeautifulSoup

def scrape_keai_articles(url):
  """Scrapes paper details from the given KAI article list URL.

  Args:
      url (str): The URL of the KAI article list to scrape.

  Returns:
      list: A list of dictionaries, each containing scraped paper details.
  """

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes

    soup = BeautifulSoup(response.content, 'lxml')

    # Find all article elements (adjust selector as needed)
    articles = soup.find_all('li', class_='most-downloaded-article-item')

    scraped_articles = []
    for article in articles:
      article_data = {}

      # Extract paper title
      title_tag = article.find('a', class_='most-downloaded-article-title__link')
      article_data['Paper Title'] = title_tag.text.strip() if title_tag else None

      # Extract date (likely within the 'most-downloaded-article-item__date' span)
      date_tag = article.find('span', class_='most-downloaded-article-item__date')
      article_data['Date'] = date_tag.text.strip() if date_tag else None

      # Extract authors (heuristics: assuming within a 'a' tag with specific URL structure)
      all_authors = []
      for author_link in article.find_all('a', href=lambda href: href and href.startswith('/en/authors/')):
        all_authors.append(author_link.text.strip())
      article_data['Authors'] = ', '.join(all_authors) if all_authors else None

      scraped_articles.append(article_data)

    return scraped_articles

  except requests.exceptions.RequestException as e:
    print(f"Error scraping articles from {url}: {e}")
    return []

# Base URL for KAI most downloaded articles
base_url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/"

# Scrape article data
scraped_articles = scrape_keai_articles(base_url)

if scraped_articles:
  print("Scraped Article Details - Paper Title, Date, Authors:")
  for article in scraped_articles:
    print(f"\nPaper Title: {article['Paper Title']}")
    print(f"Date: {article.get('Date')}")  # Print only if available
    print(f"Authors: {article.get('Authors')}")  # Print only if available
else:
  print("No articles found or error occurred during scraping.")


# In[ ]:




