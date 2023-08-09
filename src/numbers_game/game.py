import uuid
import random


class Answer:
    LOWER = "lower"
    HIGHER = "higher"
    CORRECT = "correct"
    GAME_OVER = "game-over"


class Game:

    def __init__(self, range: int) -> None:
        self.id = str(uuid.uuid4())
        self.guesses_left = 10
        self.number = random.randint(1, range)

    def guess(self, guess: int) -> dict:
        self.guesses_left -= 1
        result = self._get_result(guess)
        game_over = result in (Answer.GAME_OVER, Answer.CORRECT)

        return {
            "answer": result,
            "guesses_left": self.guesses_left,
            "correct_number": self.number if game_over else None
        }

    def _get_result(self, guess: int) -> Answer:
        result = None
        if guess == self.number:
            result = Answer.CORRECT
        elif guess > self.number:
            result = Answer.LOWER
        elif guess < self.number:
            result = Answer.HIGHER
        if result != Answer.CORRECT and self.guesses_left == 0:
            return Answer.GAME_OVER
        return result


class Games:

    def __init__(self) -> None:
        self.all = dict()

    def new(self, range: int) -> str:
        game = Game(range=range)
        self.all[game.id] = game
        return game.id

    def remove(self, id: str) -> None:
        del self.all[id]
