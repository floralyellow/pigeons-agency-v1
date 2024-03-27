export interface Player {
  id: number
  lvl: number
  seeds: number
  droppings: number
  feathers: number
  military_score: number
  last_attacked: number
  time_last_attack: Date
  defense_team: 'A' | 'B'
  protected_until: Date
  is_dark_mode :boolean
  is_tutorial_done : boolean
  nb_notifs :number
}

