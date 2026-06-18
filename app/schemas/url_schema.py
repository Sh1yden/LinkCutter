from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class BaseUrlSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
    )


class URLCreate(BaseUrlSchema):
    original_url: HttpUrl = Field(
        ...,
        description="The original URL",
        max_length=2048,
    )
    custom_code: str | None = Field(
        None,
        description="Your custom code",
        min_length=3,
        max_length=50,
        pattern=r"^[a-zA-Z0-9_-]+$",
    )


class URLResponse(BaseUrlSchema):
    short_url: str
    original_url: HttpUrl
    code: str
