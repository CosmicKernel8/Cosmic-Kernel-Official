def update_energy_budget(self, new_address_space):
    """
    [v2.8.6 Patch] Landauer's Principle Extension
    주소 공간 확장 시 소모되는 최소 연산 비용(E_scaling)을 계산하여 
    전체 에너지 무결성을 유지함.
    """
    # delta_address = 현재 공간 - 이전 공간
    delta_address = new_address_space - self.last_address_space
    # E = delta_S * kT * ln(2) 기반 연산
    energy_cost = delta_address * self.k_boltzmann * self.temperature * math.log(2)

    if self.vacuum_energy >= energy_cost:
        self.vacuum_energy -= energy_cost
        self.address_space = new_address_space
        return True
    return False # 에너지 부족 시 확장 중단 (Soft-lock)
