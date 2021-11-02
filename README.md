# Portfolio Analysis Application

This application will ask the user for their risk tolerence and amount they would like to invest, and we will return a basket of equities suitable to their preferences.  The application will be using Monte Carlo Simulation to give the user an idea of how their portfolio might look at the end of their holding period by showcasing a lower and upper bound prediction using a 95% confidence interval.

The application will begin by asking the client how much they are willing to invest in their portfolio, with a $1mm minimum. The application will then ask the user for their risk tolerance level. They can choose conservative, aggressive, or very aggressive. We'll label these as level 1, 2, and 3.

Once we have the above information we'll then have a basket of 5 tickers that we will run a Monte Carlo simulation on for three different time horizons: 5 years, 10 years, and 20 years.

Before the Monte Carlo simulation we assume we have an equal amount invested in each ticker. So we divide the amount invested by five and buy as many shares as possible of each ticker and display to the client how many shares they own of each ticker based on yesterday's close.

Once we have this we run the Monte Carlo simulation assuming 20% weight in each security, and we give the 95% confidence interval
of the low and high value of the portfolio.  As mentioned above we run this for all three time horizons.

Finally, if the client confirms we will output a CSV file as a report that shows how much the client invested,
the tickers that are in their portfolio and the number of shares they own, and the low and high values of the portfolio
from the 95% confidence interval of each time horizon (5yrs, 10yrs,and 20yrs).

---

## Technologies

The team is using python version 3.7.10 and is importing the following from the built-in libraries and from functions created within the team:

import questionary
import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation

%matplotlib inline

---

## Installation Guide

The Portfolio Analysis Application uses Python version 3.7.10 and Git version 2.33.0.windows.2 installed on a laptop running windows 10 pro.

One only needs to launch jupyter lab from the gitbash terminal and then run the portfolio_analysis.ipynb noteback from the 
webpage that launches.

---

## Usage

Ensure the MCForecastTools.py file, gitignore file, and .env files are in the directory where you run portfolio_analysis.ipynb
from and the client should be good to go.  The client needs to specify the risk tolerance and timeframe they would like the Monte
Carlo to run. The client is also free to change allocation percentages in the monte carlo simulation, the years we simulate if what we offer is not to their liking, and even include more than just 5 securities if they so desire.  As long as we can pull the ticker from
Alpaca, any ticker is fair game.

---

## Contributors
The contributors are Paul Lopez, Chaim Kriger, Bipasha Goswami, Briggs Lalor, and Nev Douglas
---

## License
No licenses required. Just get the consent of the contributors above and everything should be fine.
Chaim might want a fee just a warning. :)