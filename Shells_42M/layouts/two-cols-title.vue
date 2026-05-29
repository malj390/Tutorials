<template>
  <div class="slidev-layout two-cols-title h-full w-full">
    <div class="mb-8">
      <slot />
    </div>
    <div class="grid grid-cols-2 gap-6">
      <div class="col-left">
        <slot name="left" />
      </div>
      <div class="col-right">
        <slot name="right" />
      </div>	
    </div>
  </div>
</template>