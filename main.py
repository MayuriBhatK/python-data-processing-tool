import pandas as pd
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_file(input_file, output_file):
    try:
        data = pd.read_csv(input_file)
        data.dropna(inplace=True)
        data.to_csv(output_file, index=False)
        logging.info("File processed successfully")
    except Exception as e:
        logging.error(str(e))

if __name__ == "__main__":
    process_file("input.csv", "output.csv")
  
