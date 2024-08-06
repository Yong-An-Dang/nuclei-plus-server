from typing import List

from pydantic import BaseModel


class SyncFilter(BaseModel):
    """
    private String dir;
    private String id;
    private String name;
    private String author;
    private String severity;
    private String tags;
    """
    dir: str  # Path
    id: str  # Template's ID
    name: str  # Template's Name
    author: str  # Template's Author
    severity: str  # Template's Severity
    tags: str  # Template's Tags


class SyncTemplate(BaseModel):
    """
    private String dir;
    private String content;
    """
    # Path
    dir: str = None
    # Base64
    content: str = None


class SyncRequestBody(BaseModel):
    """
    private String action;
    """
    # Action
    action: str = None
    # Download
    filter: SyncFilter = None
    pageSize: int = None
    currentPage: int = None
    # Upload
    count: int = None
    templates: List[SyncTemplate] = None


class SyncResponseBody(BaseModel):
    """
    private int code;
    private String reason;
    private List<SyncTemplate> templates;
    private int total;
    private int pageSize;
    private int currentPage;
    """
    code: int = 0
    reason: str = "success"
    templates: List[SyncTemplate] = None
    pageSize: int = None
    currentPage: int = None
    total: int = None


class ChatRequestBody(BaseModel):
    humanMessage: str = ""


class ChatResponseBody(BaseModel):
    aiMessage: str = ""
