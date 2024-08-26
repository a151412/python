import { Component, OnInit } from '@angular/core';
import { ConfiguracoesService } from '../configuracoes.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  configuracoes: any[] = [];

  constructor(private configuracoesService: ConfiguracoesService, private router: Router) { }

  ngOnInit(): void {
    this.getAllLatestConfiguracoes();
  }

  getAllLatestConfiguracoes(): void {
    this.configuracoesService.getAllLatestConfiguracoes().subscribe(data => {
      this.configuracoes = data;
    });
  }

  onSelectCeC(cec: string): void {
    this.router.navigate(['/configuracoes', cec]);
  }

  deleteConfiguracao(id: number): void {
    if (confirm("Tem certeza que deseja excluir esta configuração?")) {  // Confirmação antes de excluir
      this.configuracoesService.deleteConfiguracao(id).subscribe(() => {
        this.getAllLatestConfiguracoes();  // Atualiza a lista após exclusão
      });
    }
  }
}
