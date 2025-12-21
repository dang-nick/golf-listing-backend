# Golf Listing Backend
This backend builds a model for historic golf club listings.
** Need to plan project to avoid compliance issues **

golf-lsting-backend/
├── ingestion/
│   ├── __init__.py
│   ├── ebay_client.py
│   ├── fetch_listings.py
│   ├── normalize.py
│   ├── runner.py
│   └── schedules.py
│
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── routes/
│   │   ├── clubs.py
│   │   └── metrics.py
│   ├── schemas.py       # Pydantic models
│   └── dependencies.py
│
├── db/
│   ├── __init__.py
│   ├── models.py        # SQLAlchemy models
│   ├── session.py
│   └── migrations/      # Alembic
│
├── shared/
│   ├── __init__.py
│   └── constants.py
│
├── scripts/
│   └── run_ingestion.py
│
├── tests/
│   ├── ingestion/
│   └── api/
│
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.ingestion
├── pyproject.toml
└── README.md