import os
import requests
from utils.general_utils import return_season_dataframe


def get_nhl_current_season():
    """get nhl current season and return as dataframe"""
    # base string
    nhl = "https://api.sportsdata.io/v3/nhl/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        nhl,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "nhl")

    return r


def get_nba_current_season():
    """get nba current season and return as dataframe"""
    # base string
    nba = "https://api.sportsdata.io/v3/nba/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        nba,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "nba")

    return r


def get_nfl_current_season():
    """get nfl current season and return as dataframe"""
    # base string
    nfl = "https://api.sportsdata.io/v3/nfl/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        nfl,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "nfl")

    return r


def get_cbb_current_season():
    """get cbb current season and return as dataframe"""
    # base string
    cbb = "https://api.sportsdata.io/v3/cbb/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        cbb,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "cbb")

    return r


def get_mlb_current_season():
    """get mlb current season and return as dataframe"""
    # base string
    mlb = "https://api.sportsdata.io/v3/mlb/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        mlb,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "mlb")

    return r


def get_cfb_current_season():
    """get cfb current season and return as dataframe"""
    # base string
    cfb = "https://api.sportsdata.io/v3/cfb/scores/json/CurrentSeason"
    # call environment variable
    r = requests.get(
        cfb,
        headers={"Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]},
    )
    # get status
    status = r.status_code
    # return dataframe
    r = return_season_dataframe(r.json(), status, "cfb")

    return r
