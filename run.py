# run.py
from app import create_app
from imports import SearchForm
from imports import Taskdata

app = create_app()

td = Taskdata()

@app.context_processor
def base():
    search_form = SearchForm()
    return dict(search_form=search_form)


if __name__ == '__main__':
    app.run( debug=True)
    