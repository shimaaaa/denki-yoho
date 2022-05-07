import { Configuration, DefaultApi } from './api_client_tools/index';
import { AreaDemandForecast, DemandForecastData } from './models/forecast';

export class DenkiYohoApiClient {

  private static getClient() {
    const conf = new Configuration({
      basePath: 'http://localhost:8000',
    });
    return new DefaultApi(conf);
  }

  static async listForcasts(): Promise<Array<AreaDemandForecast>> {
    const api = DenkiYohoApiClient.getClient();
    const response = await api.forecastListApiForecastGet();
    return response.data.map(x => {
      const hourlyData = x.hourlyForecastList.map(y => {
        return new DemandForecastData({
          area: y.area,
          dateTime: y.dt,
          actualResult: y.actualResult,
          forecastDemand: y.forecastDemand,
          forecastSupply: y.forecastSupply
        });
      });
      const peakDemand = new DemandForecastData({
        area: x.peakDemand.area,
        dateTime: x.peakDemand.dt,
        actualResult: x.peakDemand.actualResult,
        forecastDemand: x.peakDemand.forecastDemand,
        forecastSupply: x.peakDemand.forecastSupply
      })
      const peakUsage = new DemandForecastData({
        area: x.peakUsage.area,
        dateTime: x.peakUsage.dt,
        actualResult: x.peakUsage.actualResult,
        forecastDemand: x.peakUsage.forecastDemand,
        forecastSupply: x.peakUsage.forecastSupply
      })
      return new AreaDemandForecast({
        area: x.area,
        hourlyForecastList: hourlyData,
        peakDemand: peakDemand,
        peakUsage: peakUsage,
      });
    });

    // const demandForecasts = response.demand.map(x => {
    //   return new Forecast({
    //     area: x.area,
    //     hour24: x.hour24,
    //     maxDemandKw: x.maxDemandKw,
    //     supplyKw: x.supplyKw,
    //   })
    // });
    // const usageForecasts = response.usage.map(x => {
    //   return new Forecast({
    //     area: x.area,
    //     hour24: x.hour24,
    //     maxDemandKw: x.maxDemandKw,
    //     supplyKw: x.supplyKw,
    //   })
    // });
    // return new ForecastData({
    //   demand: demandForecasts,
    //   usage: usageForecasts,
    // })
  }
}
