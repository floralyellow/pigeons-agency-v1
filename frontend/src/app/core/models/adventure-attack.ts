export interface AdventureAttack {
    id: number;
    atk_tot_score: number;
    atk_tot_phys: number;
    atk_tot_magic: number;
    atk_shield_value: number;
    atk_shield_blocs: number;
    def_tot_score: number;
    def_tot_phys: number;
    def_tot_magic: number;
    def_shield_value: number;
    def_shield_blocs: number;
    created_at: Date;
    is_victory: boolean;
    attacker: number;
    adventure: number;
}
