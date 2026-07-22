from dataclasses import dataclass


@dataclass
class CompanyProfile:

    company_id: int

    segment: str

    subtype: str

    name: str | None = None

    regime: str | None = None

    size: str | None = None

    state: str | None = None