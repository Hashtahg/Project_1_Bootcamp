# Portfolio Analysis Application

This application will ask the user for their risk tolerence and prefered stock holding period, and will return a basket of equites suitable to their preferences.
The application will be using Monte Carlo Simulations to give the user an idea of how their portfolio might look at the end of their holding period by showcasing a lower and upper bound prediction using a 95% confidence interval.

The application will begin by asking the client their risk tolerance level. They can choose conservative, aggressive, or very aggressive. We'll label these as level 1, 2, and 3.  The next question will be what timeframe in years are they looking for us to forecast the potential 95% confidence interval for the low and high value of their portfolio.

Once we have the above information we'll then have a basket of 5 tickers that we will run a Monte Carlo simulation on for the number of years the client specified.

Before the Monte Carlo simulation we assume we have 100 shares of each ticker and pull in the yesterday closes to
get a current value of the holdings of each security and the total portfolio.

We do this by multiplying the yesterday close by the 100 shares, then summing up each holding value to get the total portfolio.

value_i yest_close_i * shares_i = holding value of the security i
total portfolio holding value is the sum of values of each holding value for each security i, namely: value_1 + value_2 + ... + value_5

Once we have this we run the Monte Carlo simulation assuming 20% weight in each security, and we give the 95% confidence interval
of the low and high value of the portfolio.

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