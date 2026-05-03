import logging
from src.core.recon_context import ReconContext

logger = logging.getLogger(__name__)


class Orchestrator:
    """Main orchestrator - only binds modules together."""
    
    def __init__(self, business_date: str, gold_table_name: str, spark_session):
        self.business_date = business_date
        self.gold_table_name = gold_table_name
        self.spark = spark_session
        self.ctx = ReconContext(business_date, gold_table_name)
    
    def run(self):
        """Single entry point - does everything."""
        try:
            logger.info(f"Starting reconciliation run: {self.ctx.job_run_id}")
            logger.info(f"Business Date: {self.business_date}")
            logger.info(f"Gold Table: {self.gold_table_name}")
            
            self._load_metadata()
            self._map_attributes()
            self._build_queries()
            self._execute_recon()
            self._check_duplicates()
            self._persist_outputs()
            
            self.ctx.complete_run("SUCCESS")
            logger.info(f"Reconciliation completed: {self.ctx.job_run_id}")
            
        except Exception as e:
            self.ctx.complete_run("FAILED")
            self.ctx.error_message = str(e)
            logger.error(f"Reconciliation failed: {str(e)}")
            raise
    
    def _load_metadata(self):
        logger.info("Step 1: Loading metadata")
    
    def _map_attributes(self):
        logger.info("Step 2: Mapping attributes")
    
    def _build_queries(self):
        logger.info("Step 3: Building queries")
    
    def _execute_recon(self):
        logger.info("Step 4: Executing reconciliation")
    
    def _check_duplicates(self):
        logger.info("Step 5: Checking duplicates")
    
    def _persist_outputs(self):
        logger.info("Step 6: Persisting outputs")
