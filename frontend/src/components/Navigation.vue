<script>

export default{
    name: 'x',
    data(){
        return{
            dataAtual: new Date().toLocaleDateString(),
            modulos: [
                {
                    'nome': 'PACIENTES',
                    'descricao': 'Gerenciamento dos pacientes da clínica.'
                },
                {
                    'nome': 'MÉDICOS',
                    'descricao': 'Gerenciamento dos médicos da clínica.'
                },
                {
                    'nome': 'FUNCIONÁRIOS',
                    'descricao': 'Gerenciamento dos funcionários da clínica.'
                },
                {
                    'nome': 'PRODUTOS',
                    'descricao': 'Gerenciamento dos produtos úteis.'
                },
            ],
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
        <v-row>
            <v-col v-for="modulo in modulos" class="d-flex flex-column align-center justify-center">
                <v-card height="220" width="250" class=" text-center card-modulo rounded-xl">
                    <h2 class="text-secondary mt-7">{{ modulo.nome }}</h2>
                    <p class="mx-6 text-subtitle-1 font-weight-medium my-5">{{ modulo.descricao }}</p>
                    <v-btn class="rounded-pill bg-secondary">Acessar</v-btn>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
  </v-container>
</template>

<style scoped>
.font-lora{
  font-family: lora;
}
</style>
