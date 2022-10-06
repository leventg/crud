from pydantic import BaseModel, Field

class MdlList(BaseModel):
    """
        list model used for presentation. All fields are mandatory
    """
    id:int = Field(gt=0, description="The id must be greater than zero")
    address:str = Field(min=1, max=300, description="length of address field must be greater than zero and less than 301")
    price:int = Field(ge=0, description="The price must be zero or greater than zero")