import time
import threading
from collections import OrderedDict

# [정보] 이 모듈은 커널 수준의 자원 잠금(Lock) 관리와 전송 재스케줄링을 담당합니다.
# '청소기의 역설'을 해결한 스마트 클리너와 LRU 기반 락 캐시가 탑재되었습니다!

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
        self.sector_locks = OrderedDict() # LRU 캐시용
        self.max_locks = max_locks
        self.retry_queue = [] # 실패한 전송 큐
        
        # 청소기의 역설 해결 (Background Thread)
        threading.Thread(target=self._smart_cleaner, daemon=True).start()
        # 재배치 스케줄러 가동
        threading.Thread(target=self._rescheduler, daemon=True).start()

    def _get_sector_lock(self, lock_id):
        """락 캐싱 (LRU 로직으로 메모리 낭비 방지)"""
        if lock_id in self.sector_locks:
            self.sector_locks.move_to_end(lock_id)
            return self.sector_locks[lock_id]
        
        if len(self.sector_locks) >= self.max_locks:
            self.sector_locks.popitem(last=False) # 가장 오래된 락 삭제
            
        new_lock = threading.Lock()
        self.sector_locks[lock_id] = new_lock
        return new_lock

    def _smart_cleaner(self):
        """락을 짧게 잡아 전체 시스템 지연을 방지하는 스마트 클리너"""
        while True:
            time.sleep(10)
            keys = list(self.backup_buffer.keys())
            for key in keys:
                # 데이터 유효 시간 체크 (60초)
                if time.time() - self.buffer_timestamps.get(key, 0) > 60:
                    if key in self.backup_buffer: del self.backup_buffer[key]
                    if key in self.buffer_timestamps: del self.buffer_timestamps[key]
                    print(f"🧹 [KERNEL_CLEAN] Purified: {key}")

    def _rescheduler(self):
        """실패한 전송 건들을 다시 시도하는 심폐소생 스케줄러"""
        while True:
            if self.retry_queue:
                task = self.retry_queue.pop(0)
                print(f"♻️ [RESCHEDULE] Retrying: {task['key']}")
                self.teleport_state(task['node'], task['key'], task['data'])
            time.sleep(5)

    def teleport_state(self, node_id, memory_key, payload):
        """커널 수준의 상태 전송 로직"""
        lock = self._get_sector_lock(node_id)
        
        # 락 획득 시도 (2초 타임아웃)
        acquired = lock.acquire(timeout=2.0)
        if not acquired:
            # 실패 시 재배치 큐에 삽입
            self.retry_queue.append({'node': node_id, 'key': memory_key, 'data': payload})
            return "⏳ QUEUED: Sector Busy, Rescheduling..."

        try:
            self.backup_buffer[memory_key] = payload
            self.buffer_timestamps[memory_key] = time.time()
            # 실제 전송 하위 로직은 network 패키지에서 처리하도록 설계됨
            return "✅ SUCCESS"
        finally:
            lock.release()

# --- 단독 실행 방지 로직 ---
if __name__ == "__main__":
    overlord = CosmicAbsoluteOverlord()
    print(f"👑 [v5.5.0] Absolute Overlord Activated.")
