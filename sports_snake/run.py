import os
import click
import pandas as pd
from src.get_sport_season import get_nhl_current_season
from src.get_sport_season import get_cbb_current_season
from src.get_sport_season import get_cfb_current_season
from src.get_sport_season import get_mlb_current_season
from src.get_sport_season import get_nba_current_season
from src.get_sport_season import get_nfl_current_season
from utils.general_utils import call_sport_schedule


@click.group()
def cli():
    pass


@cli.command()
@click.argument("sport")
@click.argument("season")
@click.argument("key")
def pull(sport, season, key):
    season = str(season)
    os.environ["OCP-APIM-SUBSCRIPTION-KEY"] = key

    df = call_sport_schedule(sport, season)

    file_name = sport + season + ".csv"
    if isinstance(df, pd.DataFrame):
        df.to_csv(file_name)
    else:
        print("error")


@cli.command()
@click.argument("sport")
@click.argument("key")
def cs(sport, key):
    os.environ["OCP-APIM-SUBSCRIPTION-KEY"] = key
    if sport == "nhl":
        df = get_nhl_current_season()
        click.echo(df)
    elif sport == "cbb":
        df = get_cbb_current_season()
        click.echo(df)
    elif sport == "cfb":
        df = get_cfb_current_season()
        click.echo(df)
    elif sport == "mlb":
        df = get_mlb_current_season()
        click.echo(df)
    elif sport == "nba":
        df = get_nba_current_season()
        click.echo(df)
    elif sport == "nfl":
        df = get_nfl_current_season()
        click.echo(df)
    else:
        click.echo("sport is not found")


@cli.command()
def test():
    print("Welcome to sportsnake!")
    print("Get a trail API key from sportdata.io to get started.")


if __name__ == "__main__":
    cli()
