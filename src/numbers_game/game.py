import uuid
import random
import time


class Answer:
    LOWER = "lower"
    HIGHER = "higher"
    CORRECT = "correct"
    GAME_OVER = "game-over"


class Game:

    def __init__(self, range: int, max_guesses: int) -> None:
        self.id = str(uuid.uuid4())
        self.guesses_left = max_guesses
        self.number = random.randint(1, range)
        self.start_time = int(time.time())
        self.total_time = None
        self.total_score = 0

    def guess(self, guess: int) -> dict:
        self.guesses_left -= 1
        result = self._get_result(guess)
        game_over = result in (Answer.GAME_OVER, Answer.CORRECT)

        if result == Answer.CORRECT:
            self._get_score()

        return {
            "answer": result,
            "guesses_left": self.guesses_left,
            "correct_number": self.number if game_over else None,
            "total_time": self.total_time,
            "total_score": self.total_score
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

    def _get_score(self) -> None:
        end_time = int(time.time())
        self.total_time = end_time - self.start_time



class Games:

    def __init__(self) -> None:
        self.all = dict()

    def new(self, range: int, max_guesses: int) -> str:
        game = Game(range=range, max_guesses=max_guesses)
        self.all[game.id] = game
        return game.id

    def remove(self, id: str) -> None:
        del self.all[id]
