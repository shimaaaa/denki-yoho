<script setup lang="ts">
  import { reactive } from 'vue';
  import { Category } from './constants';
  import ForecastComponent from './components/Forecast.vue';
  import { Forecast, ForecastData } from './models/forecast';
  import { DenkiYohoApiClient } from './api_client'

  interface State {
    demandForecasts: Array<Forecast>,
    usageForecasts: Array<Forecast>,
  }
  const state = reactive<State>({
    demandForecasts: [],
    usageForecasts: [],
  })
  const loadForecastData = async () => {
    const data = await DenkiYohoApiClient.listForcasts();
    state.demandForecasts = data.demand;
    state.usageForecasts = data.usage;
  }
  loadForecastData();

</script>

<template>
    <el-container>
      <el-header>でんき予報</el-header>
      <el-main>
        <el-row>
          <ForecastComponent
            :category="Category.DEMAND"
            :forecasts="state.demandForecasts"
          />
        </el-row>
        <el-row>
          <ForecastComponent
            :category="Category.USAGE"
            :forecasts="state.usageForecasts"
          />
        </el-row>
      </el-main>
    </el-container>
</template>

