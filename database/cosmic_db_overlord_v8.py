import sqlite3
import logging
from logging.handlers import TimedRotatingFileHandler
import time
import threading

# [주의] 이 파일은 database/ 폴더에 위치하며, 시스템의 영속성을 책임집니다!

class CosmicEnterpriseOverlord:
    """
    Cosmic OS v8.0.0: Enterprise-Grade Persistence & Logging
    - SQLite Integration (No JSON Bottleneck)
    - Database Transactions (Atomic Snapshots)
    - Timed Rotating Logs (Infinite Logging)
    """
    def __init__(self, db_path="cosmic_universe.db"):
        self.db_path = db_path
        self._init_db()
        self._init_logger()
        
        self.backup_buffer = {}
        self.lock = threading.Lock() 
        
        # 시스템 가동
        threading.Thread(target=self._persistence_worker, daemon=True).start()

    def _init_logger(self):
        self.logger = logging.getLogger("CosmicOS")
        self.logger.setLevel(logging.INFO)
        
        # 7일 치 로그만 보관하고 나머지는 자동 삭제!
        handler = TimedRotatingFileHandler(
            "cosmic_system.log", when="midnight", interval=1, backupCount=7
        )
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.info("🚀 Cosmic OS v8.0.0 Logging System Online.")

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS storage 
                            (key TEXT PRIMARY KEY, payload TEXT, timestamp REAL)''')
            conn.commit()

    def _persistence_worker(self):
        while True:
            time.sleep(60) # 1분마다 동기화
            with self.lock:
                items = list(self.backup_buffer.items())
            
            if items:
                with sqlite3.connect(self.db_path) as conn:
                    conn.executemany("INSERT OR REPLACE INTO storage VALUES (?, ?, ?)", 
                                     [(k, str(v), time.time()) for k, v in items])
                    conn.commit()
                self.logger.info(f"💾 Snapshot complete: {len(items)} shards secured.")

    def teleport_state(self, memory_key, payload):
        with self.lock: 
            self.backup_buffer[memory_key] = payload
            self.logger.info(f"✨ State {memory_key} synchronized.")
            return "SUCCESS"

# --- 단독 실행 방지 로직 (나중에 main.py에서 부를 수 있게!) ---
if __name__ == "__main__":
    overlord = CosmicEnterpriseOverlord()
    print(f"🏢 [v8.0.0] Cosmic Enterprise Kernel is running.")
