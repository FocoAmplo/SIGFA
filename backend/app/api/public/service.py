from decimal import Decimal

from sqlalchemy.orm import Session

from backend.app.models.lead import Lead

from .schemas import PublicLeadCreate


class PublicLeadService:

    @staticmethod
    def calculate_score(data: PublicLeadCreate) -> int:

        score = 0

        if data.company_name:
            score += 10

        if data.segment:
            score += 10

        if data.employees >= 100:
            score += 20
        elif data.employees >= 30:
            score += 15
        elif data.employees >= 10:
            score += 10
        elif data.employees > 0:
            score += 5

        revenue = data.monthly_revenue or Decimal("0")

        if revenue >= Decimal("1000000"):
            score += 25
        elif revenue >= Decimal("500000"):
            score += 20
        elif revenue >= Decimal("100000"):
            score += 15
        elif revenue >= Decimal("30000"):
            score += 10
        elif revenue > 0:
            score += 5

        if data.main_problem:
            problem_length = len(data.main_problem.strip())

            if problem_length >= 150:
                score += 15
            elif problem_length >= 50:
                score += 10
            elif problem_length > 0:
                score += 5

        score += data.urgency * 3

        score += data.investment_capacity * 3

        return min(score, 100)

    @staticmethod
    def classify(score: int) -> tuple[str, bool]:

        if score >= 75:
            return "alta prioridade", True

        if score >= 55:
            return "qualificado", True

        if score >= 35:
            return "em maturação", False

        return "não qualificado", False

    @classmethod
    def create_lead(
        cls,
        db: Session,
        data: PublicLeadCreate,
    ) -> Lead:

        score = cls.calculate_score(data)

        classification, qualified = cls.classify(score)

        lead = Lead(
            name=data.name,
            email=data.email,
            phone=data.phone,
            company_name=data.company_name,
            segment=data.segment,
            city=data.city,
            state=data.state.upper() if data.state else None,
            employees=data.employees,
            monthly_revenue=data.monthly_revenue,
            main_problem=data.main_problem,
            urgency=data.urgency,
            investment_capacity=data.investment_capacity,
            score=score,
            classification=classification,
            status="novo",
            source=data.source,
            notes=data.notes,
            qualified=qualified,
        )

        db.add(lead)
        db.commit()
        db.refresh(lead)

        return lead


public_lead_service = PublicLeadService()