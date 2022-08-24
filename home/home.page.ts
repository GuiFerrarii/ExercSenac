import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  peso : string
  altura :string
  saida : string
  opcao : string
  resultado : string
 

  constructor() {}


  calcular(){
    var peso = parseFloat(this.peso)
    var altura = parseFloat(this.altura)
    var opcao = this.opcao
    var resultado = parseFloat(this.resultado)

    var resultado = peso / altura **2
    this.saida = resultado.toString()
  }

}
