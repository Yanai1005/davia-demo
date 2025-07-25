from davia import Davia

app = Davia()

@app.task
def hello_world(name: str = "World") -> str:
    """シンプルな挨拶を返します。"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run()
