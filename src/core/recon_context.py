import uuid
from datetime import datetime


class ReconContext:
    """Single source of truth for reconciliation run."""
    
    def __init__(self, business_date, gold_table_name):
        self.business_date = business_date
        self.gold_table_name = gold_table_name
        self.job_run_id = str(uuid.uuid4())
        self.start_time = datetime.now()
        self.gold_attr_list = None
        self.bronze_tables = None
        self.gold_query = None
        self.bronze_queries = {}
        self.gold_df = None
        self.comparison_dfs = {}
        self.duplicate_df = None
        self.reconcilable_columns = []
        self.deferred_columns = []
        self.unmapped_reason = {}
        self.gold_row_count = 0
        self.bronze_row_counts = {}
        self.match_counts = {}
        self.mismatch_counts = {}
        self.status = "RUNNING"
        self.error_message = None
        self.end_time = None
    
    def add_deferred_column(self, column_name, reason):
        self.deferred_columns.append(column_name)
        self.unmapped_reason[column_name] = reason
    
    def complete_run(self, status="SUCCESS"):
        self.status = status
        self.end_time = datetime.now()
    
    def to_dict(self):
        return {
            "job_run_id": self.job_run_id,
            "business_date": self.business_date,
            "gold_table_name": self.gold_table_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.status,
            "gold_row_count": self.gold_row_count,
            "deferred_columns": ",".join(self.deferred_columns),
            "error_message": self.error_message
        }
