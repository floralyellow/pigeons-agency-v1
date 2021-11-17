import { Pigeon } from "./pigeon";
import { User } from "./user";

export class Expedition {
  user :User
  droppings_minute?: number
  nb_pigeons?: number
  expeditions: Pigeon[]
}
