import logging

from fastapi import APIRouter

from server.services.sync import sync_upload, sync_download
from server.sql.schemas import SyncRequestBody

logger = logging.getLogger(__name__)

router = APIRouter(tags=["sync"])


@router.post("/sync")
def sync(body: SyncRequestBody):
    logger.debug(body.action)
    if body.action == "upload":
        response = sync_upload(body)
    else:
        response = sync_download(body)

    return response
