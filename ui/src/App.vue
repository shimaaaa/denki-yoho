<script setup lang="ts">
  import { reactive } from 'vue';
  import { Category } from './constants';
  import ForecastComponent from './components/Forecast.vue';
  import { AreaDemandForecast, DemandForecastData } from './models/forecast';
  import { DenkiYohoApiClient } from './api_client'

  interface State {
    areaDemandForecasts: Array<AreaDemandForecast>
  }
  const state = reactive<State>({
    areaDemandForecasts: [],
  })
  const loadForecastData = async () => {
    const data = await DenkiYohoApiClient.listForcasts();
    state.areaDemandForecasts = data
  }
  loadForecastData();

</script>

<template>
    <el-container>
      <el-header>でんき予報</el-header>
      <el-main>
        <el-row v-for="(areaDemandForecast,index) in state.areaDemandForecasts" :key="index">
          <ForecastComponent
            :area-demand-forecast="areaDemandForecast"
          />
        </el-row>
      </el-main>
    </el-container>
</template>
