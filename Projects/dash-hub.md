# Dash-hub
## Background
[Dash](https://dash.plotly.com/) is an extension to Plotly's plotting platform for web dashboards. The platform is a popular professional choice, with many companies having various internal dashboards. This project has 2 main goals. 

Firstly, I want to be able to host multiple apps on 1 server and easily turn them on and off. Secondly, I want an easier method for integrating backends in the dash callback format.

### Goal 1: Single platform for hosting multiple apps
Various hosting platforms such as Plotly's own [Dash Enterprise](https://plotly.com/dash/) or [MS Azure app services](https://azure.microsoft.com/en-us/products/app-service) allow you to easily spin-up and kill your applications. The aim of this project is to be an open-source alternative for hosting multiple apps, which can be self-hosted. Particularly, the project is supposed to serve as a hub for your dashboards.

### Goal 2: Easy backend implementation
The dash platform offers 2 methods of handling server-side computations. The normal method is to write an ordinary callback, which will run on the front-end server and will freeze up your application whilst running. Since this is not convenient for long running callbacks, dash has introduced "background callbacks". These callbacks use Redis for task queuing and Celery for task execution.

Although these 2 options will cover your bases, I found the first option lacking and the second option overkill. Instead, I wanted a callback which you can simply write as normal, but execute on an external server. The dashboard should not get frozen up, but simply get pinged when the backend is done.

## Status
The development is currently in Beta due to a lack of testing.
Locally the following app platforms were successfully hosted:
- [x] Dash & Flask
- [x] Dash with new API callbacks
- [x] Static webpages (html & JS)
- [x] FastAPI

```{note}
The current framework uses multi-threading and **not** multi-processing. This means that applications will boot relatively quickly (since no new python process requires to start), but no advantage is taken from multiple processors if available. Multi-processing support might be added in the future.
```

## Dash-hub Demo
```{seealso} Demo
:class: dropdown
:::{iframe}https://dashhub.pythonanywhere.com/dashhub/
:width: 100%
:::
```
:::{warning}
The above dashboard is hosted on the free platform [pythonanywhere.com](pythonanywhere.com). The free tier on the platform requires renewing every, 3 months. If the demo above does not show anything, I will most likely need to renew the site.

Furthermore, the current Demo seems to work for fine for static webpages and Dash/Flask applications. However, running a FastAPI backend application such as **receiver** seems to not work on the current host though.
:::

## API callbacks example
I'm very pleased to share that by installing this package, you can now easily execute callbacks on a external servers.

Have a look at the example below on how to use the framework: 

```{tip} Example: Dash application with API callback
:class: dropdown
:::python
import dash
from dash import Input, Output, State, dcc, html

from dash_hub.connect_api import Receiver, api_callback, InputReceiver

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Input(id="num_1", type="number"),
        dcc.Input(id="num_2", type="number"),
        html.Button("Send Data", id="button"),
        html.Div(id="response-output"),
        # This receiver will check if the callback has finished executing every 'interval' ms.
        Receiver(id="receiver", interval=1000, n_intervals=0),
    ]
)

@api_callback(
    "http://127.0.0.1:8000/receive-data/",
    Output("response-output", "children"),
    InputReceiver("receiver"),
    Input("button", "n_clicks"),
    State("num_1", "value"),
    State("num_2", "value"),
)
def trigger_thread(data, n_clicks, num_1, num_2):
    # Note: `data` is supplied by the backend.
    return f"{num_1} * {num_2} = {data['num_3']}"


if __name__ == "__main__":
    app.run_server(debug=True, port=8081)
:::
```

```{tip} Example: FastAPI backend
:class: dropdown
:::python
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class DataModel(BaseModel):
    button : int
    num_1: float
    num_2: float

class ResponseModel(BaseModel):
    num_3: float

@app.post("/receive-data/", response_model=ResponseModel)
async def receive_data(data: DataModel):
    return {"num_3" : data.num_1 * data.num_2}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
:::