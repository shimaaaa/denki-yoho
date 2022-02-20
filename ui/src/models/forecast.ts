import { Area, getAreaValueFromKey } from '../constants';

export class Forecast {
  area: string
  hour24: number
  maxDemandKw: number
  supplyKw: number

  constructor(props: {
      area: string,
      hour24: number,
      maxDemandKw: number,
      supplyKw: number,
  }) {
    this.area = props.area;
    this.hour24 = props.hour24;
    this.maxDemandKw = props.maxDemandKw;
    this.supplyKw = props.supplyKw;
  }

  public get areaLabel(): string {
    return getAreaValueFromKey(this.area);
  }

  public get ratioPc(): number {
    return Math.round(this.maxDemandKw / this.supplyKw * 100);
  }

  public get hourRangeLabel(): string {
    let end = 0;
    if (this.hour24 <= 24) {
      end = this.hour24 + 1;
    }
    return `${this.hour24}時～${end}時`;
  }
}

export class ForecastData {
  demand: Array<Forecast>
  usage: Array<Forecast>
  constructor(
    props: {
      demand: Array<Forecast>,
      usage: Array<Forecast>,
    }
  ) {
    this.demand = props.demand;
    this.usage = props.usage;
  }
}
