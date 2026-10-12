from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def clean_and_marge_data(
        df_income: pd.DataFrame, df_life: pd.DataFrame, year: str
        ) -> pd.DataFrame:
    """clean values and merge by country."""
    if "country" not in df_income.columns or "country" not in df_life.columns:
        raise KeyError("'country' not found in Columns")
    if year not in df_income.columns or year not in df_life.columns:
        raise KeyError(f"'{year}' not found in Columns")
    gdp = df_income[["country", year]].rename(columns={year: "gdp"})
    life = df_life[["country", year]].rename(columns={year: "life"})
    merged = pd.merge(gdp, life, on="country")
    merged_df = merged.dropna()
    return merged_df


def plot_gdp_and_life(gdp: pd.Series, life: pd.Series, year: str) -> None:
    """Plot scatter graph of GDP vs Life Expectancy for a given year."""
    plt.scatter(gdp, life)
    plt.title(year)
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")  # 幅が広いため対数スケールに変換
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


def main():
    """Load datasets and display life expectancy vs GDP for 1900."""
    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    df_life = load("life_expectancy_years.csv")
    if df_income is None or df_life is None:
        return

    try:
        year = "1900"
        merged_data = clean_and_marge_data(df_income, df_life, year)
        plot_gdp_and_life(merged_data["gdp"], merged_data["life"], year)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
