from actor import A, B


class Game:

    def __init__(self, side_a: str, side_b: str, qas: list, _id=None) -> None:
        self.side_a: str = side_a
        self.side_b: str = side_b
        self.qas: list = qas
        self._id = _id

    def turn(self, actor_a: A, actor_b: B) -> None:
        if len(self.qas) == 0:
            self.qas.append(actor_a.instruct(self.side_a, self.side_b))
            self.qas.append(actor_b.instruct(self.side_b, self.side_a))
            return
        if self.qas[-1]['actor'] == self.side_a:
            self.qas.append(actor_b.act(self.side_b))
            return
        self.qas.append(actor_a.act(self.side_a))
