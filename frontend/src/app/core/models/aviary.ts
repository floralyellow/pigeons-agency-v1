import { Pigeon } from "./pigeon";
import { User } from "./user";

export interface Aviary {
  user: User
  pigeons: Pigeon[]
}
