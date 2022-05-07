<script lang="ts" setup>
  import { computed } from 'vue';
import { AreaDemandForecast } from '../models/forecast';

  const props = defineProps({
    areaDemandForecast: AreaDemandForecast,
  });
  const peakDemand = computed(() => props.areaDemandForecast?.peakDemand);
  const peakUsage = computed(() => props.areaDemandForecast?.peakUsage);

</script>


<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
}
</style>

<template>
  <v-card class="ma-4 pa-md-4 mx-lg-auto" width="600px">
    <template v-slot:title>
      <span>{{ props.areaDemandForecast.areaLabel }}エリア</span>
    </template>

    <v-card-text>

    <v-table>
      <tbody>
        <tr>
          <td>需要ピーク</td>
          <td>{{ peakDemand?.dateTime.getHours() }}時
          ～{{ peakDemand?.nextHourDateTime.getHours() }}時
          </td>
          <td>{{peakDemand?.ratioPc}}%</td>
        </tr>
        <tr>
          <td>使用率ピーク</td>
          <td>{{ peakUsage?.dateTime.getHours() }}時
          ～{{ peakUsage?.nextHourDateTime.getHours() }}時
          </td>
          <td>{{peakUsage?.ratioPc}}%</td>
        </tr>
      </tbody>
    </v-table>
    </v-card-text>
  </v-card>
</template>
