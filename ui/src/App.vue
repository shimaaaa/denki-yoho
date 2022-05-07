<script setup lang="ts">
  import { reactive } from 'vue';
import { DenkiYohoApiClient } from './api_client';
import ForecastComponent from './components/Forecast.vue';
import { AreaDemandForecast } from './models/forecast';

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
  <div id="app">
    <v-app>
      <v-app-bar color="grey-lighten-2">でんき予報</v-app-bar>
      <v-main>
        <div v-for="(areaDemandForecast,index) in state.areaDemandForecasts" :key="index">
          <ForecastComponent
            :area-demand-forecast="areaDemandForecast"
          />
        </div>
      </v-main>
    </v-app>
  </div>
</template>
