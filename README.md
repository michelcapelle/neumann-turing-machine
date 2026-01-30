# The Neumann-Turing Machine

## An LLM Approach to Strategic Game Theory

John von Neumann (1903-1957) was a Hungarian-born American mathematician. Important work in set theory inaugurated a career that touched nearly every major branch of mathematics. Von Neumann’s gift for applied mathematics took his work in directions that influenced quantum theory, automata theory, economics, and defense planning. Von Neumann pioneered game theory and, along with Alan Turing and Claude Shannon, was one of the conceptual inventors of the stored-program digital computer.

Alan Turing (1912-1954) was a British mathematician and logician who made major contributions to mathematics, cryptanalysis, logic, philosophy, and mathematical biology and also to the new areas later named computer science, cognitive science, artificial intelligence, and artificial life.

## Game Theory

In 1928 von Neumann published “Theory of Parlor Games,” a key paper in the field of game theory. Though von Neumann knew of the earlier work of the French mathematician Émile Borel, he gave the subject mathematical substance by proving the mini-max theorem. This asserts that for every finite, two-person zero-sum game, there is a rational outcome in the sense that two perfectly logical adversaries can arrive at a mutual choice of game strategies, confident that they could not expect to do better by choosing another strategy.

## Artificial Intelligence

Turing was a founding father of artificial intelligence and of modern cognitive science, and he was a leading early exponent of the hypothesis that the human brain is in large part a digital computing machine. He theorized that the cortex at birth is an “unorganised machine” that through “training” becomes organized “into a universal machine or something like it.” Turing proposed what subsequently became known as the Turing test as a criterion for whether an artificial computer is thinking (1950). In late 2022, the advent of ChatGPT reignited conversation about the likelihood that the components of the Turing test had been met.

## Goal

The API contains 2 LLM models -- Alpha and Beta. Both LLMs are instructed to serve a state's national interests in a war game. Each turn, one of the LLMs is prompted to generate and act upon a scenario. The LLM's answer -- a generated event -- is provided as contextual input for the other LLM's turn. At the end of the war game, the Alpha model is prompted to analyze and summarize the key findings leading to the (un)successful outcome of the game. Was Alpha able to improve its situation?

At the end of all training war games, all key findings serve as contextual input for the instruction prompt for the Alpha model's next series -- the evaluation war games. This series the Alpha model starts with its lessons learned from the training series. The Beta model remains instructed as a tabula rasa.

At the end of all evaluation war games, the results of this series are evaluated again. Did the training makes sense? Was Alpha able to improve its average result using the lessons learned?

## Installation

### Dependencies

```bash
pip install -r requirements.txt
```

### Models

```bash
python llm.py
```

## Usage

### Docker: Air (MongoDB), Chat (MongoExpress), Channel (RabbitMQ)

```bash
docker-compose up -d
```

### Chat

[localhost:8081](http://localhost:8081)

`admin:admin`

### Channel

[localhost:15672/#/queues](localhost:15672/#/queues)

`admin:admin`

### Enigma (worker)

```bash
python enigma.py
```

### API

```bash
python app.py
```

[localhost:5000/swagger](http://localhost:5000/swagger)

### Cyanide (UI)

```bash
cd cyanide
ng serve
```

[localhost:4200/](http://localhost:4200/)
