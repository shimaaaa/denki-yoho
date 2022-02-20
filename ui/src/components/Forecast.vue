<script lang="ts" setup>
  import { PropType } from 'vue'
  import { Forecast } from '../models/forecast';

  const props = defineProps({
    category: String,
    forecasts: Array as PropType<Forecast[]>,
  });
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
  <el-card class="box-card">
    <template #header>
      <div class="card-header">
        <span>{{ props.category }}ピーク時</span>
      </div>
    </template>
    <div v-for="(forecast, index) in props.forecasts" :key="index" class="text item">
      <el-row>
        <el-col>
          {{ forecast.areaLabel }} ({{forecast.hourRangeLabel}})
        </el-col>
      </el-row>
      <el-row>
        <el-col>
          <el-progress :percentage="forecast.ratioPc" />
        </el-col>
      </el-row>
    </div>
  </el-card>
</template>
