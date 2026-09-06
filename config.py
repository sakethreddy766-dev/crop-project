import os

class Config:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:bunny766@localhost:5432/crop_project"
    )