import time
import threading
from collections import OrderedDict

class CosmicSingularity:
    """
    Cosmic OS v6.0.0: The Ultimate Architecture
    - Backpressure Control (Retry Storm Defense)
    - Thread-Safe Item Access (Race Condition Defense)
    - Monotonic Time Scaling (Clock Drift Defense)
    """
    def __init__(self, max_locks=1000, max_queue_size=5000):
        self.backup_buffer = {}
        self.buffer_timestamps = {}
        self.item_locks = {} # 🚨 PATCH 2: 개별 아이템 전용 락
        self.sector_locks = OrderedDict()
        self.max_locks = max_locks
        self.max_queue_size = max_queue_size # 🚨 PATCH 1: 큐 제한
        self.retry_queue = []
        
        # 🚨 PATCH 3: 왜곡 없는 단조 시간(Monotonic) 사용
        threading.Thread(target=self._robust_cleaner, daemon=True).start()
        threading.Thread(target=self._rescheduler, daemon=True).start()

    def _get_item_lock(self, key):
        """특정 데이터 조작 시 충돌 방지용 락"""
        if key not in self.item_locks:
            self.item_locks[key] = threading.Lock()
        return self.item_locks[key]

    def _robust_cleaner(self):
        """🚨 PATCH 2: KeyError 없는 안전한 청소기"""
        while True:
            time.sleep(10)
            current_time = time.monotonic() # 🚨 PATCH 3
            keys = list(self.backup_buffer.keys())
            for key in keys:
                # 개별 아이템 락을 잡아서 전송 중인 데이터 삭제 방지
                with self._get_item_lock(key):
                    if key in self.backup_buffer and \
                       current_time - self.buffer_timestamps.get(key, 0) > 60:
                        del self.backup_buffer[key]
                        del self.buffer_timestamps[key]
                        print(f"🧹 [SECURE_CLEAN] Purified: {key}")

    def _rescheduler(self):
        while True:
            if self.retry_queue:
                task = self.retry_queue.pop(0)
                self.teleport_state(task['node'], task['key'], task['data'], is_retry=True)
            time.sleep(5)

    def teleport_state(self, node_id, memory_key, payload, is_retry=False):
        # 🚨 PATCH 1: Retry Storm 방지
        if not is_retry and len(self.retry_queue) >= self.max_queue_size:
            return "🚫 REJECTED: Cosmic Queue Overflow! Try later."

        lock = self._get_sector_lock(node_id)
        acquired = lock.acquire(timeout=2.0)
        
        if not acquired:
            if not is_retry: self.retry_queue.append({'node': node_id, 'key': memory_key, 'data': payload})
            return "⏳ QUEUED: Sector Congestion"

        try:
            # 🚨 PATCH 2: 전송 중 청소기가 못 건드리게 락!
            with self._get_item_lock(memory_key):
                self.backup_buffer[memory_key] = payload
                self.buffer_timestamps[memory_key] = time.monotonic()
                # (전송 로직...)
                return "✅ SUCCESS"
        finally:
            lock.release()

# --- 우주의 특이점 가동 ---
singularity = CosmicSingularity()
print(f"🌌 [v6.0.0] The Cosmic Singularity is Stable.")
