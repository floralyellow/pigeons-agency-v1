import { Injectable } from '@angular/core';
import {Pigeon} from '../models/pigeon'

@Injectable({
  providedIn: 'root'
})
export class PigeonsService {

  constructor() { }

  getClassToApply(pigeon : Pigeon) {
    if (pigeon.luck > 93) {
      return 'legendary'
    } else if (pigeon.luck > 78) {
      return 'epic'
    } else if (pigeon.luck > 48) {
      return 'rare'
    } else if (pigeon.luck > 18) {
      return 'uncommon'
    } else {
      return ''
    }
  }

  getStars(pigeon : Pigeon) {
    if (pigeon.luck > 93) {
      return 5;
    } else if (pigeon.luck > 78) {
      return 4;
    } else if (pigeon.luck > 48) {
      return 3;
    } else if (pigeon.luck > 18) {
      return 2;
    } else {
      return 1;
    }
  }

  getPigeonType(pigeon : Pigeon) {
    switch (pigeon.pigeon_type) {
      case 1:
        return 'faFistRaised';
      case 2:
        return 'faHatWizard';
      case 3:
        return 'faShieldAlt';
    }
  }
}
