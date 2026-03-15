class Musteri(BaseModel):
    username:str = Field(min_length=1 )
    password:str = Field(min_length=6)
    age:int = Field(gt=0)