# FBRef Stats Documentation

### Setup

**As mentioned in the [README](README.md) file:**
To install this project, input the following into the command line:
```sh
pip install fbrefstats
```
From there, you can import the package into your program using:

```sh
from fbrefstats import LeagueScraper, GeneralScraper, StatStrings
```


Once the script has been imported, you are ready to start using it.
Create an object of the ```LeagueScraper``` class, and choose a league for the ```league``` argument. \
The available leagues are available on a multi-line comment in the first few lines of the ```LeagueScraper``` class. \
Currently, they are:
| Country | League name | LeagueScraper Object Argument |
|----------|---------------|----------------------|
| England | Premier League | "england" |
| France | Ligue 1 | "france" |
| Germany | Bundesliga | "germany" |
| Spain | LaLiga | "spain" |
| Italy | Serie A | "italy" |
| Netherlands | Eredivisie | "netherlands" |
| Portugal | Primeira Liga | "portugal" |
| Hungary | Nemzeti Bajnokság I | "hungary" |
| Russia | Russian Premier League | "russia" |


Check the script out [here](fbrefstats.py).

Here is an example using the English Premier League:
```sh
scraper = LeagueScraper("england")
```
You can now use league-specific methods and they will return Premier League data. \
Non-league-specific methods are part of the ```GeneralScraper``` class. To use them, simply call them using ```GeneralScraper.method()```

### Methods

Below is the documentation for every method currently found in the script.

---
<details>
<summary>
    <h4><code>LeagueScraper.getLeagueLeaders(self, stat_id)</code></h4>
</summary>

***Returns a list containing league leader(s) in the category specified by*** **```stat_id```, as well as the value of the statistic.**\
This method is the only method which makes use of the variables present in the ```StatStrings``` class.\
The ```stat_id``` argument determines the category whose leaders the method will return.\
The method returns a list. The first values of the list are string(s) with the leader(s) within the ```stat_id``` category. The last value of the list is the value of the statistic.
The available variables for ```stat_id``` can be seen in the ```StatString``` class. They are:
| Category | Variable name | String represented |
|----------|---------------|----------------------|
| Substitute appearances | sub_appearances | "leaders_games_subs" |
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
from fbrefstats import LeagueScraper, StatStrings
scraper = LeagueScraper("england")
print(scraper.getLeagueLeaders(StatStrings.own_goals))
```
**Output**
```sh
['Craig Dawson', 'Marc Guéhi', 2.0]
```
</details>

---

<details>
<summary>
    <h4><code>LeagueScraper.getTeams(self)</code></h4>
</summary>

***Returns a list containing strings of all the names of the teams in the league, in alphabetical order.***\
A straightforward method. Returns a list containing every team present in the league represented by the ```league``` argument of  ```LeagueScraper```.

**Example**
```sh
from fbrefstats import LeagueScraper
scraper = LeagueScraper("france")
print(scraper.getTeams())
```
**Output**
```sh
['Angers', 'Auxerre', 'Brest', 'Le Havre', 'Lens', 'Lille', 'Lyon', 'Marseille', 'Monaco', 'Montpellier', 'Nantes', 'Nice', 'Paris S-G', 'Reims', 'Rennes', 'Saint-Étienne', 'Strasbourg', 'Toulouse']
```
</details>

---

<details>
<summary>
    <h4><code>LeagueScraper.getLeagueTable(self)</code></h4>
</summary>

***Returns a pandas dataframe of the league table.***\
Reads the current league table of the league represented by the ```league``` argument of ```LeagueScraper```.

**Example**
```sh
from fbrefstats import LeagueScraper
scraper = LeagueScraper("germany")
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
</details>

---

<details>
<summary>
    <h4><code>LeagueScraper.getSquadStats(self)</code></h4>
</summary>

***Returns a pandas dataframe of the league's squad stats.***\
Straightforward. Returns the squad stats table of the league specified in the ```league``` argument of the ```LeagueScraper``` object in the form of a pandas dataframe.

**Example**
```sh
from fbrefstats import LeagueScraper
scraper = LeagueScraper("italy")
print(scraper.getSquadStats().to_string())
```

**Output**
```sh

```   Unnamed: 0_level_0 Unnamed: 1_level_0 Unnamed: 2_level_0 Unnamed: 3_level_0 Playing Time                    Performance                                 Expected                      Progression      Per 90 Minutes                                                           
                Squad               # Pl                Age               Poss           MP Starts   Min   90s         Gls Ast G+A G-PK PK PKatt CrdY CrdR       xG  npxG   xAG npxG+xAG        PrgC PrgP            Gls   Ast   G+A  G-PK G+A-PK    xG   xAG xG+xAG  npxG npxG+xAG
