"""
Endpoint with Typer

https://typer.tiangolo.com/tutorial/package/
"""
import typer
from ai_doc.runner import Runner

app = typer.Typer()


@app.command()
def main():
    """
    endpoint function
    """
    runner = Runner()
    return runner.run()


app(prog_name='ai-doc')
