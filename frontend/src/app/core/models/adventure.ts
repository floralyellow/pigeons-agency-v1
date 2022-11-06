import * as internal from "events"
import { Player } from "./player"

export class Adventure {
    player : number
    lvl : number
    encounter : number
    nb_tries : number
    is_success = false
    reward_droppings = 0
    created_at : Date
    completed_at = Date
}
