
import { getAreaValueFromKey } from '../constants';

export class AreaDemandForecast {
  area: string
  hourlyForecastList: Array<DemandForecastData>
  peakDemand: DemandForecastData
  peakUsage: DemandForecastData

  constructor(props: {
    area: string
    hourlyForecastList: Array<DemandForecastData>
    peakDemand: DemandForecastData
    peakUsage: DemandForecastData
  }) {
    this.area = props.area
    this.hourlyForecastList = props.hourlyForecastList
    this.peakDemand = props.peakDemand
    this.peakUsage = props.peakUsage
  }
  public get areaLabel(): string {
    return getAreaValueFromKey(this.area);
  }
}

export class DemandForecastData {
  area: string
  dateTime: Date
  actualResult: number
  forecastDemand: number
  forecastSupply: number

  constructor(props: {
    area: string,
    dateTime: Date,
    actualResult: number,
    forecastDemand: number,
    forecastSupply: number
  }) {
    this.area = props.area
    this.dateTime = props.dateTime
    this.actualResult = props.actualResult
    this.forecastDemand = props.forecastDemand
    this.forecastSupply = props.forecastSupply
  }
}


// export class Forecast {
//   area: string
//   hour24: number
//   maxDemandKw: number
//   supplyKw: number

//   constructor(props: {
//       area: string,
//       hour24: number,
//       maxDemandKw: number,
//       supplyKw: number,
//   }) {
//     this.area = props.area;
//     this.hour24 = props.hour24;
//     this.maxDemandKw = props.maxDemandKw;
//     this.supplyKw = props.supplyKw;
//   }

//   public get areaLabel(): string {
//     return getAreaValueFromKey(this.area);
//   }

//   public get ratioPc(): number {
//     return Math.round(this.maxDemandKw / this.supplyKw * 100);
//   }

//   public get hourRangeLabel(): string {
//     let end = 0;
//     if (this.hour24 <= 24) {
//       end = this.hour24 + 1;
//     }
//     return `${this.hour24}時～${end}時`;
//   }
// }

// export class ForecastData {
//   demand: Array<Forecast>
//   usage: Array<Forecast>
//   constructor(
//     props: {
//       demand: Array<Forecast>,
//       usage: Array<Forecast>,
//     }
//   ) {
//     this.demand = props.demand;
//     this.usage = props.usage;
//   }
// }
