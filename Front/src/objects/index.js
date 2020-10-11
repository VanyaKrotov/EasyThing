export class Coords {
  constructor({ latitude = 0.0, longitude = 0.0 } = {}) {
    this.latitude = latitude;
    this.longitude = longitude;
  }
}

export class Location {
  constructor() {
    this.coords = new Coords();
    this.country = '';
    this.adress = '';
  }
}
