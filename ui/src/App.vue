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
    <el-container>
      <el-header>でんき予報</el-header>
      <el-main>
        <div v-for="(areaDemandForecast,index) in state.areaDemandForecasts" :key="index">
          <ForecastComponent
            :area-demand-forecast="areaDemandForecast"
          />
        </div>
<el-row>
  <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple-light"></div></el-col>
  <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
</el-row>
      </el-main>
    </el-container>
</template>
