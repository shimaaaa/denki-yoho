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

/**
 * An enumeration.
 * @export
 * @enum {string}
 */
export enum Area {
    Hokkaido = 'hokkaido',
    Tohoku = 'tohoku',
    Tokyo = 'tokyo',
    Chubu = 'chubu',
    Hokuriku = 'hokuriku',
    Kansai = 'kansai',
    Chugoku = 'chugoku',
    Shikoku = 'shikoku',
    Kyushu = 'kyushu',
    Okinawa = 'okinawa'
}

export function AreaFromJSON(json: any): Area {
    return AreaFromJSONTyped(json, false);
}

export function AreaFromJSONTyped(json: any, ignoreDiscriminator: boolean): Area {
    return json as Area;
}

export function AreaToJSON(value?: Area | null): any {
    return value as any;
}

