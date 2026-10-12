from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def validate_dataframe(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """Filter dataset for the specified country."""
    if "country" not in df.columns:
        raise KeyError("'country' not found in Columns")
    country_df = df[df["country"] == country]
    if country_df.empty:
        raise ValueError(f"{country} not found")
    if len(country_df.columns) < 2:
        raise ValueError("Dataset does not contain year columns.")
    return country_df


def plot_life_expectancy_years(country_df: pd.DataFrame, country: str) -> None:
    """Plot life expectancy projections for the specified country."""
    years = country_df.columns[1:].astype(int)
    life_expectancy = country_df.values[0][1:]

    plt.plot(years, life_expectancy)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(1800, 2081, 40))  # xticks = x軸で()刻みで表示
    plt.show()


def main():
    """Load life expectancy dataset and plot Japan's projections."""
    df = load("life_expectancy_years.csv")
    if df is None:
        return
    country = "Japan"
    try:
        country_df = validate_dataframe(df, country)
        plot_life_expectancy_years(country_df, country)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
