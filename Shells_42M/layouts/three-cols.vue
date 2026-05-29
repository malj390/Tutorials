<template>
  <div class="slidev-layout three-cols h-full w-full">
    <div class="mb-8">
      <slot />
    </div>
    <div class="grid grid-cols-3 gap-6">
      <div class="col-left">
        <slot name="left" />
      </div>
      <div class="col-middle">
        <slot name="middle" />
      </div>
      <div class="col-right">
        <slot name="right" />
      </div>	
    </div>
  </div>
</template>