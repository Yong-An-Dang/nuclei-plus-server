import logging

from server.sql import crud
from server.sql.schemas import SyncRequestBody, SyncResponseBody

logger = logging.getLogger(__name__)


def sync_upload(body: SyncRequestBody):
    for template in body.templates:
        tmp = crud.create_template(template)
        logger.debug(tmp.__dict__)
    resp = SyncResponseBody()
    resp.code = 0
    resp.reason = "success"
    return resp


def sync_download(body: SyncRequestBody):
    pass
