from pydantic import BaseModel, Field
from typing import Optional


class WorkQuery(BaseModel):
    work_id: str = Field(...,
                         description="OpenAlex Work ID (e.g., 'W1234567890') or DOI.")


class WorksSearchQuery(BaseModel):
    filter: Optional[str] = Field(
        None, description="OpenAlex filter string (e.g., 'institutions.id:https://openalex.org/I97018004')")
    sort: Optional[str] = Field(
        None, description="Sort order (e.g., 'publication_date:desc')")
    per_page: Optional[int] = Field(
        10, description="Number of results per page.")
    page: Optional[int] = Field(1, description="Page number.")


class AuthorQuery(BaseModel):
    author_id: str = Field(...,
                           description="OpenAlex Author ID (e.g., 'A1234567890').")


class InstitutionQuery(BaseModel):
    institution_id: str = Field(...,
                                description="OpenAlex Institution ID (e.g., 'I97018004').")
