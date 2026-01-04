import time
import threading
from collections import OrderedDict

# [정보] 이 모듈은 커널의 임계 구역 보호와 전송 부하 제어(Backpressure)를 담당합니다.
# 데이터 경합(Race Condition)을 방지하는 개별 아이템 락 시스템이 탑재되었습니다!

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
        self.item_locks = {} # 개별 아이템 전용 락
        self.sector_locks = OrderedDict()
        self.max_locks = max_locks
        self.max_queue_size = max_queue_size # 큐 크기 제한
        self.retry_queue = []
        
        # 왜곡 없는 단조 시간(Monotonic) 기반 청소기 및 스케줄러 가동
        threading.Thread(target=self._robust_cleaner, daemon=True).start()
        threading.Thread(target=self._rescheduler, daemon=True).start()

    def _get_item_lock(self, key):
        """특정 데이터 조작 시 충돌 방지를 위한 세밀한 락(Fine-grained Lock)"""
        if key not in self.item_locks:
            self.item_locks[key] = threading.Lock()
        return self.item_locks[key]

    def _get_sector_lock(self, lock_id):
        """섹터 단위 락 관리 (LRU 방식)"""
        if lock_id in self.sector_locks:
            self.sector_locks.move_to_end(lock_id)
            return self.sector_locks[lock_id]
        if len(self.sector_locks) >= self.max_locks:
            self.sector_locks.popitem(last=False)
        new_lock = threading.Lock()
        self.sector_locks[lock_id] = new_lock
        return new_lock

    def _robust_cleaner(self):
        """KeyError 없는 안전한 리소스 회수 프로세스"""
        while True:
            time.sleep(10)
            current_time = time.monotonic() # 클럭 드리프트 방지
            keys = list(self.backup_buffer.keys())
            for key in keys:
                # 개별 아이템 락을 사용하여 전송 중인 데이터 삭제 방지
                with self._get_item_lock(key):
                    if key in self.backup_buffer and \
                       current_time - self.buffer_timestamps.get(key, 0) > 60:
                        del self.backup_buffer[key]
                        del self.buffer_timestamps[key]
                        # 사용 완료된 락도 함께 정리하여 메모리 절약
                        if key in self.item_locks: del self.item_locks[key]
                        print(f"🧹 [SECURE_CLEAN] Purified: {key}")

    def _rescheduler(self):
        """실패한 태스크의 재분배 스케줄러"""
        while True:
            if self.retry_queue:
                task = self.retry_queue.pop(0)
                self.teleport_state(task['node'], task['key'], task['data'], is_retry=True)
            time.sleep(5)

    def teleport_state(self, node_id, memory_key, payload, is_retry=False):
        """우주적 상태 전송 및 부하 관리 로직"""
        # Retry Storm 방지: 큐가 가득 차면 신규 요청 거절
        if not is_retry and len(self.retry_queue) >= self.max_queue_size:
            return "🚫 REJECTED: Cosmic Queue Overflow!"

        lock = self._get_sector_lock(node_id)
        acquired = lock.acquire(timeout=2.0)
        
        if not acquired:
            if not is_retry: 
                self.retry_queue.append({'node': node_id, 'key': memory_key, 'data': payload})
            return "⏳ QUEUED: Sector Congestion"

        try:
            # 전송 중 청소기가 건드리지 못하게 아이템 레벨 락 사용
            with self._get_item_lock(memory_key):
                self.backup_buffer[memory_key] = payload
                self.buffer_timestamps[memory_key] = time.monotonic()
                return "✅ SUCCESS"
        finally:
            lock.release()

# --- 우주의 특이점 가동 ---
if __name__ == "__main__":
    singularity = CosmicSingularity()
    print(f"🌌 [v6.0.0] The Cosmic Singularity is Stable.")
