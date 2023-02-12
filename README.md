# wdc_baku

A project that collects the current weather condition of Baku and stores it in a log file. The weather data is collected from a trusted weather API and stored in both JSON and CSV formats, as well as a log file.

## Usage

1. Clone repository

```bash
git clone https://github.com/test2user-aqil/wdc_baku
```

2. Navigate to the project directory

```bash
cd wdc_baku
```

3. Install the required libraries

```bash
pip install -r requirements.txt
```

4. Set the API key as an environment variable

```bash
export API_KEY=<your_api_key>
```

5. Run the script

```bash
python3 wdc_baku.py
```

## Data

The weather data collected includes the following information:

-   Temperature (in Celsius)
-   Description (e.g. "clear sky", "light rain")

## File formats

-   JSON
-   CSV
-   Log

## Note

The weather API used in this project provides limited free requests per day. If you plan on using the script frequently, it is recommended to sign up for a paid plan to ensure a steady supply of weather data.
