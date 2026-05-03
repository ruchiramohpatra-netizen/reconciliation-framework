# Reconciliation Framework

## Project Overview
A modular, class-based reconciliation framework for comparing Gold and Bronze tables in a Data Lakehouse environment.

## Architecture

### Core Components

| Component | Responsibility |
|-----------|---------------|
| **Orchestrator** | Single entry point, binds all modules |
| **ReconContext** | Single source of truth for each run |
| **GoldMetadata** | BDM mapping logic (only source of truth) |
| **QueryBuilder** | Builds Gold/Bronze queries |
| **ReconExecutor** | Executes reconciliation logic |
| **ReconOutputDB** | Persists 5 output tables independently |

### Output Tables
1. `recon_run` - Run summary statistics (parent)
2. `duplicate_check` - Duplicate business key records
3. `column_match` - Column-level match/mismatch status
4. `mismatch_summary` - Aggregated mismatch counts per column
5. `unique_detail` - Records unique to Gold or Bronze

## Key Design Principles
- Orchestrator has NO business logic - only calls modules
- BDM mapping logic in GoldMetadata ONLY (not duplicated)
- Each output table has independent write method
- ReconContext passed to all modules as single source of truth

## Tech Stack
- PySpark for data processing
- Delta Lake for storage
- Databricks for execution
- pytest for unit testing

## Key Highlights

- Modular OOP design with single source of truth (ReconContext)
- Orchestrator only binds modules, no business logic
- BDM mapping logic not duplicated across files
- Independent persistence methods for each output table
- PySpark integration with Delta Lake

## Running the Project

### Setup
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
