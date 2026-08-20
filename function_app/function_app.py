import azure.functions as func # type: ignore
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION) # type: ignore

@app.route(route="http_trigger") # type: ignore
def http_trigger(req: func.HttpRequest) -> func.HttpResponse: # type: ignore
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name') # type: ignore
    if not name:
        try:
            req_body = req.get_json() # type: ignore
        except ValueError:
            pass
        else:
            name = req_body.get('name') # type: ignore

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.") # type: ignore
    else:
        return func.HttpResponse( # type: ignore
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        ) # type: ignore