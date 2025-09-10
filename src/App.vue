<template>
  <div id="app">
    <div v-if="showMemorial" class="memorial-screen">
      <div class="memorial-text" :class="{ 'fade-in': fadeIn, 'fade-out': fadeOut }">
        Rest in peace
      </div>
    </div>
    
    <div v-else class="main-content" :class="{ 'content-fade-in': showMainContent }">
      <div class="counter">
        Total victims: {{ victims.length }}
      </div>
      
      <div class="victims-list">
        <Victim v-for="(victim, index) in victims" :key="index" :person="victim" />
      </div>
    </div>
  </div>
</template>

<script>
import Victim from './components/Victim.vue'
import victimsData from './assets/victims.json'

export default {
  name: 'App',
  components: {
    Victim
  },
  data() {
    return {
      showMemorial: true,
      fadeIn: false,
      fadeOut: false,
      showMainContent: false,
      victims: victimsData
    }
  },
  mounted() {
    this.startMemorialSequence()
  },
  methods: {
    startMemorialSequence() {
      setTimeout(() => {
        this.fadeIn = true
      }, 500)
      
      setTimeout(() => {
        this.fadeOut = true
      }, 3000)
      
      setTimeout(() => {
        this.showMemorial = false
        setTimeout(() => {
          this.showMainContent = true
        }, 100)
      }, 5000)
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  min-height: 100vh;
  background-color: #000;
  color: #fff;
  font-family: Arial, sans-serif;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}

.memorial-screen {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.memorial-text {
  font-size: 12pt;
  font-weight: bold;
  opacity: 0;
  transition: opacity 2s ease-in-out;
  text-align: center;
}

.memorial-text.fade-in {
  opacity: 1;
}

.memorial-text.fade-out {
  opacity: 0;
}

.main-content {
  padding: 20px;
  opacity: 0;
  transition: opacity 2s ease-in-out;
}

.main-content.content-fade-in {
  opacity: 1;
}

.counter {
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
  padding: 20px;
  border-bottom: 2px solid #333;
}

.victims-list {
  max-width: 800px;
  margin: 0 auto;
}

</style>