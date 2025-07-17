from src.etl.load_data import load_raw_data

sales, calendar, prices = load_raw_data()

def main():
    print("Hello from m5-forecasting!")


if __name__ == "__main__":
    main()