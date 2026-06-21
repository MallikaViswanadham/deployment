from fastapi import FastAPI,Query,Path;
from fastapi.middleware.cors import CORSMiddleware;
from pydantic import BaseModel,Field,HttpUrl;
from enum import Enum;
from typing import Annotated,Literal
app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name:str
    price : int
    is_offer : bool | None = None
    tax:int
    image:Image|None = None

class Enummodel(str,Enum):
    resnet = "resnet"
    lenet = "lenet"
    alexnet = "alexnet"

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200","https://angular-frontend.icyocean-28693c97.westus2.azurecontainerapps.io"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/dis')
def hello():
    return {'name':'MALLIKA'} 

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):       #http://127.0.0.1:8000/items/5?q=mallika
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    return {"item_id":item_id,"item_name":item.name}

@app.get("/modelname/{model_name}")
def get_enumodel(model_name:Enummodel):
    if model_name is Enummodel.alexnet:
        return {"model_name":model_name};
    if model_name.value == "lenet":
        return {"model_name" : model_name}
    return {"model_name": model_name, "message": "Have some residuals"}

fake_items_db =[{"item_name":"foo"},{"item_name":"het"},{"item_name":"ret"},{"item_name":"tet"}]

@app.get("/items/")
def get_items(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit];

@app.post("/items/")
def create_item(item:Item):
    return item;


@app.post("/items1/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict;

@app.get("/items2/")
async def read_items(q: Annotated[str | None, Query(max_length=50, pattern="^fixedquery$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items3/")
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items5/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items6/")
def read_items(hidden_query: Annotated[str | None,Query(include_in_schema=False)]=None):
    if hidden_query:
        return {"query":hidden_query}
    else:
        return {"query":"Not found"}
    
@app.get("/items7/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(alias="item-id1",title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items8/{item_id}")
async def read_items(
    *,
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results

@app.get("/items9/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
     

@app.put("/items10/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/items12/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images
