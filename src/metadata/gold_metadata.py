import logging
from typing import List

logger = logging.getLogger(__name__)


class GoldMetadata:
    """Owner of column-level metadata. BDM logic ONLY here."""
    
    def __init__(self, context, spark):
        self.context = context
        self.spark = spark
        self.all_columns = []
        self.bdm_mapped_columns = []
        self.unmapped_columns = []
    
    def load_metadata(self):
        logger.info(f"Loading metadata for: {self.context.gold_table_name}")
        self.all_columns = self._fetch_all_columns()
        self.bdm_mapped_columns = [col for col in self.all_columns if self._is_bdm_mapped(col)]
        self.unmapped_columns = [col for col in self.all_columns if not self._is_bdm_mapped(col)]
        self._log_unmapped_columns()
        return self.bdm_mapped_columns
    
    def _fetch_all_columns(self):
        df = self.spark.table(self.context.gold_table_name)
        return df.columns
    
    def _is_bdm_mapped(self, column_name):
        return True  # Placeholder - implement actual logic
    
    def _log_unmapped_columns(self):
        for col in self.unmapped_columns:
            self.context.add_deferred_column(col, "No BDM mapping found")
    
    def get_reconcilable_columns(self) -> List[str]:
        return self.bdm_mapped_columns
    
    def get_deferred_columns(self) -> List[str]:
        return self.unmapped_columns
