-- create table statements
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

--connnect to file
\c tournament;

-- creates players table
CREATE TABLE players(
    id SERIAL PRIMARY KEY,
    name TEXT
	);

--creates matches table where player ID is linked in
CREATE TABLE matches(
    match_id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES players(id),
    loser INTEGER REFERENCES players(id)
    );


--creates wins table view ordered by wins
CREATE VIEW playerStandingsWinner AS
	SELECT players.id AS player, count (matches.winner) AS wins
	FROM players LEFT JOIN matches
	ON players.id = matches.winner
	GROUP BY players.id
	ORDER BY wins;

--creates playerMatches table view ordered by match count
CREATE VIEW playerMatches AS
	SELECT players.id AS player, count (matches.*) AS matchCount
	FROM players LEFT JOIN matches
	ON players.id = matches.loser OR players.id = matches.winner
	GROUP BY players.id
	ORDER BY matchCount;


	--creates playerStandings table view order by player wins
CREATE VIEW playerStandings AS 
	SELECT players.id, players.name, playerStandingsWinner.wins, playerMatches.matchCount
	FROM players LEFT JOIN playerStandingsWinner 
	ON playerStandingsWinner.player = players.id 
	LEFT JOIN playerMatches ON players.id = playerMatches.player
	ORDER BY playerStandingsWinner.wins;

