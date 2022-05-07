/* tslint:disable */
/* eslint-disable */
/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    Area,
    AreaFromJSON,
    AreaFromJSONTyped,
    AreaToJSON,
} from './Area';
import {
    DemandForecast,
    DemandForecastFromJSON,
    DemandForecastFromJSONTyped,
    DemandForecastToJSON,
} from './DemandForecast';

/**
 * 
 * @export
 * @interface AreaDemandForecast
 */
export interface AreaDemandForecast {
    /**
     * 
     * @type {Area}
     * @memberof AreaDemandForecast
     */
    area: Area;
    /**
     * 
     * @type {Array<DemandForecast>}
     * @memberof AreaDemandForecast
     */
    hourlyForecastList: Array<DemandForecast>;
    /**
     * 
     * @type {DemandForecast}
     * @memberof AreaDemandForecast
     */
    peakDemand: DemandForecast;
    /**
     * 
     * @type {DemandForecast}
     * @memberof AreaDemandForecast
     */
    peakUsage: DemandForecast;
}

export function AreaDemandForecastFromJSON(json: any): AreaDemandForecast {
    return AreaDemandForecastFromJSONTyped(json, false);
}

export function AreaDemandForecastFromJSONTyped(json: any, ignoreDiscriminator: boolean): AreaDemandForecast {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'area': AreaFromJSON(json['area']),
        'hourlyForecastList': ((json['hourly_forecast_list'] as Array<any>).map(DemandForecastFromJSON)),
        'peakDemand': DemandForecastFromJSON(json['peak_demand']),
        'peakUsage': DemandForecastFromJSON(json['peak_usage']),
    };
}

export function AreaDemandForecastToJSON(value?: AreaDemandForecast | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'area': AreaToJSON(value.area),
        'hourly_forecast_list': ((value.hourlyForecastList as Array<any>).map(DemandForecastToJSON)),
        'peak_demand': DemandForecastToJSON(value.peakDemand),
        'peak_usage': DemandForecastToJSON(value.peakUsage),
    };
}

