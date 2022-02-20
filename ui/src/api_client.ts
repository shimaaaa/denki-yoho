import { DefaultApi, Configuration } from './api_client_tools/index'
import { Forecast, ForecastData } from './models/forecast'

export class DenkiYohoApiClient {

  private static getClient() {
    const conf = new Configuration({
      basePath: 'http://127.0.0.1:8000',
    });
    return new DefaultApi(conf);
  }

  static async listForcasts(): Promise<ForecastData> {
    const api = DenkiYohoApiClient.getClient();
    const response = await api.forecastListApiForecastGet();
    const demandForecasts = response.demand.map(x => {
      return new Forecast({
        area: x.area,
        hour24: x.hour24,
        maxDemandKw: x.maxDemandKw,
        supplyKw: x.supplyKw,
      })
    });
    const usageForecasts = response.usage.map(x => {
      return new Forecast({
        area: x.area,
        hour24: x.hour24,
        maxDemandKw: x.maxDemandKw,
        supplyKw: x.supplyKw,
      })
    });
    return new ForecastData({
      demand: demandForecasts,
      usage: usageForecasts,
    })
  }
}
