<h1 align="center">Stellar Coffee</h1>
<img src="./docs/StellarCoffee2.png"> 
<h2 align="center">Our Data Structure Course's Final Project</h2>
</br>

# Ethymologies
### Stellar literally derived from Latin "Stella" which means star, in English referring "something that exceptionally perfect", 
### While Coffee referring "a godly substance which can enhance a programmer by an exceptionally amount"

# What is this?
This is a digital object called "Za Programs" which tries to mimic a Cafe

# Wait again? Why Though
The last time was an [CLI Program](https://github.com/nmluci/KisatenSim), while this one is a proper Human-friendly program in a form of something called "Website"

# What This Program Actually DO?
## Simping a coffee. (again)
Jokes aside, Its simulate an digital ordering system on a coffee shop backed by an REST API

# Functionalities
Tell me more about this program? Fine.

It's actually consist of 2 Core Part, [FrontEnd](https://github.com/kompiangg/StellarCoffeeFE) and [BackEnd](https://github.com/nmluci/StellarCoffee) 


| Frontend Stuff        | Backend Stuff                    |
------------------------|-----------------------------------
| Homepage              | User Authenticaton System        |
| Menu Page             | Order Logging System             |
| User Leaderboard Page | Today Specials Generation System |
| Special Menu Page     | User Leaderboard Ranking System  |
| User Login Page       | Rest API + Auth + CORS           |

[Click Here For More In-depth Stuff Documentation (and cooler style)](./docs/modulesBreakdown.md)

# Implemented Concepts
- Modularity (Obviously)
- Database Management
- Hashing
- Linear Searching
- Quick Sorting
- Graph Coloring

# Implemented Data Structure
- Array
- Hashmap
- Graph

# Technical Stuff
## Installation Usage
### First Time Install
Make a new virtual environment (in case soemthing wrong, then its probably not my fault)
```
python -m virtualenv ./venv
```
Install all dependencies needed
```
pip install -r ./requirement.txt
```

Run for the first time
```
python ./run.py --debug
```

### Run (after being initialized)
```
python ./run.py
```

## Environment Variables
| variables | values                         |
------------|---------------------------------
| API_KEY   | Access API KEY                 | 
| DEV_KEY   | Internal Access KEY            | 
| DB_AUTH   | Database path + protocol used* |

#### * string should be formatted as what stated in sqlalchemy docs
#### ** all key are sold separately for ~~owner profit~~ security concern
## Depedencies
| Libraries        | Function                                             | 
-------------------|-------------------------------------------------------
| Flask            | Provides Backend Microinfrastructure                 |
| Flask-cors       | Provides CORS for Flask Framework                    |
| Flask-SQLAlchemy | Provides SQLAlchemy Integrations for Flask Framework |
| SQLAlchemy       | Provides Database Interface Abstraction for Python   |

## Why Python?
bruh. Python is really really really **easy** to adapted to

# Full Team
| [Fuyuna](https://github.com/nmluci) | [Pangpang](https://github.com/kompiangg) | [Ngakan](https://github.com/NgakanWidyasprana) | [Diah](https://github.com/diahpramesti) | [James Fang](https://github.com/jamesfangyauw) | [Audy](https://github.com/diahpramesti) | 
--------------------------------------|------------------------------------------|------------------------------------------------|-----------------------------------------|------------------------------------------------|------------------------------------------
| Project Lead, Back-End, DBA         | Full-Stack DevOps                        | Full-Stack                                     | Front-End                               | Front-End                                      | Front-End        