import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ConfiguracaoFormComponent } from './configuracao-form/configuracao-form.component';

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'configuracoes/:cec', component: ConfiguracaoFormComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
