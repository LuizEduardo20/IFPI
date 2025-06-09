from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime
import uuid
from enum import Enum

app = FastAPI(
    title="DevMasters Project Management API",
    description="API para gerenciamento de mini-projetos da DevMasters Inc.",
    version="1.0.0"
)

class ProjectStatus(str, Enum):
    PLANEJADO = "Planejado"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDO = "Concluído"
    CANCELADO = "Cancelado"

class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, description="Título do projeto")
    description: Optional[str] = Field(None, description="Descrição detalhada do projeto")
    priority: int = Field(..., ge=1, le=3, description="Prioridade do projeto (1-3)")
    status: ProjectStatus = Field(..., description="Status atual do projeto")

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True

# Simulando um banco de dados na memória
projects_db = {}

@app.get("/projects", response_model=List[ProjectResponse])
async def list_projects(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=100),
    status: Optional[ProjectStatus] = None,
    priority: Optional[int] = Query(None, ge=1, le=3)
):
    filtered_projects = list(projects_db.values())
    
    if status:
        filtered_projects = [p for p in filtered_projects if p.status == status]
    if priority:
        filtered_projects = [p for p in filtered_projects if p.priority == priority]
    
    return filtered_projects[skip:skip + limit]

@app.post("/projects", response_model=ProjectResponse, status_code=201)
async def create_project(project: ProjectCreate):
    project_id = uuid.uuid4()
    project_data = project.dict()
    project_data["id"] = project_id
    project_data["created_at"] = datetime.now()
    
    projects_db[project_id] = project_data
    return project_data

@app.get("/projects/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: uuid.UUID):
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projects_db[project_id]

@app.put("/projects/{project_id}", response_model=ProjectResponse)
async def update_project(project_id: uuid.UUID, project: ProjectUpdate):
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    
    project_data = project.dict()
    project_data["id"] = project_id
    project_data["created_at"] = projects_db[project_id]["created_at"]
    
    projects_db[project_id] = project_data
    return project_data

@app.delete("/projects/{project_id}", status_code=204)
async def delete_project(project_id: uuid.UUID):
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    
    del projects_db[project_id]
    return None