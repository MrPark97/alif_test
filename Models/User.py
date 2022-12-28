from pydantic import BaseModel


class User(BaseModel):
    client_id: int
    age: int
    gender: str
    marital_status: str
    job_position: str
    credit_sum: float
    credit_month: int
    tariff_id: float
    score_shk: float
    education: str
    living_region: str
    monthly_income: int
    credit_count: float
    overdue_credit_count: float
