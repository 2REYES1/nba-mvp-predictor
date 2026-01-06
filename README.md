# nba-mvp-predictor
This is machine learning project that will predict the winner of the NBA Most Valuable Player (MVP) for any season. It will focus on Supervised Learning using Regression.

## The Challenge
As an NBA fan, it’s clear that being the "Most Valuable Player" isn't just a math equation based on the best stats. It’s a complex mix of individual dominance, team success, and the "narrative" created by how fans and voters perceive a player's impact. What made someone an MVP in 2012 is very different from what wins the award today, as voter priorities have shifted from pure winning toward historic statistical efficiency. My challenge was to build a model that doesn't just read box scores, but actually captures how these shifting perceptions translate into votes.

## Data Acquistion & Pipeline
I pulled the raw data directly from the nba_api, specifically focusing on the leaguedashplayerstats endpoint to get full box-score data for every player. To make the data "MVP-ready," I implemented the league's 65-game eligibility rule and filtered for top-tier fantasy performers to eliminate the noise from bench players. I also performed feature engineering to convert raw stats into league ranks, ensuring the model compares players relative to their specific era and competition.

## Modeling & Iteration
I started with a simple Linear Regression model, which initially struggled with a low $R^2$ because it was trying to process too many irrelevant features and seasons. Through several iterations, I discovered that "less is more," narrowing the training window to the most recent seasons and focusing on high-impact "Power Features" like W_PCT_RANK and NBA_FANTASY_PTS_RANK. This process taught me that refining the input data is often more important than the complexity of the algorithm itself.

## Model Performance
After optimizing the feature set and training window, the model achieved a strong $R^2$ score of 0.8 specifically for the 2022-23 test season, meaning it explained 80% of the logic for that year. The Mean Absolute Error (MAE) sat at roughly 0.88, indicating the model was accurate within less than one ranking position for the top candidates. However, this high performance is currently localized to the modern era, as the model struggles to maintain that same accuracy when predicting prior seasons where voter criteria differed. I am currently working on refining the features to better capture historical trends and ensure the model generalizes across the NBA's evolving eras.

## Tech Stack
The backend of this project is built entirely in Python, utilizing Pandas for heavy data manipulation and Scikit-Learn for the regression modeling. I managed the development environment through Git using a feature-branch workflow to keep my experimental model versions organized. For the next phase, I am integrating a Firebase database to store predictions and a React frontend to display a live "MVP Race" dashboard for users.