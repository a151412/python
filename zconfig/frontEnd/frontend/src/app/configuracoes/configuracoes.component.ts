import { Component, OnInit } from '@angular/core';
import { ConfiguracoesService } from '../configuracoes.service';

@Component({
  selector: 'app-configuracoes',
  templateUrl: './configuracoes.component.html',
  styleUrls: ['./configuracoes.component.css']
})
export class ConfiguracoesComponent implements OnInit {

  configuracao: any = {};
  cec: string = '';

  constructor(private configuracoesService: ConfiguracoesService) { }

  ngOnInit(): void {
    this.getLastConfiguracao();
  }

  getLastConfiguracao(): void {
    this.configuracoesService.getLastConfiguracao(this.cec).subscribe(data => {
      this.configuracao = data;
    });
  }

  saveNewConfiguracao(): void {
    const novaConfiguracao = { ...this.configuracao, data: new Date().toISOString().split('T')[0] };
    this.configuracoesService.createConfiguracao(novaConfiguracao).subscribe();
  }
}
