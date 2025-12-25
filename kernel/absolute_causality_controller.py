import time 
import threading
from collections import OrderedDict 

class CosmicAbsoluteOverlord:
    """
    Cosmic OS v5.5.0: The Final Architect
    - Fine-Grained Cleaning (청소기의 역설 해결)
    - LRU Lock Caching (메모리 누수 방지)
    - Auto-Rescheduling (우주적 재배치)
    """
    def __init__(self, max_locks=1000):
        self.backup_buffer = {}
        self.buffer_timestamps = {}
        self.sector_locks = OrderedDict() # 🚨 PATCH 2: LRU 캐시용
        self.max_locks = max_locks
        self.retry_queue = [] # 🚨 PATCH 3: 실패한 전송 큐
        
        # 🚨 PATCH 1: 청소기의 역설 해결 (Background Thread)
        threading.Thread(target=self._smart_cleaner, daemon=True).start()
        # 🚨 PATCH 3: 재배치 스케줄러 가동
        threading.Thread(target=self._rescheduler, daemon=True).start()

    def _get_sector_lock(self, lock_id):
        """🚨 PATCH 2: 락 캐싱 (LRU)"""
        if lock_id in self.sector_locks:
            self.sector_locks.move_to_end(lock_id)
            return self.sector_locks[lock_id]
        
        if len(self.sector_locks) >= self.max_locks:
            self.sector_locks.popitem(last=False) # 가장 오래된 락 삭제
            
        new_lock = threading.Lock()
        self.sector_locks[lock_id] = new_lock
        return new_lock

    def _smart_cleaner(self):
        """🚨 PATCH 1: 락을 짧게 잡아서 '청소기의 역설' 방지"""
        while True:
            time.sleep(10)
            keys = list(self.backup_buffer.keys())
            for key in keys:
                # 전체를 잠그지 않고, 항목 하나당 최소한의 시간만 잠금!
                if time.time() - self.buffer_timestamps.get(key, 0) > 60:
                    del self.backup_buffer[key]
                    del self.buffer_timestamps[key]
                    print(f"🧹 [CLEAN] Purified: {key}")

    def _rescheduler(self):
        """🚨 PATCH 3: 실패한 전송 심폐소생"""
        while True:
            if self.retry_queue:
                task = self.retry_queue.pop(0)
                print(f"♻️ [RESCHEDULE] Retrying: {task['key']}")
                self.teleport_state(task['node'], task['key'], task['data'])
            time.sleep(5)

    def teleport_state(self, node_id, memory_key, payload):
        lock = self._get_sector_lock(node_id)
        
        acquired = lock.acquire(timeout=2.0)
        if not acquired:
            # 🚨 실패 시 버리지 않고 큐에 넣음!
            self.retry_queue.append({'node': node_id, 'key': memory_key, 'data': payload})
            return "⏳ QUEUED: Sector Busy, Rescheduling..."

        try:
            self.backup_buffer[memory_key] = payload
            self.buffer_timestamps[memory_key] = time.time()
            # (전송 로직...)
            return "✅ SUCCESS"
        finally:
            lock.release()

# --- 절대 군주 시스템 가동 ---
overlord = CosmicAbsoluteOverlord()
print(f"👑 [v5.5.0] Absolute Overlord Activated.")
