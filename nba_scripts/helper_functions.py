from nba_api.stats.endpoints import leaguedashplayerstats
import unicodedata

def get_train_window(test_idx, seasons):
    start_idx = max(0, test_idx-2)
    # end_idx = min(len(seasons), test_idx + 4)
    return seasons[start_idx:test_idx]

def get_season_stats(curr_season):
    # This function gets the season stats based on the season string it is given.
    # returns a clean table (Dataframe)
    # 'Season' column is added to the table so we don't forget which year the stats belong to
    stats = leaguedashplayerstats.LeagueDashPlayerStats(season=curr_season)
    df = stats.get_data_frames()[0]
    df['Season'] = curr_season
    return df


def clean_name(name):
    return ''.join(c for c in unicodedata.normalize('NFD', name)
                  if unicodedata.category(c) != 'Mn')