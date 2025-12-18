import typer

app = typer.Typer()

@app.command(help="Profile a CSV file and write JSON + Markdown reports.")
def profile(
    input_path: str = "data/sample.csv",
    out_dir: str = "outputs",
    report_name: str = "my-Report",
) -> None:
    print(f"Profiling {input_path}...")

@app.command()
def version() -> None:
    typer.echo("csv-profiler 0.1")

if __name__ == "__main__":
    app()

