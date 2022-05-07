<script lang="ts" setup>
  import { PropType } from 'vue'
  import { AreaDemandForecast } from '../models/forecast';

  const props = defineProps({
    areaDemandForecast: AreaDemandForecast,
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
        <span>{{ props.areaDemandForecast.areaLabel }}エリア</span>
      </div>
    </template>
  </el-card>
</template>
