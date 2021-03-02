import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { from } from 'rxjs';
import { DepartmentComponent } from './department/department.component';

import {EmployeesComponent} from './employees/employees.component'
const routes: Routes = [

  {path: 'employee', component:EmployeesComponent},
  {path: 'department', component:DepartmentComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
