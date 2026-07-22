from sqlalchemy.orm import Session

from backend.app.models.company import Company
from backend.app.models.diagnosis import Diagnosis
from backend.app.models.action_plan import ActionPlan
from backend.app.models.notification import Notification


class DashboardService:

    def __init__(self, db: Session):
        self.db = db

    def get_overview(self, company_id: int) -> dict:
        """
        Retorna o resumo executivo do Dashboard.
        """

        company = (
            self.db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

        total_diagnoses = (
            self.db.query(Diagnosis)
            .filter(Diagnosis.company_id == company_id)
            .count()
        )

        open_actions = (
            self.db.query(ActionPlan)
            .filter(
                ActionPlan.company_id == company_id,
                ActionPlan.status != "COMPLETED",
            )
            .count()
        )

        notifications = (
            self.db.query(Notification)
            .filter(Notification.company_id == company_id)
            .count()
        )

        return {
            "company": company.corporate_name if company else "",
            "diagnoses": total_diagnoses,
            "open_actions": open_actions,
            "notifications": notifications,
            "maturity": 0,
            "risk_level": "UNKNOWN",
            "overall_score": 0,
        }