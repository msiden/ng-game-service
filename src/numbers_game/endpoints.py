from game import Games


games = Games()

def health_check() -> bool:
    return True

def new_game(range: int) -> dict:
    return {
        "id": games.new(range)
    }

def submit_guess(id: str, guess: int) -> dict:
    game = games.all.get(id)

    if game is None:
        return 'Game not found', 500

    result = game.guess(guess)

    if result['correct_number'] is not None:
        games.remove(id)

    return result
