"""Opportunities API endpoints"""

from fastapi import APIRouter, Query, HTTPException, status
from typing import List, Optional

router = APIRouter()


SAMPLE_OPPORTUNITIES = [
    {
        "id": 1,
        "title": "China Flooring Construction Project",
        "region": "Asia/China",
        "industry": "Construction",
        "description": "Large commercial flooring construction project",
        "budget": 500000,
        "posted_date": "2026-06-01",
        "deadline": "2026-07-01",
    },
    {
        "id": 2,
        "title": "USA Industrial Flooring Project",
        "region": "North America/USA",
        "industry": "Industrial",
        "description": "Industrial plant flooring construction",
        "budget": 800000,
        "posted_date": "2026-06-02",
        "deadline": "2026-07-15",
    },
]


@router.get("/", summary="Get all opportunities")
async def list_opportunities(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    region: Optional[str] = None,
    industry: Optional[str] = None,
):
    """Get list of opportunities with optional filters"""
    opportunities = SAMPLE_OPPORTUNITIES

    if region:
        opportunities = [
            o for o in opportunities if region.lower() in o["region"].lower()
        ]

    if industry:
        opportunities = [
            o for o in opportunities if industry.lower() in o["industry"].lower()
        ]

    return {
        "total": len(opportunities),
        "skip": skip,
        "limit": limit,
        "data": opportunities[skip : skip + limit],
    }


@router.get("/{opportunity_id}", summary="Get opportunity details")
async def get_opportunity(opportunity_id: int):
    """Get single opportunity details"""
    for opp in SAMPLE_OPPORTUNITIES:
        if opp["id"] == opportunity_id:
            return opp
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Opportunity not found",
    )


@router.post("/", summary="Create new opportunity")
async def create_opportunity(title: str, region: str, industry: str):
    """Create new opportunity (admin function)"""
    new_id = max([o["id"] for o in SAMPLE_OPPORTUNITIES]) + 1
    new_opportunity = {
        "id": new_id,
        "title": title,
        "region": region,
        "industry": industry,
    }
    SAMPLE_OPPORTUNITIES.append(new_opportunity)
    return new_opportunity
