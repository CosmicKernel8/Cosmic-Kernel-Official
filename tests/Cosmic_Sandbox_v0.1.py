# --- [Cosmic_Sandbox_v0.1.py] ---

# 모듈 불러오기 (실제 GitHub에서는 경로에 맞춰 import 해야 합니다)
# 예를 들어, src/ 아래에 있다면 from src.cosmic_core import CosmicCore
# 여기서는 편의상 동일 레벨에 있다고 가정합니다.
from cosmic_core import CosmicCore
from cosmic_kernel import CosmicKernel
from thermal_manager import ThermalManager
from white_hole_port import WhiteHolePort
from cosmic_stabilizer import CosmicStabilizer
from Cosmic_Expansion_Engine import CosmicExpansionEngine # 주의: 파일명 대소문자 확인!

print("[SANDBOX] Initializing Cosmic OS v3.5.0 Simulation...")

# 1. 핵심 모듈 인스턴스 생성
core = CosmicCore()
thermal_manager = ThermalManager()
white_hole = WhiteHolePort()
stabilizer = CosmicStabilizer()
expansion_engine = CosmicExpansionEngine()

# 2. CosmicKernel에 모든 모듈 주입
# Kernel은 모든 모듈의 Orchestrator 역할을 합니다.
kernel = CosmicKernel(core, expansion_engine, white_hole, thermal_manager)

# 3. 샌드박스 설정: 작은 가상 우주 시뮬레이션 파라미터
initial_density = 1.0       # 초기 우주 밀도 (가상 값)
simulation_cycles = 5       # 시뮬레이션 반복 횟수
cluster_id_a = "Andromeda_Galaxy" # 시뮬레이션할 은하 클러스터 ID

print(f"[SANDBOX] Running {simulation_cycles} cycles for Cluster: {cluster_id_a}")
print("-" * 50)

# 4. 시뮬레이션 루프 실행
for cycle in range(simulation_cycles):
    # 커널의 메인 업데이트 사이클 호출
    # input_density와 cluster_id는 매 사이클마다 전달됩니다.
    kernel.update_universe_cycle(initial_density, cluster_id_a)
    
    # 시뮬레이션 데이터 변화 (임의로 값 조정)
    initial_density *= (1.0 + kernel.expansion_engine.total_address_space / 1e15) # 팽창에 따라 밀도 변화
    thermal_manager.total_heat_dissipated += (initial_density * 1e25) # 열 누적 시뮬레이션
    
    # 5. 각 사이클 후 상태 모니터링
    # kernel.monitor.render_system_health()는 update_universe_cycle 내부에서 호출됩니다.
    time.sleep(0.5) # 각 사이클 사이 0.5초 대기

print("-" * 50)
print("[SANDBOX] Simulation Complete. Check Cosmic OS Dashboard for Final Status.")
print(f"[SANDBOX] Total Universe Time Elapsed: {kernel.current_time} cycles.")

# 최종 커널 상태 요약
kernel.monitor.render_system_health()
