from load_csv import load
from matplotlib.ticker import FuncFormatter
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


def parse_population(val: str) -> float:
    """Convert population string with suffix to float."""
    val = str(val).strip().upper()  # 前後の空白削除 + 大文字化
    if val.endswith("B"):
        return float(val[:-1]) * 1e9
    if val.endswith("M"):
        return float(val[:-1]) * 1e6
    if val.endswith("K"):
        return float(val[:-1]) * 1e3
    return float(val)


def format_population_ticks(val: float, _: float) -> str:
    """Format tick values dynamically as billions, millions, or thousands."""
    if val <= 0:
        return "0"
    if val >= 1e9:
        return f"{val / 1e9:g}B"
    if val >= 1e6:
        return f"{val / 1e6:g}M"
    if val >= 1e3:
        return f"{val / 1e3:g}k"
    return f"{val:g}"


def plot_two_countries_pop(df_1: pd.DataFrame, df_2: pd.DataFrame,
                           country_1: str, country_2: str) -> None:
    """Plot population comparison between two countries."""
    years = [str(y) for y in range(1800, 2051)]
    pop_country1 = [parse_population(p) for p in df_1[years].values[0]]
    pop_country2 = [parse_population(p) for p in df_2[years].values[0]]

    plt.plot(range(1800, 2051), pop_country1, label=country_1, color="blue")
    plt.plot(range(1800, 2051), pop_country2, label=country_2, color="green")
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(range(1800, 2050, 40))
    # グラフのy軸のフォーマッターを変えるために使う
    plt.gca().yaxis.set_major_formatter(FuncFormatter(format_population_ticks))

    plt.legend(loc="lower right")
    plt.show()


def main():
    """Load population dataset and compare two countries."""
    df = load("population_total.csv")
    if df is None:
        return
    try:
        country_1 = "Japan"
        country_2 = "France"
        df_1 = validate_dataframe(df, country_1)
        df_2 = validate_dataframe(df, country_2)
        plot_two_countries_pop(df_1, df_2, country_1, country_2)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
