
/**
 * Este arquivo é o ponto de entrada principal da aplicação Angular.
 * Ele é responsável por inicializar a aplicação e iniciar o módulo principal (AppModule).
 */

import { enableProdMode } from '@angular/core';  // Importa a função para habilitar o modo de produção
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';  // Importa a função para bootstrap da aplicação no navegador
import { AppModule } from './app/app.module';  // Importa o módulo principal da aplicação
import { environment } from './environments/environment';  // Importa as configurações de ambiente

if (environment.production) {
  enableProdMode();  // Habilita o modo de produção se a aplicação estiver em ambiente de produção
}

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));  // Inicializa o AppModule e captura qualquer erro que possa ocorrer
