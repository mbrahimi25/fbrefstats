import requests
from bs4 import BeautifulSoup
import pandas as pd

session = requests.session()

prem_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
laliga_url = "https://fbref.com/en/comps/12/La-Liga-Stats"
bundesliga_url = "https://fbref.com/en/comps/20/Bundesliga-Stats"
seriea_url = "https://fbref.com/en/comps/11/Serie-A-Stats"
ligue1_url = "https://fbref.com/en/comps/13/Ligue-1-Stats"
eredivisie_url = "https://fbref.com/en/comps/23/Eredivisie-Stats"
primeiraliga_url = "https://fbref.com/en/comps/32/Primeira-Liga-Stats"
# FBRef URLs for different leagues 


# Headers to mimic a standard web browser
headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

class StatStrings:
  """
  Class with strings for each statistic where leaders are available
  """
  goals = "leaders_goals"
  goals_per_90 = "leaders_goals_per90"
  assists = "leaders_assists"
  assists_per_90 = "leaders_assists_per90"
  ga = "leaders_goals_assists"
  ga_per_90 = "leaders_goals_assists_per90"
  pens_created = "leaders_pens_made"
  non_pen_goals = "leaders_goals_pens"
  non_pen_goals_per90 = "leaders_goals_pens_per90"
  non_pen_ga_per90 = "leaders_goals_assists_pens_per90"
  xg = "leaders_xg"
  xg_per_90 = "leaders_xg_per90"
  non_pen_xg = "leaders_npxg"
  non_pen_xg_per_90 = "leaders_npxg_per90"
  xag = "leaders_xg_assist"
  xag_per_90 = "leaders_xg_assist_per90"
  shots = "leaders_shots"
  shots_per_90 = "leaders_shots_per90"
  shots_on_target = "leaders_shots_on_target"
  shots_on_target_per_90 = "leaders_shots_on_target_per90"
  shots_on_target_percent = "leaders_shots_on_target_pct"
  goals_per_shot = "leaders_goals_per_shot"
  goals_per_shot_on_target = "leaders_goals_per_shot_on_target"
  non_pen_xg_per_shot = "leaders_npxg_per_shot"
  goals_xg_comparision = "leaders_xg_net"
  non_pen_goals_npxg_comparision = "leaders_npxg_net"
  key_passes = "leaders_assisted_shots"
  pass_completion_percent = "leaders_passes_pct"
  progressive_passing_distance = "leaders_passes_progressive_distance"
  passes_into_final_third = "leaders_passes_into_final_third"
  passes_into_penalty_area = "leaders_passes_into_penalty_area"
  crosses_into_penalty_area = "leaders_crosses_into_penalty_area"
  progressive_passes = "leaders_progressive_passes"
  through_balls = "leaders_through_balls"
  xa = "leaders_pass_xa"
  xa_per_90 = "leaders_pass_xa_per90"
  corners = "leaders_corner_kicks"
  crosses = "leaders_crosses"
  throw_ins = "leaders_throw_ins"
  shot_creating_actions = "leaders_sca"
  shot_creating_actions_per_90 = "leaders_sca_per90"
  goal_creating_actions = "leaders_gca"
  goal_creating_actions_per_90 = "leaders_gca_per90"
  tackles = "leaders_tackles"
  tackles_won = "leaders_tackles_won"
  dribblers_tackled = "leaders_challenge_tackles"
  dribblers_tackled_percent = "leaders_challenge_tackles_pct"
  blocks = "leaders_blocks"
  interceptions = "leaders_interceptions"
  clearances = "leaders_clearances"
  touches = "leaders_touches"
  successful_take_ons = "leaders_take_ons_won"
  successful_take_ons_percent = "leaders_take_ons_won_pct"
  progressive_carrying_distance = "leaders_carries_progressive_distance"
  progressive_carries = "leaders_progressive_carries"
  carries_into_penalty_area = "leaders_carries_into_penalty_area"
  progressive_passes_recieved = "leaders_progressive_passes_recieved"
  
  minutes = "leaders_minutes" ####### Special case as usually many players have equal minutes
  
  sub_appearances = "leaders_games_subs"
  points_per_game = "leaders_points_per_game"
  plus_minus = "leaders_plus_minus"
  plus_minus_per_90 = "leaders_plus_minus_per90"
  xg_plus_minus = "leaders_xg_plus_minus"
  xg_plus_minus_per_90 = "leaders_xg_plus_minus_per90"
  yellow_cards = "leaders_cards_yellow"
  red_cards = "leaders_cards_red"
  aerials_won = "leaders_aerials_won"
  aerials_won_percent = "leaders_aerials_won_pct"
  fouls_commited = "leaders_fouls"
  fouls_drawn = "leaders_fouled"
  own_goals = "leaders_own_goals"
  clean_sheets = "leaders_gk_clean_sheets"
  clean_sheets_percent = "leaders_gk_clean_sheets_pct"
  saves = "leaders_gk_saves"
  save_percentage = "leaders_gk_save_pct"
  goals_against_per_90 = "leaders_gk_goals_against_per90"
  psxg_ga_comparision = "leaders_gk_psxg_net"
  psxg_ga_comparision_per_90 = "leaders_gk_psxg_net_per90"
  

