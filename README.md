# The Neumann-Turing Machine

The Neumann-Turing Machine: An LLM approach to strategic game theory

## Goal

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
