import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Configuracao {
  id: number;
  data: string;
  cec: string;
  memoria: number;
  mips: number;
  observacao: string;
}

@Injectable({
  providedIn: 'root'
})
export class ConfiguracoesService {

  private apiUrl = 'http://127.0.0.1:8000/configuracoes';

  constructor(private http: HttpClient) { }

  getAllLatestConfiguracoes(): Observable<Configuracao[]> {
    return this.http.get<Configuracao[]>(`${this.apiUrl}/latest`);
  }

  getLastConfiguracao(cec: string): Observable<Configuracao> {
    return this.http.get<Configuracao>(`${this.apiUrl}/latest/${cec}`);
  }

  createConfiguracao(configuracao: Configuracao): Observable<Configuracao> {
    return this.http.post<Configuracao>(`${this.apiUrl}/`, configuracao);
  }

  deleteConfiguracao(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }

}