class Scraper:
  """
  A class for scraping data from different leagues on FBRef
  Instantiate a Scraper by passing the country name of the league you wish to scrape into the 'league' argument. Available leagues include:
  * 'england' (Premier League)
  * 'france' (Ligue 1)
  * 'germany' (Bundesliga)
  * 'spain' (La Liga)
  * 'italy' (Serie A)
  * 'netherlands' (Eredivisie)
  * 'portugal' (Primeira Liga)
  """
  
  def __init__(self, league):
    self.league = league
    match league:
      case "england":
        self.url = prem_url
      case "france":
        self.url = ligue1_url
      case "germany":
        self.url = bundesliga_url
      case "italy":
        self.url = seriea_url
      case "spain":
        self.url = laliga_url
      case "netherlands":
        self.url = eredivisie_url
      case "portugal":
        self.url = primeiraliga_url
      case other:
        raise ValueError(f"Invalid league: {league}")
    # switch/case statement assigning the different league urls to the self.url variable in order to be read by BeautifulSoup
    
    response = session.get(self.url, headers=headers)
    # gets the raw HTML from self.url

    splitter = '<!-- 	<div class="data_grid" id="div_leaders" data-entry-type="Leaderboards">'
    # splits the raw HTML after a specific comment so that the code can read a commented-out section which includes league leaders in different stats
    #print(splitter in response.text)
    leader_tables_html = response.text.split(splitter)[1]
    # this variable stores the second part of the splitted text so BeautifulSoup doesn't see that it's a comment

    # two BeautifulSoup objects. self.soup for the main tables, and self.leaders_soup for the league leaders in different stats
    self.soup = BeautifulSoup(response.text, "html.parser")
    self.leaders_soup = BeautifulSoup(leader_tables_html, "html.parser")


  def getLeagueLeaders(self, stat_id):
    if (stat_id == StatStrings.minutes): # Minute leaders
      playerRows = self.leaders_soup.find("div", id=stat_id).findAll("tr") # Returns all the rows

      highestMinutes = playerRows[0].find("td", {"class":"value"}).text.split(" ")[1]
      # Gets the minute value of the first row in the table

      leaders = [] # Creates the leaders list to return to the user
      
      for i in playerRows: # Loops through all the rows
        if i.find("td", {"class": "value"}).text == " " + highestMinutes:
          leaders.append(i.find("td", {"class": "who"}).find("a").text)

        # if the current row's minute value is the same as highestMinutes:
        # append the player name to the leaders list

      leaders.append(int(highestMinutes))
      
    else: # Any stat other than minutes
      firstPlacePlayersRows = self.leaders_soup.find("div", id=stat_id).findAll("tr",{"class":"first_place"})
      # Scrapes the table rows with the class "first_place" (as there may be more than one)
      leaders = [i.find("td", {"class":"who"}).find("a").text for i in firstPlacePlayersRows]
      # Scrapes the player names from each entry in firstPlacePlayers
      leaderValue = float(firstPlacePlayersRows[0].find("td", {"class": "value"}).text)
      # Scrapes the amount of of the stat value by the top keeper(s)
      leaders.append(leaderValue)
      # Appends the leaderValue to leaders[] so that it can be returned to the user

    return leaders
 
  def getTeams(self):
    """
    Returns a list containing strings of all the names of the teams in the league, in alphabetical order
    """
    table = self.soup.findAll('table')[2]
    league_rows = table.find('tbody').findAll('tr')
    teams = [team.find('th', {'data-stat':'team'}).find('a').text for team in league_rows]

    return teams

  def getLeagueTable(self):
    """
    Returns a pandas dataframe of the league table
    """
    
    league_table = self.soup.findAll('table')[0]
    table = pd.read_html(str(league_table))[0]
    return table

  def getSquadStats(self):
    """
    Returns a pandas dataframe of the squad stats
    """

    squad_stats = self.soup.findAll('table')[2]
    table = pd.read_html(str(squad_stats))[0]
    return table

  def getPlayerLink(self, inputted_player_name):
    """
    Returns the stats page for the player inputted.
    If more than one player has that name, it will return all their links in a list.
    The optional 'nationality' argument is to input a nation's 3 letter abbreviation so only players from that nation are returned by the function.
    /// ADD FUNCTIONALITY FOR THIS ^^^^^
    """
    returned_players = []
    
    player_name_list = inputted_player_name.split(" ")

    searchbar_link = "https://fbref.com/en/search/search.fcgi?search="
    for i in player_name_list:
        searchbar_link += i + "+"
    # This is the search URL that will be scraped to find the player page
    
    search_html = session.get(searchbar_link, headers=headers)
    search_soup = BeautifulSoup(search_html.text, "html.parser")
    # returns HTML of the search bar page
    try:
      search_h3 = search_soup.find('h3').text
      # The first h3 tag on the website
    except:
      raise ValueError("Input unable to be processed") from None

    if (search_h3 == "About FBref.com"):
      # The player has been found and we're on his page. Now we need the URL
      player_link = "https://fbref.com" + search_soup.find('div', {'id': 'bottom_nav_container'}).find('a')['href']
      # Finds a div (id: bottom_nav_container) and finds the first link inside it, which contains a link back to the same page we're on (for some reason). We can use this to find the URL of our player and return it in our function
      returned_players.append(player_link)
    
    elif (search_h3 == 'Players from Leagues Covered by FBref.'):
      # If the search returns more than one player
      player_divs = search_soup.findAll('div', {'class': 'search-item-name'})
      # finds all the players
      for i in player_divs:
        returned_players.append("https://fbref.com" + i.find('a')['href'])

    else:
      print("Input unable to be processed")
    
    return returned_players