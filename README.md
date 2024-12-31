# FBScrape
### A python script to scrape football data from [FBRef]

![Static Badge](https://img.shields.io/badge/License-GNU-red) ![Static Badge](https://img.shields.io/badge/Python-yellow)

### About
FBScrape is a Python script which uses *BeautifulSoup* and *requests* to scrape data from [FBRef].
This is a small side project I work on in my free time. As an avid soccer fan and someone who finds sports stats interesting, I tried making a program which takes player stats into account so I could gain an advantage on my fantasy leagues with my friends. However, I could not find many good free libraries which provided soccer data, so I resolved to build one myself.


### Installation
As of now, the project is not available as a standalone library. To use this product currently, you can **download the script** and import it into any other Python scripts you wish to use using:
```sh
from fbscraper import Scraper, StatStrings
```

### Usage
As seen above, there are two classes within the ```fbscraper``` script:
(The names of these classes may change in the future, they are currently placeholders)
- ```Scraper```
- ```StatStrings```

The ```Scraper``` class contains the actual scraping code. ```StatStrings``` is a class full of variables holding strings, and are used when calling the method ```Scraper.getLeagueLeaders()```.

**Check out the [documentation](DOCUMENTATION.md) for info on how to use the script.**

### To-do
As of right now, this script is still in a very early development phase, and I am only working on it as a personal side project. I have a few things I am thinking of adding:

- **Update ```README.md``` (Urgent)** ☑
- **Add a documentation file** ☑

- **Turn *FBScrape* into a library** ☐\
I have never made an actual library before, so I would like to research how to turn this into a real installable Python library.

- **More scraping!** ☐\
There is so much data available on [FBRef], so I would love to add more methods so that this data can be accessed through the script

- **Add support for different league formats** ☐\
As of right now, there are very few leagues supported (currently the English, French, German, Spanish, Italian, Dutch, and Portuguese top flights) as I am yet to add functionality to leagues with different formats (promotion/relegation playoffs, MLS post-season, or Apertura/Clausura formats commonly found in Latin America)

- **Different table formats** ☐\
As of now, methods which return tables (such as ```Scraper.getLeagueTable()```) return a *pandas* dataframe. While this is ok, I could also add support to return as a CSV file, or to print the table directly into the console

- **Add nationality argument to ```Scraper.getPlayerLink()```** ☐\
Currently, ```Scraper.getPlayerLink()``` takes one argument: ```inputted_player_name```. The method returns a list of URLs depending on which players were found when searching with ```inputted_player_name```. This can get annoying when there are many players with similar names, so adding a *nationality* argument would be useful for searching.

- **Static functions** ☐\
Research making some methods static (like ```Scraper.getPlayerLink()```) as they do not tie in specifically to one league. It does not make sense to have a ```Scraper``` object which can be used to get English league stats, but have to call a method from that object to search for players anywhere around the world.

### License
GNU GPL

[FBRef]: <https://fbref.com>
