"""Keep existing deployment commands working during package migration."""

from census_income.api import app

__all__ = ["app"]
