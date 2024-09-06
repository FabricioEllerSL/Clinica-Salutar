<script>

export default{
    name: 'x',
    data(){
        return{
            dataAtual: new Date().toLocaleDateString(),
        }
    }
}







// EXEMPLO DE INTEGRACAO COM A API

// import axios from 'axios';

// export default {
//   data() {
//     return {
//       pacientes: []
//     }
//   },
//   mounted() {
//     axios.get('http://localhost:8000/api/v1/pacientes/').then(
//       response => {
//         this.pacientes = response.data;
//       }
//     ).catch(error => { console.log(error) })
//   }
// }
</script>

<template>
  <v-container fluid class="fill-height bg-primary">
    <v-app-bar class="bg-white elevation-2 px-4">
      <v-app-bar-title class="font-lora text-h4 text-left text-secondary font-weight-medium">
        Feller Clínica
      </v-app-bar-title>
      <v-app-bar-title class="text-h5 text-grey text-center font-weight-regular">
        PsychoSystem &copy; 2024
      </v-app-bar-title>
      <v-app-bar-title class="text-h5 text-right">
        {{ dataAtual }}
      </v-app-bar-title>
    </v-app-bar>

    <v-container class="text-center">
      <h1 class="text-h1 text-secondary font-lora font-weight-normal">Feller</h1>
      <h1 class="text-h1 text-third font-lora font-weight-normal">Clínica</h1>
      <p class="text-h6 my-5">Sistema de gerenciamento e controle geral</p>
      <v-btn to="/login" class="bg-secondary rounded-lg w-25 pt-6 pb-6 d-flex align-center mx-auto text-h6">LOGIN</v-btn>

    </v-container>
  </v-container>
</template>

<style scoped>
.font-lora{
  font-family: lora;
}
</style>
