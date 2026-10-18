"""
Flipped Metric Curriculum: Master Econometric & Visualization Template
Author: Christopher R. Herdelin
Repository: Turn-Key Applied Econometrics for Economics and Finance Students

This script provides production-grade templates for the weekly analyst desk 
exercises, enforcing professional data pipelines and dual-audience visual fidelity.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from fredapi import Fred

# -------------------------------------------------------------------------
# 0. CONFIGURATION & INFRASTRUCTURE POOL
# -------------------------------------------------------------------------
# Set style parameters to optimize the data-ink ratio globally
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#CBD5E0'
plt.rcParams['axes.linewidth'] = 0.8

# Secure your FRED API Key from environment variables or replace placeholder
FRED_API_KEY = os.getenv('FRED_API_KEY', 'YOUR_FRED_API_KEY_HERE')
fred = Fred(api_key=FRED_API_KEY)


def apply_cio_chart_standards(ax, title, ylabel, xlabel="Year", source_text="Source:"):
    """
    Applies strict corporate presentation standards to a Matplotlib axis.
    Removes default software clutter, left-aligns titles, and mutes gridlines.
    """
    ax.set_title(title, fontsize=11, fontweight='bold', pad=14, loc='left', color='#2D3748')
    ax.set_ylabel(ylabel, fontsize=9, color='#4A5568')
    ax.set_xlabel(xlabel, fontsize=9, color='#4A5568')
    
    # Eliminate bounding box clutter (top and right spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CBD5E0')
    ax.spines['bottom'].set_color('#CBD5E0')
    
    # Mute gridlines to optimize data-ink scannability
    ax.grid(True, linestyle='--', alpha=0.4, color='#E2E8F0')
    ax.tick_params(axis='both', colors='#4A5568', labelsize=8)
    
    # Clean footnote scholarly attribution
    plt.figtext(0.1, -0.04, source_text, fontsize=7, style='italic', color='#718096')


# -------------------------------------------------------------------------
# MODULE I EXERCISES (WEEKS 1-6)
# -------------------------------------------------------------------------

def run_week_1_exercise():
    """
    Weeks 1-2: Stationarity & High-Frequency Baselines
    Target: Daily 10-Year Treasury Yields (GS10) First-Differencing
    """
    print("[Executing Week 1-2 Exercise] Ingesting Daily Treasury Yields...")
    
    # Data Acquisition via FRED Pipeline
    df_raw = fred.get_series('GS10', start_date='2015-01-01')
    df = pd.DataFrame(df_raw, columns=['Yield'])
    df.index.name = 'Date'
    
    # STUDENT TASK: Execute First-Differencing Transformation to stabilize mean
    df['Yield_Diff'] = df['Yield'].diff()
    df.dropna(inplace=True)
    
    # CIO Visual Realization Block
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.plot(df.index, df['Yield_Diff'], color='#1A365D', linewidth=1.0, label='$\\Delta$ Yield')
    
    apply_cio_chart_standards(
        ax=ax,
        title="Stationary First-Difference ($\\Delta Y_t$) of 10-Year Treasury Yields",
        ylabel="Percentage Point Change",
        source_text="Source: Federal Reserve Bank of St. Louis FRED Database (Series: GS10)"
    )
    
    plt.tight_layout()
    plt.savefig('week_1_treasury_diff.png', bbox_inches='tight')
    plt.close()
    print(" -> Success: 'week_1_treasury_diff.png' exported.")


def run_week_3_exercise():
    """
    Weeks 3-4: Univariate Modeling (ARMA/ARIMA) Baseline
    Target: CPI Inflation Log-Transformations and Residual Setup
    """
    print("[Executing Week 3-4 Exercise] Ingesting Consumer Price Index Data...")
    
    # Monthly CPI Ingestion
    df_raw = fred.get_series('CPIAUCSL', start_date='2010-01-01')
    df = pd.DataFrame(df_raw, columns=['CPI'])
    df.index.name = 'Date'
    
    # STUDENT TASK: Execute log-transformation and seasonal differencing for variance control
    df['Log_CPI'] = np.log(df['CPI'])
    df['Inflation_Rate'] = df['Log_CPI'].diff(12) * 100  # YoY Inflation
    df.dropna(inplace=True)
    
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.plot(df.index, df['Inflation_Rate'], color='#2C5282', linewidth=1.2)
    
    apply_cio_chart_standards(
        ax=ax,
        title="U.S. Consumer Price Index (CPI) Corporate Executive View",
        ylabel="Year-over-Year % Change",
        source_text="Source: Bureau of Labor Statistics via FRED (Series: CPIAUCSL)"
    )
    
    plt.tight_layout()
    plt.savefig('week_3_cpi_inflation.png', bbox_inches='tight')
    plt.close()
    print(" -> Success: 'week_3_cpi_inflation.png' exported.")


# -------------------------------------------------------------------------
# MODULE II EXERCISES (WEEKS 7-10)
# -------------------------------------------------------------------------

def run_week_7_exercise():
    """
    Weeks 7-8: Multivariate Dynamics (VAR Layout Array)
    Target: Macroeconomic Monetary Policy Array Setup
    """
    print("[Executing Week 7-8 Exercise] Building Multi-Variable VAR Matrix...")
    
    # Ingesting the 3-Variable Macro Desk Infrastructure System
    series_dict = {
        'FundsRate': 'FEDFUNDS',
        'Unemployment': 'UNRATE',
        'IndustrialProd': 'INDPRO'
    }
    
    macro_data = {}
    for var_name, series_id in series_dict.items():
        macro_data[var_name] = fred.get_series(series_id, start_date='2000-01-01')
        
    df = pd.DataFrame(macro_data)
    df.index.name = 'Date'
    df.dropna(inplace=True)
    
    # STUDENT TASK: Standardize metrics and check levels for non-stationarity
    # Visual Output checks correlation behavior for the CIO Desk Brief
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.plot(df.index, df['FundsRate'], color='#9B2C2C', linewidth=1.2, label='Fed Funds Rate')
    ax.plot(df.index, df['Unemployment'], color='#2B6CB0', linewidth=1.2, label='Unemployment Rate')
    
    apply_cio_chart_standards(
        ax=ax,
        title="Macroeconomic Policy Context Matrix: Policy Rate vs. Labor Slack",
        ylabel="Percentage (%)",
        source_text="Source: Board of Governors / BLS via FRED System"
    )
    ax.legend(frameon=False, loc='upper right', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('week_7_var_inputs.png', bbox_inches='tight')
    plt.close()
    print(" -> Success: 'week_7_var_inputs.png' exported.")


def run_week_9_exercise():
    """
    Weeks 9-10: Financial Volatility Models (ARCH/GARCH Engine)
    Target: High-Frequency Equity Returns Volatility Ingestion
    """
    print("[Executing Week 9-10 Exercise] Ingesting Market Data via Yahoo Finance...")
    
    # Ingesting S&P 500 Daily Market Closing Prices via yfinance API
    ticker = "^GSPC"
    data_raw = yf.download(ticker, start="2020-01-01", end="2026-10-15")
    
    df = pd.DataFrame(data_raw['Close'])
    df.columns = ['Close']
    
    # STUDENT TASK: Calculate daily log returns to isolate volatility clusters
    df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1)) * 100
    df.dropna(inplace=True)
    
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.plot(df.index, df['Log_Return'], color='#2D3748', linewidth=0.6, alpha=0.85)
    
    apply_cio_chart_standards(
        ax=ax,
        title="S&P 500 Index Daily Returns Matrix (Exhibiting Volatility Clustering)",
        ylabel="Daily Log Return (%)",
        source_text="Source: Yahoo Finance Data Engine (Ticker: ^GSPC)"
    )
    
    plt.tight_layout()
    plt.savefig('week_9_volatility_clusters.png', bbox_inches='tight')
    plt.close()
    print(" -> Success: 'week_9_volatility_clusters.png' exported.")


# -------------------------------------------------------------------------
# MODULE III CAPSTONE SHOCK ENGINE (WEEKS 13-14)
# -------------------------------------------------------------------------

def run_week_13_capstone_shock():
    """
    Weeks 13-14: Capstone Macro Desk Simulation Live Stress Test
    Target: Simulating an unannounced structural commodity market anomaly 
    """
    print("[Executing Week 13-14 Capstone] Initializing 48-Hour Live Desk Shock Production...")
    
    # Ingesting Crude Oil Futures to simulate the supply-side shock mechanism
    oil_data = yf.download("CL=F", start="2024-01-01", end="2026-10-17")
    df = pd.DataFrame(oil_data['Close'])
    df.columns = ['Oil_Price']
    df['Oil_Return'] = np.log(df['Oil_Price'] / df['Close'].shift(1)) * 100
    df.dropna(inplace=True)
    
    # Simulate an exogenous structural break point injection for student tracking
    shock_date = pd.to_datetime('2026-10-17')
    
    fig, ax = plt.subplots(figsize=(10, 4), dpi=300)
    ax.plot(df.index, df['Oil_Price'], color='#7B341E', linewidth=1.2)
    
    # Visual marker indicating where the 48-hour live out-of-sample test begins
    ax.axvline(shock_date, color='#E53E3E', linestyle=':', linewidth=1.5, label='Exogenous Shock Window')
    
    apply_cio_chart_standards(
        ax=ax,
        title="Capstone Simulation Framework: Exogenous Crude Oil Shock Window",
        ylabel="USD per Barrel (WTI Crude)",
        source_text="Source: NYMEX via Yahoo Finance Engine (Ticker: CL=F)"
    )
    ax.legend(frameon=False, loc='upper left', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('week_13_capstone_shock.png', bbox_inches='tight')
    plt.close()
    print(" -> Success: 'week_13_capstone_shock.png' exported.")


# -------------------------------------------------------------------------
# EXECUTION ORCHESTRATION PIPELINE
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("==================================================================")
    print("STARTING FLIPPED METRIC CURRICULUM AUTOMATION PIPELINE RUN")
    print("==================================================================")
    try:
        run_week_1_exercise()
        run_week_3_exercise()
        run_week_7_exercise()
        run_week_9_exercise()
        run_week_13_capstone_shock()
        print("\n==================================================================")
        print("PIPELINE COMPLETED SUCCESFULLY: All turn-key figures are generated.")
        print("==================================================================")
    except Exception as e:
        print(f"\n[Execution Error] Pipeline execution halted: {str(e)}")
        print("Verify your FRED_API_KEY environment configuration baseline.")
"""