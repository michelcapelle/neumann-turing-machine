# The Neumann-Turing Machine

The Neumann-Turing Machine: An LLM approach to strategic game theory

## Goal

The API contains 2 LLM models -- Alpha and Beta. Both LLMs are instructed to serve a state's national interests in a war game. Each turn, one of the LLMs is prompted to generate and act upon a scenario. The LLM's answer -- a generated event -- is provided as contextual input for the other LLM's turn. At the end of the war game, the Alpha model is prompted to analyze and summarize the key findings leading to the (un)successful outcome of the game. Was Alpha able to improve its situation?

At the end of all training war games, all key findings serve as contextual input for the instruction prompt for the Alpha model's next series -- the evaluation war games. This series the Alpha model starts with its lessons learned from the training series. The Beta model remains instructed as a tabula rasa.

At the end of all evaluation war games, the results of this series is evaluated again. Did the training makes sense? Was Alpha able to improve its average result using the lessons learned?

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
