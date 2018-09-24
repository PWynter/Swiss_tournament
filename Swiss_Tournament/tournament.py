import psycopg2


def connect():
    """Connect to PostgreSQL tournament database with a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM matches"
    db_cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Deletes players from players table """
    db = connect()
    db_cursor = db.cursor()
    query = "DELETE FROM players"
    db_cursor.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT count(*) as num FROM players"
    db_cursor.execute(query)
    count = int(db_cursor.fetchone()[0])
    db.commit()
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO players (name) values (%s)"
    db_cursor.execute(query, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    db = connect()
    db_cursor = db.cursor()
    query = "SELECT * FROM playerStandings"
    db_cursor.execute(query)
    standings = db_cursor.fetchall()
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db = connect()
    db_cursor = db.cursor()
    query = "INSERT INTO matches (winner, loser) values (%s, %s);"
    db_cursor.execute(query, (int(winner), int(loser)))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    db = connect()
    db_cursor = db.cursor()
    query = "SELECT id, name FROM playerStandings"
    db_cursor.execute(query)
    standings = db_cursor.fetchall()
    number_of_pairs = len(standings)/2
    pairings = []
    for _ in range(number_of_pairs):
        p1 = standings.pop(0)
        p2 = standings.pop(0)
        pairings.append((p1[0], p1[1], p2[0], p2[1]))    
    db.commit()
    db.close()
    return pairings

   