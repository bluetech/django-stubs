from email._policybase import Policy  # type: ignore
from email.mime.message import MIMEMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

utf8_charset: Any
utf8_charset_qp: Any
DEFAULT_ATTACHMENT_MIME_TYPE: str
RFC5322_EMAIL_LINE_LENGTH_LIMIT: int

class BadHeaderError(ValueError): ...

ADDRESS_HEADERS: Any

def forbid_multi_line_headers(name: str, val: str, encoding: str) -> Tuple[str, str]: ...
def split_addr(addr: str, encoding: str) -> Tuple[str, str]: ...
def sanitize_address(addr: Union[Tuple[str, str], str], encoding: str) -> str: ...

class MIMEMixin: ...

class SafeMIMEMessage(MIMEMixin, MIMEMessage):
    defects: List[Any]
    epilogue: None
    policy: Policy
    preamble: None

class SafeMIMEText(MIMEMixin, MIMEText):
    defects: List[Any]
    epilogue: None
    policy: Policy
    preamble: None
    encoding: str = ...
    def __init__(self, _text: str, _subtype: str = ..., _charset: str = ...) -> None: ...

class SafeMIMEMultipart(MIMEMixin, MIMEMultipart):
    defects: List[Any]
    epilogue: None
    policy: Policy
    preamble: None
    encoding: str = ...
    def __init__(
        self, _subtype: str = ..., boundary: None = ..., _subparts: None = ..., encoding: str = ..., **_params: Any
    ) -> None: ...

class EmailMessage:
    content_subtype: str = ...
    mixed_subtype: str = ...
    encoding: Any = ...
    to: List[str] = ...
    cc: List[Any] = ...
    bcc: List[Any] = ...
    reply_to: List[Any] = ...
    from_email: str = ...
    subject: str = ...
    body: str = ...
    attachments: List[Any] = ...
    extra_headers: Dict[Any, Any] = ...
    connection: Any = ...
    def __init__(
        self,
        subject: str = ...,
        body: Optional[str] = ...,
        from_email: Optional[str] = ...,
        to: Optional[Union[Sequence[str], str]] = ...,
        bcc: Optional[Union[Sequence[str], str]] = ...,
        connection: Optional[Any] = ...,
        attachments: Optional[Union[List[Tuple[str, Union[str, bytes], str]], List[MIMEText]]] = ...,
        headers: Optional[Dict[str, str]] = ...,
        cc: Optional[Union[Sequence[str], str]] = ...,
        reply_to: Optional[Union[List[Optional[str]], str]] = ...,
    ) -> None: ...
    def get_connection(self, fail_silently: bool = ...) -> Any: ...
    def message(self) -> MIMEMixin: ...
    def recipients(self) -> List[str]: ...
    def send(self, fail_silently: bool = ...) -> int: ...
    def attach(
        self,
        filename: Optional[Union[MIMEText, str]] = ...,
        content: Optional[Union[bytes, EmailMessage, SafeMIMEText, str]] = ...,
        mimetype: Optional[str] = ...,
    ) -> None: ...
    def attach_file(self, path: str, mimetype: Optional[str] = ...) -> None: ...

class EmailMultiAlternatives(EmailMessage):
    alternative_subtype: str = ...
    alternatives: Any = ...
    def __init__(
        self,
        subject: str = ...,
        body: str = ...,
        from_email: Optional[str] = ...,
        to: Optional[List[str]] = ...,
        bcc: Optional[List[str]] = ...,
        connection: Optional[Any] = ...,
        attachments: None = ...,
        headers: Optional[Dict[str, str]] = ...,
        alternatives: Optional[List[Tuple[str, str]]] = ...,
        cc: None = ...,
        reply_to: None = ...,
    ) -> None: ...
    def attach_alternative(self, content: str, mimetype: str) -> None: ...
