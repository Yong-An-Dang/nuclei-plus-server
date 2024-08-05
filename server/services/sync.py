import logging

from server.sql import crud
from server.sql.schemas import SyncRequestBody, SyncResponseBody, SyncTemplate

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
    """
    filter: SyncFilter = None
    pageSize: int = None
    currentPage: int = None

    private String dir;
    private String id;
    private String name;
    private String author;
    private String severity;
    private String tags;

    :param body:
    :return:
    """
    skip = body.pageSize * (body.currentPage - 1)
    limit = body.pageSize
    templates = crud.get_templates(body.filter, skip, limit)
    logger.debug(templates)

    syncTemplates = []
    for template in templates:
        tmp = SyncTemplate()
        tmp.content = template.content_base64
        tmp.dir = template.dir
        syncTemplates.append(tmp)
    resp = SyncResponseBody()
    resp.code = 0
    resp.reason = "success"
    resp.templates = syncTemplates
    resp.pageSize = body.pageSize
    resp.currentPage = body.currentPage

    return resp
