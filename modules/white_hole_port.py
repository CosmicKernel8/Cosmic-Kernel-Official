 import math

class WhiteHolePort:
    """
    [v3.0.1] White Hole Output Port Module
    Description: 블랙홀 GC에서 정제된 공간 자원을 배출하는 출력 포트.
    Patch v3.0.1: 시공간 충돌 방지 및 무결성 체크 로직(Space Integrity Check) 추가.
    """
    def __init__(self, emission_efficiency=0.99):
        self.efficiency = emission_efficiency
        self.total_emitted_space = 0
        self.is_port_open = True
        self.current_space_density = 0.5 # 초기 시공간 밀도 상태

    def check_space_density_overflow(self):
        """
        [v3.0.1 Patch] 시공간 무결성 체크
        현재 공간의 밀도가 너무 낮거나(과팽창) 구조적 한계를 넘었는지 확인.
        """
        # 밀도가 임계치 이하로 떨어지면(너무 넓어지면) 오버플로우로 간주
        return self.current_space_density < 0.1

    def emit_purified_space(self, processed_entropy):
        """
        압축된 엔트로피를 순수 공간 자원으로 변환하여 배출함.
        """
        if not self.is_port_open:
            return "Error: Port Closed"

        # 자원 변환 과정 (Entropy to Space Resource)
        emitted_resource = processed_entropy * self.efficiency
        
        # [v3.0.1 Patch] 충돌 방지 및 트래픽 셰이핑 적용
        emitted_resource = self._apply_traffic_shaping(emitted_resource)
        
        self.total_emitted_space += emitted_resource
        return emitted_resource

    def _apply_traffic_shaping(self, resource_amount):
        """
        [v3.0.1 Patch] 시공간 무결성 및 충돌 방지 로직
        공간이 이미 너무 넓거나 불안정하면 방출 속도를 낮추어 시스템 붕괴를 막음.
        """
        if self.check_space_density_overflow():
            # 공간이 이미 너무 넓으면 방출 속도를 50%로 제한 (가속 팽창 제어)
            resource_amount *= 0.5 
            print("[AUTO-ADJUST] Expansion Rate Throttled to preserve Integrity.")
        
        if resource_amount > 10000:
            print("[WARN] High Emission Rate. Monitoring Space Fabric Tension.")
            
        return resource_amount

# 시뮬레이션 활용 예시
# port = WhiteHolePort()
# new_space = port.emit_purified_space(processed_entropy=5000)
