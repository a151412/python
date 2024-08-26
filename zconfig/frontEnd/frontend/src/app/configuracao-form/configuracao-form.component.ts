import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ConfiguracoesService } from '../configuracoes.service';

@Component({
  selector: 'app-configuracao-form',
  templateUrl: './configuracao-form.component.html',
  styleUrls: ['./configuracao-form.component.css']
})
export class ConfiguracaoFormComponent implements OnInit {

  cec: string = '';
  configuracao: any = {};

  constructor(
    private route: ActivatedRoute,
    private configuracoesService: ConfiguracoesService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.cec = this.route.snapshot.paramMap.get('cec') || '';
    this.getLastConfiguracao();
  }

  getLastConfiguracao(): void {
    this.configuracoesService.getLastConfiguracao(this.cec).subscribe(data => {
      this.configuracao = data;
    });
  }

   saveNewConfiguracao(): void {
    const novaConfiguracao = { ...this.configuracao, data: new Date().toISOString().split('T')[0] };
    this.configuracoesService.createConfiguracao(novaConfiguracao).subscribe(() => {
      this.router.navigate(['/dashboard']);  // Redireciona para o dashboard após salvar
     });
  }
}
