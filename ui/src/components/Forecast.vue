<script lang="ts" setup>
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
    <div class="text item">
      <el-row>
        <el-col :span="8"><div class="grid-content bg-purple">aaa</div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple-light"></div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </div>
  </el-card>
</template>
