# Documentation

### Setup
**As mentioned in the [README](README.md) file:**
As of now, the project is not available as a standalone library. To use this product currently, you can **download the script** and import it into any other Python scripts you wish to use using:
```sh
from fbscraper import Scraper, StatStrings
```
Once the script has been imported, you are ready to start using it.
Create an object of the ```Scraper``` class, and choose a league for the ```league``` argument.
The available leagues are available on a multi-line comment in the first few lines of the ```Scraper``` class. Check the script out [here](fbscraper.py).
Here is an example using the English Premier League:
```sh
scraper = Scraper("england")
```
You can now use league-specific methods and they will return Premier League data. As of now, non-league-specific methods must also be called from this object.

### Methods
Below is the documentation for every method currently found in the script.

---
##### ```Scraper.getLeagueLeaders(self, stat_id)```
***Returns a list containing league leader(s) in the category specified by*** **```stat_id```, as well as the value of the statistic.**
This method is the only method which makes use of the variables present in the ```StatStrings``` class.
The ```stat_id``` argument determines the category whose leaders the method will return.
The method returns a list. The first values of the list are string(s) with the leader(s) within the ```stat_id``` category. The last value of the list is the value of the statistic.
The available variables for ```stat_id``` can be seen in the ```StatString``` class. They are:
| Category | Variable name | String represented |
|----------|---------------|----------------------|
| Sub appearances | sub_appearances | "leaders_games_subs" |
| PPG (Points per game) | points_per_game | "leaders_points_per_game" |
| Plus-minus | plus_minus | "leaders_plus_minus" |
| Plus-minus per-90 | plus_minus_per_90 | "leaders_plus_minus_per90" |
| xG plus-minus| xg_plus_minus | "leaders_xg_plus_minus" |
| xG plus-minus per-90| xg_plus_minus_per_90 | "leaders_xg_plus_minus_per90" |
| Yellow Cards | yellow_cards | "leaders_cards_yellow" |
| Red Cards | red_cards | "leaders_cards_red" |
| Aerials won | aerials_won | "leaders_aerials_won" |
| Aerials won %| aerials_won_percent | "leaders_aerials_won_pct" |
| Fouls commited | fouls_commited | "leaders_fouls" |
| Fouls drawn | fouls_drawn | "leaders_fouled" |
| Own goals | own_goals | "leaders_own_goals" |
| Clean sheets | clean_sheets | "leaders_gk_clean_sheets" |
| Clean sheets % | clean_sheets_percent | "leaders_gk_clean_sheets_pct" |
| Saves | saves | "leaders_gk_saves" |
| Save percentage | save_percentage | "leaders_gk_save_pct" |
| Goals against per-90 | goals_against_per_90 | "leaders_gk_goals_against_per90" |
| Post-shot xG - G/A comparision |  psxg_ga_comparision | "leaders_gk_psxg_net" |
| Post-shot xG G/A comparision per-90| psxg_ga_comparision_per_90 | "leaders_gk_psxg_net_per90" |

**Example**
```sh
from fbscraper import Scraper, StatStrings
scraper = Scraper("england")
print(scraper.getLeagueLeaders(StatStrings.own_goals))
```
**Output**
```sh
['Craig Dawson', 'Marc Guéhi', 2.0]
```
---
#### ```Scraper.getTeams(self)```
***Returns a list containing strings of all the names of the teams in the league, in alphabetical order.***
A straightforward method. Returns a list containing every team present in the league represented by the ```league``` argument of  ```Scraper```.

**Example**
```sh
from fbscraper import Scraper, StatStrings
scraper = Scraper("france")
print(scraper.getTeams())
```
**Output**
```sh
['Angers', 'Auxerre', 'Brest', 'Le Havre', 'Lens', 'Lille', 'Lyon', 'Marseille', 'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Paris S-G', 'Reims', 'Rennes', 'Saint-Étienne', 'Strasbourg', 'Toulouse']
```
---
#### ```Scraper.getLeagueTable(self)```
***Returns a pandas dataframe of the league table.***
Reads the current league table of the league represented by the ```league``` argument of ```Scraper```.

**Example**
```sh
from fbscraper import Scraper, StatStrings
scraper = Scraper("germany")
print(scraper.getLeagueTable().to_string())
```

