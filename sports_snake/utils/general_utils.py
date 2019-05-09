import os
import requests
from collections.abc import Iterable
from pandas.io.json import json_normalize


def call_sport(url_string):
    """Make an API call to sport data"""
    if "OCP-APIM-SUBSCRIPTION-KEY" in os.environ:
        d = requests.get(
            url_string,
            headers={
                "Ocp-Apim-Subscription-Key": os.environ["OCP-APIM-SUBSCRIPTION-KEY"]
            },
        )
        return d
    else:
        print("Please set key as environment variable!")


def call_sport_schedule(sport, season):
    """Call Sports schedule. Requires API to be set in environment"""
    # make url string
    string = make_url(sport, season)
    # call api
    r = call_sport(string)
    # check status_code
    status_code = r.status_code

    if status_code == 200:
        # normalize_json to dataframe
        r = json_normalize(r.json())
    else:
        status_code = str(status_code)
        message = "status code: "
        r = message + status_code

    return r


def normalize_json(request_json):
    """Normalize JSON request"""
    a = json_normalize(request_json.json())
    return a


def print_key():
    """Helper funtion to print API Key"""
    if "OCP-APIM-SUBSCRIPTION-KEY" in os.environ:
        print(os.environ["OCP-APIM-SUBSCRIPTION-KEY"])
    else:
        print("Please set key as environment variable!")


def sport_season_missing_message(status_code):
    """Message for missing sport"""
    message = "sport is likely not in season with status: "
    s = str(status_code)
    r = message + s
    return r


def return_season_dataframe(json, status, sport):
    """
    If sport is not in season then response only returns 
    one value. This function checks if the response is
    Iterable then returns a dataframe.
    """
    if isinstance(json, Iterable):
        # normalize the jason to make a dataframe
        r = json_normalize(json)
        # add a new column to indicate sport
        r["Sport"] = sport
        return r
    else:
        # return error message
        r = sport_season_missing_message(status)
        return r
    return r


def make_url(sport, season):
    """Make a list of or urls for iteration"""
    if sport == "cfb":
        requests_string = "https://api.sportsdata.io/v3/cfb/scores/json/Games/"
        a = requests_string + season
    elif sport == "nhl":
        requests_string = "https://api.sportsdata.io/v3/nhl/scores/json/Games/"
        a = requests_string + season
    elif sport == "nba":
        requests_string = "https://api.sportsdata.io/v3/nba/scores/json/Games/"
        a = requests_string + season
    elif sport == "nfl":
        requests_string = "https://api.sportsdata.io/v3/nfl/scores/json/Schedules/"
        a = requests_string + season
    elif sport == "cbb":
        requests_string = "https://api.sportsdata.io/v3/cbb/scores/json/Games/"
        a = requests_string + season
    elif sport == "mlb":
        requests_string = "https://api.sportsdata.io/v3/mlb/scores/json/Games/"
        a = requests_string + season
    else:
        pass
    return a
