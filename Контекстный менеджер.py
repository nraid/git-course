
class DBConnection:

    def __enter__(self):
        print("Connected to db...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnected from db...")


with DBConnection() as conn:
    print("selecting from db...")
    