**Output**
```sh
    Rk           Squad  MP   W  D   L  GF  GA  GD  Pts  Pts/MP    xG   xGA   xGD  xGD/90     Last 5  Attendance                              Top Team Scorer         Goalkeeper  Notes
0    1   Bayern Munich  15  11  3   1  47  13  34   36    2.40  34.5   9.6  25.0    1.67  W D W L W       75000                              Harry Kane - 14       Manuel Neuer    NaN
1    2      Leverkusen  15   9  5   1  37  21  16   32    2.13  28.5  16.6  11.9    0.80  W W W W W       29877                            Patrik Schick - 9     Lukáš Hrádecký    NaN
2    3  Eint Frankfurt  15   8  3   4  35  23  12   27    1.80  29.3  22.9   6.4    0.43  W W D L L       57729                           Omar Marmoush - 13        Kevin Trapp    NaN
3    4      RB Leipzig  15   8  3   4  24  20   4   27    1.80  20.6  22.0  -1.5   -0.10  L L W W L       44258              Loïs Openda, Benjamin Šeško - 6      Péter Gulácsi    NaN
4    5        Mainz 05  15   7  4   4  28  20   8   25    1.67  20.7  20.8  -0.1   -0.01  W W L W W       31851                       Jonathan Burkardt - 10      Robin Zentner    NaN
5    6        Dortmund  15   7  4   4  28  22   6   25    1.67  22.6  19.3   3.3    0.22  W D D D W       81365                          Serhou Guirassy - 6       Gregor Kobel    NaN
6    7   Werder Bremen  15   7  4   4  26  25   1   25    1.67  20.1  20.3  -0.2   -0.01  L D W W W       41950                               Jens Stage - 7   Michael Zetterer    NaN
7    8        Gladbach  15   7  3   5  25  20   5   24    1.60  25.0  24.5   0.4    0.03  W L D W W       53062                          Tim Kleindienst - 9     Moritz Nicolas    NaN
8    9        Freiburg  15   7  3   5  21  24  -3   24    1.60  21.6  18.0   3.6    0.24  L W D W L       34100                               Ritsu Doan - 5       Noah Atubolu    NaN
9   10       Stuttgart  15   6  5   4  29  25   4   23    1.53  28.2  22.6   5.6    0.38  W D W W L       59250                        Ermedin Demirović - 7    Alexander Nübel    NaN
10  11       Wolfsburg  15   6  3   6  32  28   4   21    1.40  21.7  26.0  -4.2   -0.28  W W W L L       25975                               Jonas Wind - 6      Kamil Grabara    NaN
11  12    Union Berlin  15   4  5   6  14  19  -5   17    1.13  15.8  18.7  -3.0   -0.20  L L L D L       21976                      Benedict Hollerbach - 3    Frederik Rønnow    NaN
12  13        Augsburg  15   4  4   7  17  32 -15   16    1.07  16.4  21.2  -4.8   -0.32  L W D L L       29723                            Phillip Tietz - 5  Nediljko Labrović    NaN
13  14       St. Pauli  15   4  2   9  12  19  -7   14    0.93  15.2  20.5  -5.3   -0.35  L W L L W       29448  Johannes Eggestein, Oladapo Afolayan... - 2      Nikola Vasilj    NaN
14  15      Hoffenheim  15   3  5   7  20  28  -8   14    0.93  20.6  25.6  -5.1   -0.34  W L D D L       24891                          Andrej Kramarić - 6     Oliver Baumann    NaN
15  16      Heidenheim  15   3  1  11  18  33 -15   10    0.67  20.5  26.0  -5.4   -0.36  L L L L L       15000                         Marvin Pieringer - 4       Kevin Müller    NaN
16  17   Holstein Kiel  15   2  2  11  19  38 -19    8    0.53  16.2  27.6 -11.4   -0.76  L L L L W       14874                            Shuto Machino - 6       Timon Weiner    NaN
17  18          Bochum  15   1  3  11  13  35 -22    6    0.40  16.7  32.1 -15.4   -1.03  L L L D W       25565                               Matúš Bero - 3     Patrick Drewes    NaN
```
---
Will add rest of methods at later date.
