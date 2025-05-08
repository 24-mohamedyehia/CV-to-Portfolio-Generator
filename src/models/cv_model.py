from typing import List, Optional
from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: Optional[str] = Field(None, description="Email address of the person")
    phone: Optional[str] = Field(None, description="Phone number of the person")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    github: Optional[str] = Field(None, description="GitHub profile URL")
    twitter: Optional[str] = Field(None, description="Twitter profile URL")
    website: Optional[str] = Field(None, description="Personal website URL (if available)")


class Experience(BaseModel):
    company: str = Field(..., description="Company name where the person worked")
    position: str = Field(..., description="Job title held at the company")
    duration: str = Field(..., description="Duration of employment (e.g. Jan 2020 – Mar 2023)")
    location: Optional[str] = Field(None, description="Location (city and country) of the company (if available)")
    description: str = Field(..., description="Responsibilities and achievements during this job")


class Education(BaseModel):
    degree: str = Field(..., description="Degree or certification achieved")
    university: str = Field(..., description="Name of the educational institution")
    year: str = Field(..., description="Graduation year or study duration")
    location: Optional[str] = Field(None, description="Location of the university (if available)")


class Certification(BaseModel):
    name: str = Field(None, description="Title of the certification")
    issuer: str = Field(..., description="Organization that issued the certification")
    date: Optional[str] = Field(None, description="Date when the certification was issued (if available)")


class Project(BaseModel):
    name: str = Field(..., description="Name of the project")
    description: str = Field(..., description="Brief about what the project does and its impact")
    tech_stack: List[str] = Field(..., description="List of technologies used in the project")


class Publication(BaseModel):
    title: str = Field(..., description="Title of the publication")
    publisher: str = Field(..., description="Where the publication was published")
    date: Optional[str] = Field(None, description="Publication date (if available)")


class VolunteerWork(BaseModel):
    organization: str = Field(..., description="Name of the organization where volunteer work was done")
    role: str = Field(..., description="Role or title during volunteer work")
    duration: str = Field(..., description="Duration of the volunteer work")
    description: str = Field(..., description="Brief description of volunteer activities")


class Award(BaseModel):
    name: str = Field(..., description="Name of the award or honor received")
    issuer: str = Field(..., description="Organization that issued the award")
    date: Optional[str] = Field(None, description="Date the award was given (if available)")


class Reference(BaseModel):
    name: str = Field(..., description="Name of the reference person")
    position: str = Field(..., description="Position or title of the reference person")
    contact_info: str = Field(..., description="Contact information (email or phone) of the reference person")


class CVData(BaseModel):
    name: str = Field(..., description="Full name of the person")
    contact: Contact = Field(..., description="Contact information")
    location: Optional[str] = Field(None, description="City and country where the person is based (if available)")
    summary: Optional[str] = Field(None, description="Short personal or career summary")
    skills: List[str] = Field(..., description="List of technical and soft skills")
    experience: List[Experience] = Field(..., description="List of previous job experiences")
    education: List[Education] = Field(..., description="Educational background")
    certifications: List[Certification] = Field(..., description="List of certifications achieved")
    languages: List[str] = Field(..., description="List of languages and proficiency levels")
    projects: List[Project] = Field(..., description="List of personal/professional projects")
    publications: List[Publication] = Field(..., description="List of publications (if any)")
    volunteer_work: List[VolunteerWork] = Field(..., description="Volunteer activities")
    awards: List[Award] = Field(..., description="Awards or honors received")
    interests: List[str] = Field(..., description="List of personal hobbies or interests")
    references: List[Reference] = Field(..., description="References (if any)")
    field: str = Field(..., description="Main area of expertise or career field")