0            Atalanta                 28               27.3               56.4           18    187  1620  18.0          42  30  72   39  3     4   32    0     33.5  30.4  24.4     54.8         410  892           2.33  1.67  4.00  2.17   3.83  1.86  1.35   3.22  1.69     3.04
1             Bologna                 27               26.8               57.1           17    187  1530  17.0          25  17  42   22  3     4   29    3     22.0  18.9  13.8     32.7         283  687           1.47  1.00  2.47  1.29   2.29  1.30  0.81   2.11  1.11     1.92
2            Cagliari                 24               27.3               47.4           18    198  1620  18.0          15  10  25   12  3     3   37    3     24.4  22.0  16.6     38.6         260  584           0.83  0.56  1.39  0.67   1.22  1.35  0.92   2.27  1.22     2.14
3                Como                 29               27.8               54.0           18    198  1620  18.0          17  14  31   17  0     2   40    2     20.6  19.1  15.8     34.9         319  640           0.94  0.78  1.72  0.94   1.72  1.14  0.88   2.02  1.06     1.94
4              Empoli                 25               25.8               40.3           18    198  1620  18.0          16   9  25   14  2     3   35    1     13.9  11.5   8.6     20.1         218  460           0.89  0.50  1.39  0.78   1.28  0.77  0.48   1.25  0.64     1.12
5          Fiorentina                 27               26.6               52.1           17    187  1530  17.0          30  20  50   26  4     5   34    1     24.4  20.4  17.0     37.4         316  601           1.76  1.18  2.94  1.53   2.71  1.43  1.00   2.43  1.20     2.20
6               Genoa                 31               27.1               42.8           18    198  1620  18.0          15   9  24   15  0     1   41    0     18.0  17.0  12.2     29.3         214  471           0.83  0.50  1.33  0.83   1.33  1.00  0.68   1.68  0.95     1.63
7       Hellas Verona                 27               25.8               39.2           18    198  1620  18.0          22  16  38   20  2     2   51    5     17.7  16.2  13.5     29.7         227  505           1.22  0.89  2.11  1.11   2.00  0.99  0.75   1.74  0.90     1.65
8               Inter                 23               30.0               60.1           17    187  1530  17.0          44  33  77   39  5     6   26    0     33.3  28.9  22.8     51.7         276  791           2.59  1.94  4.53  2.29   4.24  1.96  1.34   3.30  1.70     3.04
9            Juventus                 25               25.2               60.4           18    198  1620  18.0          28  19  47   24  4     4   37    1     26.0  22.9  18.1     41.0         443  737           1.56  1.06  2.61  1.33   2.39  1.44  1.01   2.45  1.27     2.28
10              Lazio                 23               27.8               53.7           18    187  1620  18.0          32  20  52   28  4     5   43    2     29.1  25.4  17.3     42.7         355  764           1.78  1.11  2.89  1.56   2.67  1.61  0.96   2.57  1.41     2.37
11              Lecce                 25               26.5               42.4           18    198  1620  18.0          11   8  19   10  1     2   32    4     18.2  16.6  13.1     29.7         239  479           0.61  0.44  1.06  0.56   1.00  1.01  0.73   1.74  0.92     1.65
12              Milan                 27               26.2               54.4           17    187  1530  17.0          26  18  44   24  2     4   28    3     28.1  25.0  19.8     44.8         399  724           1.53  1.06  2.59  1.41   2.47  1.65  1.17   2.82  1.47     2.63
13              Monza                 26               27.5               48.6           18    198  1620  18.0          15  10  25   14  1     1   49    2     15.7  15.0  10.8     25.7         257  503           0.83  0.56  1.39  0.78   1.33  0.87  0.60   1.47  0.83     1.43
14             Napoli                 23               28.7               53.1           18    198  1620  18.0          26  21  47   24  2     3   21    0     26.6  24.3  21.0     45.4         368  779           1.44  1.17  2.61  1.33   2.50  1.48  1.17   2.64  1.35     2.52
15              Parma                 27               24.3               44.6           18    198  1620  18.0          24  18  42   21  3     4   33    4     22.8  19.6  15.1     34.8         323  528           1.33  1.00  2.33  1.17   2.17  1.27  0.84   2.11  1.09     1.93
16               Roma                 24               27.0               57.8           18    198  1620  18.0          24  15  39   21  3     3   35    1     25.4  23.1  18.0     41.1         357  747           1.33  0.83  2.17  1.17   2.00  1.41  1.00   2.42  1.28     2.28
17             Torino                 25               27.3               48.2           18    198  1620  18.0          18  12  30   17  1     2   39    1     16.9  15.4  10.2     25.5         235  540           1.00  0.67  1.67  0.94   1.61  0.94  0.57   1.50  0.85     1.42
18            Udinese                 26               27.1               45.1           18    198  1620  18.0          23  17  40   23  0     2   44    3     16.4  14.7  11.6     26.3         258  537           1.28  0.94  2.22  1.28   2.22  0.91  0.64   1.55  0.82     1.46
19            Venezia                 28               26.2               43.6           18    198  1620  18.0          17  11  28   15  2     3   32    1     17.3  15.0  10.8     25.8         250  500           0.94  0.61  1.56  0.83   1.44  0.96  0.60   1.56  0.84     1.43
```
</details>

---

<details>
<summary>
    <h4><code>GeneralScraper.getPlayerLink(self, inputted_player_name)</code></h4>
</summary>

***Returns a list with the stats page for the player inputted. If more than one player has that name, it will return all their links in a list.***\
This **static** method searches the string provided in the ```inputted_player_name``` argument on the FBRef database, and returns a list with the URLs found after the search.

**Example 1**
```sh
from fbrefstats import GeneralScraper

