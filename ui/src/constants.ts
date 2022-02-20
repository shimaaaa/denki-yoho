export const Category = {
  DEMAND: '需要',
  USAGE: '使用率'
}

export const Area = {
  HOKKAIDO: '北海道',
  TOHOKU: '東北',
  TOKYO: '東京',
  CHUBU: '中部',
  HOKURIKU: '北陸',
  KANSAI: '関西',
  CHUGOKU: '中国',
  SHIKOKU: '四国',
  KYUSHU: '九州',
  OKINAWA: '沖縄',
} as const;
export type Area = typeof Area[keyof typeof Area];

export function getAreaValueFromKey(key: string): string {
  // FIXME
  for (const [akey, avalue] of Object.entries(Area)) {
    if (akey === key.toUpperCase()) {
      return avalue;
    }
  }
  throw Error(`invalid area ${key}`);
}
