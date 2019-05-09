# sportsnake

A package that makes pulling sports schedules easy. 

#### Installation

```
pip install sport_snake
```

#### Prereqs

Must have API keys from [sportsdata.io](https://sportsdata.io/developers/getting-started). 

#### Installation

```
git clone https://github.com/alexhallam/sports_snake.git
cd sportsnake
# test install
python run.py test
```

#### Example 

This package currently has two commands `pull` and `cs`. The `pull` command
pulls data as a dataframe and saves as a csv. The cs command gets meta data
about the current season

###### pull

`python run.py pull <sport> <season> <api_key>`

```
# Examples 

python run.py pull mlb 2019 <api_key>
python run.py pull nhl 2019 <api_key>
python run.py pull cbb 2019 <api_key>
python run.py pull nba 2019 <api_key>
python run.py pull nfl 2019 <api_key>
python run.py pull cfb 2019 <api_key>
```

###### cs 

`python run.py cs <sport> <api_key>`

```
# General stucture 

python run.py cs mlb <api_key>
python run.py cs nhl <api_key>
python run.py cs cbb <api_key>
python run.py cs nba <api_key>
```

#### Extra

This is an unofficial package supporting [sportsdata.io](https://sportsdata.io/developers/getting-started)

#### Todo

- [x] Add NFL to pull
- [x] Add CFB to pull
- [ ] Add NFL to cs
- [ ] Add CFB to cs