print(GeneralScraper.getPlayerLink("Riyad Mahrez"))
```

**Output 1**
```sh
['https://fbref.com/en/players/892d5bb1/Riyad-Mahrez']
```

**Example 2**
```sh
from fbrefstats import GeneralScraper

print(GeneralScraper.getPlayerLink("Ndombele"))
```

---
**Output 2**
```sh
['https://fbref.com/en/players/95099e9a/Gradi-Ndombele', 'https://fbref.com/en/players/fc5b61a3/Bosso-Alvaro', 'https://fbref.com/en/players/5cdddffa/Tanguy-Ndombele']
```
</details>

---

<details>
<summary>
    <h4><code>GeneralScraper.getPlayerPosition(player_link)</code></h4>
</summary>

***Returns a string containing the position of the player associated with the URL of player_link***\
This **static** method returns a string containing the position details of a player whose FBRef URL contains position data.

**Example 1**
```sh
from fbrefstats import GeneralScraper

vardy_url = GeneralScraper.getPlayerLink("Jamie Vardy")[0]
# Must specify [0] because GeneralScraper.getPlayerLink() returns a list,
# even if there is only one URL associated with the player namae

print(GeneralScraper.getPlayerPosition(vardy_url))
```

**Output 1**
```sh
FW
```

**Example 2**
```sh
from fbrefstats import GeneralScraper

frimpong_url = GeneralScraper.getPlayerLink("Jeremie Frimpong")[0]
print(GeneralScraper.getPlayerPosition(frimpong_url))
```

**Output 1**
```sh
DF-MF (DM-FB, right)
```

If the data is not found, the method will return a string containing the value ```N/A```

</details>

---

<details>
<summary>
    <h4><code>GeneralScraper.getPlayerFootedness(player_link)</code></h4>
</summary>

***Returns a string containing the footedness of the player associated with the URL of player_link***\
This **static** method returns a string containing the footedness (left/right footed) of a player whose FBRef URL contains the corresponding data.

**Example 1**
```sh
from fbrefstats import GeneralScraper

johnson_url = GeneralScraper.getPlayerLink("Sean Johnson")[0]
# Must specify [0] because GeneralScraper.getPlayerLink() returns a list,
# even if there is only one URL associated with the player namae

print(GeneralScraper.getPlayerFootedness(johnson_url))
```

**Output 1**
```sh
Right
```

**Example 2**
```sh
from fbrefstats import GeneralScraper

messi_url = GeneralScraper.getPlayerLink("Lionel Messi")[0]
print(GeneralScraper.getPlayerFootedness(messi_url))
```

**Output 1**
```sh
Left
```

If the data is not found, the method will return a string containing the value ```N/A```

**Error Example**
```sh
from fbrefstats import GeneralScraper

altobelli_url = GeneralScraper.getPlayerLink("Julian Altobelli")[0]
# Julian Altobelli is (as of January 11th, 2025)
# a 22 year-old Toronto FC II player. 

print(GeneralScraper.getPlayerFootedness(altobelli_url))
```

**Error Output**
```sh
N/A
```

</details>

</details>
